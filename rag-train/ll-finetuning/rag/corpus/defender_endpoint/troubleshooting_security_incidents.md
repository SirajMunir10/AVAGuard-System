# Troubleshooting: Security Incidents

**Domain:** Defender for Endpoint
**Subdomain:** Security Incidents
**Incident Type:** Troubleshooting

## Scenario / Query
How do I triage and investigate a security incident in Defender for Cloud when faced with alert fatigue?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Defender for Cloud enabled on Azure subscriptions

## Symptoms
- Security analysts are overwhelmed by multiple alerts
- Difficulty identifying actual attacks from low-fidelity signals

## Error Codes
N/A

## Root Causes
1. High volume of alerts and low-fidelity signals
2. Lack of correlation between alerts across different tenants

## Remediation Steps
1. Use Defender for Cloud security incidents to view a collection of related alerts
2. Analyze attack sequences using AI algorithms that correlate alerts across Azure subscriptions
3. Review artifacts, related events, and additional information provided in the incident for context

## Validation
1. Navigate to Microsoft Defender for Cloud in the Azure portal. 2. Under 'Security alerts', select 'Security incidents' to confirm that alerts are grouped into incidents. 3. Open a specific incident and verify that related alerts, attack sequence analysis, and artifacts are displayed. 4. Check that the incident includes correlated alerts from multiple Azure subscriptions if applicable. 5. Confirm that the AI-generated attack sequence and additional context (e.g., related events, entities) are present for the incident.

## Rollback
1. If incidents are not grouping alerts as expected, verify that the Defender for Cloud pricing tier is set to 'Standard' (required for incident correlation). 2. Ensure that the 'Security incidents' feature is enabled under Defender for Cloud settings. 3. If incidents are missing or incomplete, review alert suppression rules that may be filtering out alerts. 4. If the issue persists, contact Microsoft Support to investigate potential service-side issues with alert correlation.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-overview>
