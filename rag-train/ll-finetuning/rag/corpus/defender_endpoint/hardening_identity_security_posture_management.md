# Hardening: Identity Security Posture Management

**Domain:** Defender for Endpoint
**Subdomain:** Identity Security Posture Management
**Incident Type:** Hardening

## Scenario / Query
How to view and act on identity-related security recommendations for a user in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft 365 with Defender XDR
- **Configuration:** Identity Security Posture Management (ISPM) enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Security recommendations tab for the user.
2. Review the identity-related posture assessments displayed.
3. Select a recommendation to open its details in Microsoft Secure Score.
4. Follow the remediation guidance provided in Secure Score.

## Validation
1. In Microsoft Defender XDR, go to 'Investigate' > 'Users' and search for the target user. 2. Click on the user to open their profile page. 3. Select the 'Security recommendations' tab. 4. Verify that the list of identity-related posture assessments is displayed and matches expected recommendations. 5. Click on any recommendation and confirm it opens the corresponding details in Microsoft Secure Score. 6. In Secure Score, verify that the recommendation shows the current status (e.g., 'To address' or 'Completed') and that the remediation guidance is present.

## Rollback
1. If the remediation guidance in Secure Score was applied (e.g., enabling MFA, removing unused accounts), reverse the specific action taken (e.g., disable MFA for the user, re-add the account). 2. If no changes were made, no rollback is needed. 3. If the user profile page or Security recommendations tab is not loading, verify that Identity Security Posture Management (ISPM) is enabled in the tenant settings and that the user has the required licenses (Microsoft 365 E5 or add-on). 4. If issues persist, contact Microsoft Support with the user's UPN and tenant ID.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
