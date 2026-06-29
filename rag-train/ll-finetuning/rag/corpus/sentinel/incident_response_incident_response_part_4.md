# Incident Response: Incident Response

**Domain:** Sentinel
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I create a custom analytics rule in Microsoft Sentinel to detect multiple failed logon attempts from a single source IP within a 5-minute window, and then automate the incident response by creating a playbook that blocks the IP using Microsoft Defender for Cloud Apps?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Sentinel enabled
- **Configuration:** Sentinel workspace configured with Windows Security Events (Event ID 4625) connector; Microsoft Defender for Cloud Apps integrated

## Symptoms
- Multiple failed logon events (Event ID 4625) from the same source IP within a short time window
- Security operations team manually investigating each failed logon incident

## Error Codes
N/A

## Root Causes
1. No automated detection rule in place to correlate multiple failed logon attempts
2. No automated response to block malicious IPs

## Remediation Steps
1. In Microsoft Sentinel, navigate to Analytics > Create > Scheduled query rule
2. Define a KQL query that counts Event ID 4625 events grouped by source IP and bin by 5 minutes, filtering for counts > 5
3. Set the rule to run every 5 minutes with a 5-minute lookback
4. Configure incident creation with appropriate severity and tactics (e.g., Credential Access, T1110)
5. Create a playbook (Azure Logic App) that triggers on incident creation and uses the Microsoft Defender for Cloud Apps connector to block the IP address
6. Associate the playbook with the analytics rule under 'Automated response'

## Validation
Trigger the rule by simulating multiple failed logon attempts from a test IP; verify that an incident is created and the playbook executes to block the IP in Defender for Cloud Apps

## Rollback
Disable the analytics rule and remove the IP block from Defender for Cloud Apps via the portal or PowerShell

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
- <https://learn.microsoft.com/en-us/azure/sentinel/automate-responses-with-playbooks>
