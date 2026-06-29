# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
What are the licensing and role requirements to access Microsoft Entra ID Protection risk reports?

## Environment Context
- **Tenant Type:** Microsoft Entra ID P2 or Microsoft Entra Suite license required
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the tenant has a Microsoft Entra ID P2 or Microsoft Entra Suite license.
2. Assign the Global Reader role to view the risk reports.
3. Assign the Reports Reader role to view the sign-in and audit logs.

## Validation
1. Verify the tenant license: In the Microsoft Entra admin center, go to Identity > Overview > Properties. Under 'Tenant properties', confirm the 'License' field shows 'Microsoft Entra ID P2' or 'Microsoft Entra Suite'.
2. Verify the Global Reader role assignment: In the Microsoft Entra admin center, go to Identity > Roles & admins > Roles & admins. Search for 'Global Reader'. Select the role and confirm the user or group that needs to view risk reports is listed under 'Assignments'.
3. Verify the Reports Reader role assignment: In the same Roles & admins blade, search for 'Reports Reader'. Select the role and confirm the user or group that needs to view sign-in and audit logs is listed under 'Assignments'.
4. Test access: Sign in as the user with the assigned roles, navigate to Identity > Protection > Risk detection, and confirm that risk reports are displayed without errors.

## Rollback
1. Remove the Global Reader role assignment: In the Microsoft Entra admin center, go to Identity > Roles & admins > Roles & admins. Select 'Global Reader'. Under 'Assignments', find the user or group, select it, and click 'Remove assignment'. Confirm the removal.
2. Remove the Reports Reader role assignment: In the same Roles & admins blade, select 'Reports Reader'. Under 'Assignments', find the user or group, select it, and click 'Remove assignment'. Confirm the removal.
3. Downgrade the license (if applicable): If a license upgrade was performed, contact your licensing administrator or Microsoft support to revert to the previous license tier (e.g., from Microsoft Entra ID P2 to P1). Note: License changes may require billing adjustments.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
