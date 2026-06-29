import logging
from typing import Dict, Any, List
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)

class ValidationError(Exception):
    pass

class FindingNormalizer:
    """
    Enterprise Data Contract Normalizer.
    
    Acts as a firewall between raw SQLite ingest data and the Django models.
    Guarantees that regardless of whether the finding comes from an old script
    (legacy blob) or a new script (FindingBuilder), the database ONLY receives
    strict Phase 4B enterprise JSON.
    """
    
    VALID_STATUSES = {'PASS', 'FAIL', 'WARNING', 'ERROR'}
    VALID_SEVERITIES = {'CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO'}

    @classmethod
    def normalize_finding(cls, raw_check: Dict[str, Any], scan_id: str) -> Dict[str, Any]:
        if not isinstance(raw_check, dict):
            raise ValidationError(f"Invalid finding payload: Expected dict, got {type(raw_check)}")
            
        check_id = raw_check.get('check_id') or raw_check.get('checkId')
        if not check_id:
            raise ValidationError("Missing required field: check_id")
            
        title = raw_check.get('title', 'Unknown Check')
        
        status = str(raw_check.get('status', raw_check.get('result', 'ERROR'))).upper()
        if status not in cls.VALID_STATUSES:
            logger.warning(f"[Scan:{scan_id}][Check:{check_id}] Invalid status '{status}'. Coercing to ERROR.")
            status = 'ERROR'
            
        details = raw_check.get('details', '')
        if details and isinstance(details, str):
            details = strip_tags(details)

        # Route: Native vs Legacy
        metadata = raw_check.get('metadata', {})
        if isinstance(metadata, dict) and metadata.get('finding_type'):
            normalized = cls._validate_native_schema(raw_check, status, check_id, title)
        else:
            normalized = cls._wrap_legacy_schema(raw_check, status, check_id, title, details)
            
        if status == 'PASS':
            normalized['finding_severity'] = 'INFO'
                
        return normalized

    @classmethod
    def _validate_native_schema(cls, raw_check: Dict, status: str, check_id: str, title: str) -> Dict[str, Any]:
        metadata = raw_check.get('metadata', {})
        
        finding_severity = metadata.get('finding_severity', 'INFO').upper()
        if finding_severity not in cls.VALID_SEVERITIES: finding_severity = 'INFO'
            
        # Parse the ASFF contract into flat Django fields
        context = metadata.get('context', {})
        tech_evidence = metadata.get('technical_evidence', {})
        remediation = metadata.get('remediation', {})
        
        # Safe extraction of raw_output components
        raw_output = tech_evidence.get('raw_output', {})
        
        return {
            'check_id': check_id,
            'title': title,
            'status': status,
            'finding_severity': finding_severity,
            'rule_severity': raw_check.get('severity', 'MEDIUM').upper(),
            'category': raw_check.get('category', 'General'),
            
            # Phase 4B Explicit Fields
            'source_engine': metadata.get('source_engine', 'avaguard-cis-engine'),
            'finding_type': metadata.get('finding_type', 'compliance_misconfiguration'),
            'details': context.get('description', title),
            'why_it_matters': context.get('why_it_matters', ''),
            'error_message': tech_evidence.get('evidence_summary', ''),
            
            # JSON Fields
            'evidence': raw_output,
            'non_compliant_resources': raw_output.get('non_compliant_resources', raw_check.get('non_compliant_resources', [])),
            'references': remediation.get('references', []),
            
            # Remediation
            'remediation': remediation.get('recommended_action', raw_check.get('remediation', '')),
            
            # Metrics
            'compliant_count': raw_check.get('compliant_count', 0),
            'non_compliant_count': raw_check.get('non_compliant_count', 0),
            'total_count': raw_check.get('total_count', 0),
        }

    @classmethod
    def _wrap_legacy_schema(cls, raw_check: Dict, status: str, check_id: str, title: str, details: str) -> Dict[str, Any]:
        severity = str(raw_check.get('severity', 'MEDIUM')).upper()
        if severity not in cls.VALID_SEVERITIES:
            severity = 'MEDIUM'
            
        evidence_dict = {
            "legacy_details": details,
            "compliant_count": raw_check.get('compliant_count', 0),
            "non_compliant_count": raw_check.get('non_compliant_count', 0),
            "total_count": raw_check.get('total_count', 0),
        }
        
        return {
            'check_id': check_id,
            'title': title,
            'status': status,
            'finding_severity': severity,
            'rule_severity': severity,
            'category': raw_check.get('category', 'General'),
            
            'source_engine': 'avaguard-cis-engine-legacy',
            'finding_type': 'legacy_audit_record',
            'details': title,
            'why_it_matters': "Context not provided by legacy scanner.",
            'error_message': "See raw output below.",
            
            'evidence': evidence_dict,
            'non_compliant_resources': raw_check.get('non_compliant_resources', []),
            'references': [],
            
            'remediation': raw_check.get('remediation', 'Consult CIS Benchmarks.'),
            
            'compliant_count': raw_check.get('compliant_count', 0),
            'non_compliant_count': raw_check.get('non_compliant_count', 0),
            'total_count': raw_check.get('total_count', 0),
        }
