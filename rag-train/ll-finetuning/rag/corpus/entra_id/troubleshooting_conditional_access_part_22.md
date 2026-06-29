# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
Why does the 'Require app protection policy' grant not work for Kaizala, Skype for Business, or Visio?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Intune integrated
- **Configuration:** Conditional Access policy with grant control set to 'Require app protection policy'

## Symptoms
- Kaizala, Skype for Business, and Visio do not support the 'Require app protection policy' grant.

## Error Codes
N/A

## Root Causes
1. These applications do not support the 'Require app protection policy' grant control.

## Remediation Steps
1. Use the 'Require approved apps' grant exclusively for these applications.
2. Do not use the 'or' clause between the two grants for these three applications.

## Validation
1. Verify that the Conditional Access policy for Kaizala, Skype for Business, or Visio uses only the 'Require approved client app' grant (not 'Require app protection policy').
   - In the Azure portal, navigate to 'Microsoft Entra admin center' > 'Protection' > 'Conditional Access' > select the policy.
   - Under 'Grant', confirm that only 'Require approved client app' is selected and 'Require app protection policy' is not checked.
2. Test access for a user assigned to the policy:
   - Sign in to the application (e.g., Kaizala) on a supported device.
   - Verify that access is granted and the app is listed as an approved client.
3. Check Conditional Access insights and reporting:
   - Go to 'Monitoring' > 'Sign-in logs' and filter by the policy name.
   - Confirm that sign-ins from the application show 'Success' with the grant control 'Require approved client app'.

## Rollback
1. If the remediation causes access issues, revert the policy to its previous state:
   - In the Microsoft Entra admin center, navigate to 'Protection' > 'Conditional Access' > select the policy.
   - Under 'Grant', re-enable 'Require app protection policy' (if it was previously used) and ensure the 'or' clause is not used between grants.
   - Save the policy.
2. Alternatively, temporarily disable the policy:
   - Set the policy to 'Off' under 'Enable policy' and save.
3. Monitor sign-in logs to confirm that users regain access as before the change.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
