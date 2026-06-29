# Hierarchical Realistic Scenarios Registry
# Domain -> Subdomain -> Technology / Feature -> List of Scenarios

HIERARCHICAL_CATALOG = {
    "windows": {
        "Active Directory": {
            "Domain Controllers": [
                {"title": "Deploying Read-Only Domain Controllers (RODC) in remote branch office sites", "category": "Deployment", "is_cis": False, "cis_type": "N/A"},
                {"title": "Configuring strict LDAP signing and LDAP channel binding for Domain Controllers", "category": "Configuration", "is_cis": True, "cis_type": "Remediation"},
                {"title": "Demoting offline domain controllers and cleaning up lingering metadata", "category": "Administration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Diagnosing DFS-R SYSVOL replication bottlenecks and journal wrap errors", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Monitoring Domain Controller LSASS memory utilization and LDAP search latency", "category": "Monitoring", "is_cis": False, "cis_type": "N/A"},
                {"title": "Restricting interactive logon rights to Domain Admins via User Rights Assignment", "category": "Security Hardening", "is_cis": True, "cis_type": "Remediation"},
                {"title": "Recovering a deleted Active Directory OU using the Active Directory Recycle Bin", "category": "Incident Response", "is_cis": False, "cis_type": "N/A"},
                {"title": "Auditing privileged group membership changes in Active Directory Domain Admins", "category": "Governance", "is_cis": False, "cis_type": "N/A"},
                {"title": "Automating stale Domain Controller computer object cleanup via PowerShell", "category": "Automation", "is_cis": False, "cis_type": "N/A"},
                {"title": "Integrating Active Directory with Microsoft Defender for Identity sensor telemetry", "category": "Integration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Migrating FRS to DFS-R for SYSVOL replication on legacy Domain Controllers", "category": "Migration", "is_cis": False, "cis_type": "N/A"},
                {"title": "In-place OS upgrade procedures for Windows Server 2012 R2 Domain Controllers", "category": "Upgrade", "is_cis": False, "cis_type": "N/A"},
                {"title": "Designing a highly available multi-site Domain Controller topology with fault domains", "category": "Architecture & Design", "is_cis": False, "cis_type": "N/A"},
                {"title": "Validating Domain Controller configurations against CIS Windows Server Benchmarks", "category": "Compliance", "is_cis": True, "cis_type": "Audit"},
                {"title": "Hunting for DCShadow and DCSync replication attacks using Sysmon event ID 4662", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "Sites and Services": [
                {"title": "Designing custom Active Directory site links and bridgehead servers for replication control", "category": "Architecture & Design", "is_cis": False, "cis_type": "N/A"},
                {"title": "Configuring site link costs and replication intervals for WAN-connected sites", "category": "Configuration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting missing subnets in AD Sites and Services causing slow client logons", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Automating subnet object creation in AD Sites and Services using PowerShell and CSV data", "category": "Automation", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for abnormal replication traffic patterns indicating potential unauthorized site links", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "Replication": [
                {"title": "Diagnosing strict replication consistency errors and lingering object issues in AD", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Monitoring AD replication status using the repadmin command-line tool", "category": "Monitoring", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for unauthorized directory replication attempts indicating DCSync attacks", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "Kerberos": [
                {"title": "Implementing Kerberos Armoring (FAST) for enhanced authentication protection", "category": "Security Hardening", "is_cis": True, "cis_type": "Remediation"},
                {"title": "Troubleshooting Kerberos SPN duplicate errors causing authentication failures", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for Golden Ticket and Silver Ticket usage via abnormal TGS requests in event logs", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Incident response runbook for resetting the KRBTGT account password twice", "category": "Incident Response", "is_cis": False, "cis_type": "N/A"},
            ],
            "Group Policy": [
                {"title": "Deploying AppLocker rules via Group Policy for application whitelisting", "category": "Deployment", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting Group Policy client-side extension (CSE) processing failures", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Auditing unlinked and orphaned GPOs for clean AD governance", "category": "Governance", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for unauthorized malicious GPO creation or modification by compromised admins", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "FSMO": [
                {"title": "Transferring and seizing FSMO roles during a primary domain controller outage", "category": "Administration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Designing FSMO role placement strategy across a multi-domain forest", "category": "Architecture & Design", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting RID master pool exhaustion preventing new object creation", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
            ],
            "AD CS": [
                {"title": "Deploying a two-tier offline root CA and issuing CA hierarchy", "category": "Deployment", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hardening AD CS templates against ESC1 through ESC8 escalation paths", "category": "Security Hardening", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for rogue certificate enrollments using vulnerable AD CS templates", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ]
        }
    },
    "azure": {
        "Entra ID": {
            "MFA": [
                {"title": "Deploying Microsoft Authenticator number matching for all corporate users", "category": "Deployment", "is_cis": True, "cis_type": "Remediation"},
                {"title": "Troubleshooting MFA registration campaign rollout and user prompt delays", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for MFA fatigue attacks and subsequent successful anomalous logons", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "Conditional Access": [
                {"title": "Designing Zero Trust Conditional Access architecture for global enterprises", "category": "Architecture & Design", "is_cis": False, "cis_type": "N/A"},
                {"title": "Configuring Conditional Access policies to block legacy authentication protocols", "category": "Configuration", "is_cis": True, "cis_type": "Remediation"},
                {"title": "Troubleshooting Conditional Access lockouts using the Azure AD sign-in logs", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Automating Conditional Access policy backup and deployment via Microsoft Graph API", "category": "Automation", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for Conditional Access policy evasion through excluded IP ranges or VPN endpoints", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "PIM": [
                {"title": "Deploying Privileged Identity Management (PIM) for Entra ID Global Administrator roles", "category": "Deployment", "is_cis": True, "cis_type": "Remediation"},
                {"title": "Configuring PIM activation requirements including MFA and ticketing system justification", "category": "Configuration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for abnormal PIM role activation patterns combined with high-risk operations", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Auditing active vs eligible PIM assignments for role governance compliance", "category": "Governance", "is_cis": False, "cis_type": "N/A"},
            ],
            "Identity Protection": [
                {"title": "Configuring user risk and sign-in risk policies in Entra ID Identity Protection", "category": "Configuration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Investigating unfamiliar sign-in properties and impossible travel risk events", "category": "Incident Response", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for token theft attacks bypassing Identity Protection risk triggers", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "B2B": [
                {"title": "Designing B2B external collaboration settings and cross-tenant access policies", "category": "Architecture & Design", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting B2B guest user invitation redemption errors and token issues", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for unauthorized data exfiltration initiated by compromised B2B guest accounts", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "App Registrations": [
                {"title": "Auditing multi-tenant App Registrations for overprivileged Microsoft Graph API permissions", "category": "Security Hardening", "is_cis": False, "cis_type": "N/A"},
                {"title": "Automating client secret rotation for Azure AD App Registrations via Azure Key Vault", "category": "Automation", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for malicious OAuth consent grants and illicit application permissions abuse", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "Managed Identities": [
                {"title": "Migrating legacy service principal credentials to System-Assigned Managed Identities", "category": "Migration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting Managed Identity token acquisition failures in Azure Functions", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for privilege escalation paths leveraging overprivileged Managed Identities", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ]
        }
    },
    "intune": {
        "Enrollment": {
            "Windows Enrollment": [
                {"title": "Deploying Windows Autopilot User-Driven mode for remote worker device provisioning", "category": "Deployment", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting Enrollment Status Page (ESP) timeout errors during application installation", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Migrating from SCCM co-management workloads to pure cloud Intune MDM authority", "category": "Migration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for rogue Windows device enrollments attempting to bypass compliance checks", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "Apple ADE": [
                {"title": "Integrating Apple Business Manager (ABM) with Intune for Automated Device Enrollment", "category": "Integration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting MDM push certificate expiration and Apple ADE sync failures", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
            ],
            "Android Enterprise": [
                {"title": "Configuring Android Enterprise Corporate-Owned Dedicated device enrollment profiles", "category": "Configuration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Designing a zero-touch enrollment architecture for Android frontline worker devices", "category": "Architecture & Design", "is_cis": False, "cis_type": "N/A"},
            ],
            "Enrollment Restrictions": [
                {"title": "Configuring Intune enrollment restrictions to block personal Windows device registration", "category": "Security Hardening", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for unauthorized MDM enrollment attempts using leaked user credentials", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ]
        }
    },
    "defender": {
        "Defender for Endpoint": {
            "Onboarding": [
                {"title": "Deploying Microsoft Defender for Endpoint sensor to Windows Server via Group Policy", "category": "Deployment", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting MDE client telemetry blockages and passive mode misconfigurations", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Automating Defender for Endpoint onboarding status checks via Microsoft Graph API", "category": "Automation", "is_cis": False, "cis_type": "N/A"},
            ],
            "Device Isolation": [
                {"title": "Incident response procedure for isolating compromised endpoints using MDE network isolation", "category": "Incident Response", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting device isolation failures and verifying force-tunneling network profiles", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
            ],
            "AIR": [
                {"title": "Configuring Automated Investigation and Remediation (AIR) approval levels for server groups", "category": "Configuration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Reviewing AIR action center logs to validate automated malware containment accuracy", "category": "Monitoring", "is_cis": False, "cis_type": "N/A"},
            ],
            "TVM": [
                {"title": "Utilizing Threat and Vulnerability Management (TVM) to prioritize zero-day software patching", "category": "Administration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Validating organizational software inventory baseline compliance using TVM metrics", "category": "Compliance", "is_cis": True, "cis_type": "Validation"},
            ],
            "Indicators": [
                {"title": "Integrating custom threat intelligence feeds into MDE Indicators of Compromise (IoC) lists", "category": "Integration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for advanced persistent threat lateral movement using KQL and custom MDE indicators", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ]
        }
    },
    "sentinel": {
        "Microsoft Sentinel": {
            "Data Connectors": [
                {"title": "Deploying the Azure Monitor Agent (AMA) via Azure Arc for Sentinel Syslog ingestion", "category": "Deployment", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting Sentinel data connector latency and missing Office 365 audit events", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
                {"title": "Integrating third-party firewall logs into Sentinel via Common Event Format (CEF)", "category": "Integration", "is_cis": False, "cis_type": "N/A"},
            ],
            "Analytics Rules": [
                {"title": "Configuring KQL-based analytics rules to detect abnormal Azure resource deployments", "category": "Configuration", "is_cis": False, "cis_type": "N/A"},
                {"title": "Automating Sentinel analytics rule deployment using CI/CD pipelines and Azure DevOps", "category": "Automation", "is_cis": False, "cis_type": "N/A"},
                {"title": "Hunting for defense evasion techniques using correlated KQL queries across multiple data sources", "category": "Threat Hunting", "is_cis": False, "cis_type": "N/A"},
            ],
            "Playbooks": [
                {"title": "Designing SOAR Playbooks to automate malicious IP blocking in Azure Firewall", "category": "Architecture & Design", "is_cis": False, "cis_type": "N/A"},
                {"title": "Troubleshooting Sentinel Logic App playbook execution timeouts and permission errors", "category": "Troubleshooting", "is_cis": False, "cis_type": "N/A"},
            ]
        }
    }
}
