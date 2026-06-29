# Incident Response: Incident Response

**Domain:** Governance
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I configure and test an automated incident response playbook in Microsoft 365 Defender to contain a compromised user account?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft 365 Defender
- **Configuration:** Automation rules and playbooks in Microsoft 365 Defender (Azure Logic Apps integration)

## Symptoms
- Suspicious sign-in activity from an unfamiliar location
- Multiple failed authentication attempts followed by a successful logon
- User reports receiving password reset notifications they did not initiate

## Error Codes
N/A

## Root Causes
1. No automated incident response playbook configured to disable a compromised user account
2. Lack of testing of the playbook before an actual incident

## Remediation Steps
1. Create a playbook in Microsoft 365 Defender using Azure Logic Apps that triggers on a 'User compromised' incident.
2. Configure the playbook to automatically disable the user account in Azure AD using the 'Disable user' action.
3. Add a step to send an alert to the security operations team via email or Teams.
4. Test the playbook by simulating a user compromise incident using the Microsoft 365 Defender simulation capabilities.
5. Review the playbook run history to confirm successful execution and adjust as needed.

## Validation
Navigate to Microsoft 365 Defender > Incidents & alerts > Automation rules. Confirm the playbook is enabled and has triggered successfully on test incidents.

## Rollback
If the playbook incorrectly disables a legitimate user, re-enable the user account in Azure AD manually via the Azure portal or using the Microsoft Graph API.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/automation-rules?view=o365-worldwide>
