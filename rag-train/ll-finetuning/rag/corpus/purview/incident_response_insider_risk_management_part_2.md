# Incident Response: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Incident Response

## Scenario / Query
How to escalate an Insider Risk Management case for investigation to create a new eDiscovery (Premium) case?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Insider Risk Management solution enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal with credentials for an admin account in your Microsoft 365 organization.
2. Go to the Insider Risk Management solution.
3. Select Cases in the left navigation.
4. Select a case, and then select Escalate for investigation on the case action toolbar.
5. In the Escalate for investigation dialog box, enter a name for the new user investigation.
6. If needed, enter notes about the case, and then select Escalate.
7. Review the notice fields and update as appropriate. The values you enter override the values on the template.
8. Select Confirm to create the user investigation case.

## Validation
1. Sign in to the Microsoft Purview portal with an admin account. 2. Navigate to Insider Risk Management > Cases. 3. Confirm the original case is no longer listed in the active cases list (it should be closed or moved). 4. Navigate to eDiscovery (Premium) > Cases. 5. Verify a new case exists with the name entered during escalation. 6. Open the new case and confirm the notes and details match what was provided in the escalation dialog.

## Rollback
1. Sign in to the Microsoft Purview portal with an admin account. 2. Navigate to eDiscovery (Premium) > Cases. 3. Locate the newly created case from the escalation. 4. Select the case and choose 'Delete case' or 'Close case' to remove or deactivate it. 5. Navigate to Insider Risk Management > Cases. 6. If the original case was automatically closed, use the 'Reopen case' option to restore it to active status. 7. Verify the original case is again visible in the active cases list.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
