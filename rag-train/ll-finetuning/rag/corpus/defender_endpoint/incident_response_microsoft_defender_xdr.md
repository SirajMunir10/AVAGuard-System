# Incident Response: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Incident Response

## Scenario / Query
How to trigger remediation actions on a user from the Microsoft Defender XDR user investigation overview page?

## Environment Context
- **Tenant Type:** Microsoft 365 with Microsoft Defender XDR and Microsoft Entra ID
- **Configuration:** User investigation overview page in Microsoft Defender XDR

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the user investigation Overview page in Microsoft Defender XDR.
2. Use the Actions menu to trigger remediation actions.
3. Available actions include: Enable, disable, or suspend the user in Microsoft Entra ID.
4. Require the user to sign in again or force a password reset.
5. View Microsoft Entra account settings, related governance, the user's owned files, or shared files.

## Validation
1. Navigate to the Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to 'Incidents & alerts' > 'Incidents' and select the relevant incident.
3. In the incident details, locate the user under 'Users' and click the user name to open the user investigation overview page.
4. Confirm the 'Actions' menu is visible and contains the expected options: 'Enable user', 'Disable user', 'Suspend user', 'Require sign-in again', 'Force password reset', 'View account settings', 'View governance', 'View owned files', 'View shared files'.
5. Perform a test action (e.g., 'Require sign-in again') on a non-critical user and verify the action is executed successfully by checking the action history or activity log.
6. Confirm the user's status in Microsoft Entra ID (https://entra.microsoft.com) reflects the change (e.g., sign-in required flag is set).

## Rollback
1. If a remediation action (e.g., disable user) caused unintended issues, re-enable the user from the same user investigation overview page by selecting 'Enable user' from the 'Actions' menu.
2. If a password reset was triggered and caused lockout, use the 'Force password reset' action again to issue a new temporary password, or manually reset the password in Microsoft Entra ID.
3. If a user was suspended, use the 'Enable user' action to restore access.
4. For any action, verify the user's ability to sign in by testing authentication or checking sign-in logs in Microsoft Entra ID.
5. If the 'Actions' menu is not responding, use Microsoft Entra ID directly (https://entra.microsoft.com) to revert the change (e.g., enable user, reset password).

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
