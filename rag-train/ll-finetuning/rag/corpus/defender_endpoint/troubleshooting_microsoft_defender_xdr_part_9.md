# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
What do system tags identify in an incident in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** System tags

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. System tags identify: A type of attack, like ransomware or credential phishing.
2. Automatic actions, like automatic investigation and response and automatic attack disruption.
3. Defender Experts handling an incident.
4. Critical assets involved in the incident.

## Validation
1. Open the Microsoft Defender portal (https://security.microsoft.com).
2. Navigate to Incidents & alerts > Incidents.
3. Select an incident and review the 'Tags' section in the incident details pane.
4. Confirm that system tags are present and correctly identify: a type of attack (e.g., 'Ransomware', 'Credential phishing'), automatic actions (e.g., 'Automated investigation', 'Attack disruption'), Defender Experts handling (e.g., 'Defender Experts'), or critical assets (e.g., 'Critical asset').
5. Verify that the tags match the expected categories as documented in the source.

## Rollback
1. If system tags are incorrect or missing, no direct rollback is available as tags are automatically assigned by the system.
2. To address incorrect tagging, open a support ticket with Microsoft for review of the incident classification.
3. If tags are missing due to a configuration issue, ensure the tenant is properly licensed for Microsoft Defender XDR and that all required data connectors are enabled.
4. If the issue persists, refer to the official documentation at https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts for further troubleshooting steps.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
