# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How to block access from unsupported device platforms like Chrome OS using Conditional Access?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policy with Device platforms condition

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure a policy with a Device platforms condition that includes any device.
2. Exclude supported device platforms from the policy.
3. Set Grant control to Block access.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy created for blocking unsupported device platforms. 4. Open the policy and confirm that under 'Assignments > Device platforms', 'Include' is set to 'Any device' and 'Exclude' lists all supported platforms (e.g., Android, iOS, Windows, macOS). 5. Under 'Access controls > Grant', verify that 'Block access' is selected. 6. Use the 'What If' tool to simulate a sign-in from a Chrome OS device and confirm the policy applies and blocks access. 7. Optionally, sign in from an actual Chrome OS device and verify access is denied.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy created for blocking unsupported device platforms. 4. Either disable the policy by toggling 'Enable policy' to 'Off', or delete the policy entirely. 5. If the policy was deleted, recreate it with the original settings if needed. 6. Verify that access from previously blocked devices is restored by testing sign-in from a Chrome OS device.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
