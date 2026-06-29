# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How to activate an eligible Microsoft Entra role assignment using the Azure mobile app?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Premium P2 or EMS E5 license
- **Configuration:** Privileged Identity Management enabled for Microsoft Entra roles

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Download the Azure mobile app (iOS | Android).
2. Alternatively, select 'Open in mobile' from Privileged Identity Management > My roles > Microsoft Entra roles.
3. Open the Azure mobile app and sign in.
4. Select the Privileged Identity Management card and select My Microsoft Entra roles to view your eligible and active role assignments.
5. Select the role assignment and click on Action > Activate under the role assignment details.
6. Complete the steps to activate and fill in any required details before clicking 'Activate' at the bottom.
7. View the status of your activation requests and your role assignments under My Microsoft Entra roles.

## Validation
1. Open the Azure mobile app and sign in with the same user account that performed the activation.
2. Select the Privileged Identity Management card, then select 'My Microsoft Entra roles'.
3. Verify that the role assignment now shows a status of 'Active' instead of 'Eligible'.
4. Confirm that the activation start and end times match the requested duration.
5. Optionally, navigate to Privileged Identity Management > My roles > Microsoft Entra roles in the Azure portal to cross-check the activation status.

## Rollback
1. Open the Azure mobile app and sign in.
2. Select the Privileged Identity Management card, then select 'My Microsoft Entra roles'.
3. Locate the activated role assignment and select it.
4. Under the role assignment details, select 'Action' and then 'Deactivate' to manually deactivate the role before its scheduled expiry.
5. If the activation was unintended or caused issues, contact your Entra ID administrator to review and revoke the activation via the Azure portal under Privileged Identity Management > Microsoft Entra roles > Active assignments.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role>
