# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How can I use the Conditional Access What If tool to simulate a sign-in and understand which policies apply to a specific user, agent identity, or single tenant service principal?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies configured
- **Configuration:** Conditional Access policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Conditional Access What If policy tool to simulate a sign-in for a user, agent identity, or single tenant service principal.
2. The simulation estimates how your policies affect this sign-in and generates a report.
3. Use the What If tool and APIs to quickly determine the policies that apply to a specific user, agent identity, or single tenant service principal.

## Validation
1. Navigate to the Microsoft Entra admin center (https://entra.microsoft.com).
2. Go to Protection > Conditional Access > What If.
3. Select the user, agent identity, or single tenant service principal you want to simulate.
4. Optionally configure the cloud apps, conditions (e.g., device platform, location, client apps), and sign-in risk.
5. Click 'What If' to run the simulation.
6. Verify that the generated report lists all expected Conditional Access policies and their effects (e.g., Grant or Block).
7. Confirm that the policies shown match the policies you expect to apply based on the user's configuration and conditions.
8. Optionally, use the Microsoft Graph API (beta) to call the `conditionalAccess/whatIf` endpoint and compare the JSON response with the portal results.

## Rollback
1. If the What If simulation reveals unexpected policy application, review the Conditional Access policies that are listed in the report.
2. For each policy that should not apply, check its assignments (users, cloud apps, conditions) and adjust them as needed.
3. If a policy is missing from the simulation, verify that it is enabled and in 'Report-only' or 'On' mode.
4. If the simulation fails to load or returns an error, ensure the user/principal exists and has the correct licenses (e.g., Microsoft Entra ID P1 or P2).
5. If the simulation results are inconsistent, clear browser cache or use an InPrivate/Incognito session, then retry.
6. If the issue persists, use the Microsoft Graph API to directly query the `conditionalAccess/whatIf` endpoint with the same parameters to isolate portal vs. API issues.
7. As a last resort, disable and re-enable the relevant Conditional Access policies to reset their state, then re-run the simulation.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if>
