# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How do I use the Conditional Access What If tool to simulate a sign-in scenario and evaluate policy effects?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Conditional Access policies enabled or in report-only mode

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure the conditions of the sign-in scenario you want to simulate, including: the user, agent identity (Preview), or single tenant service principal you want to test; the cloud apps, user action they would attempt to perform, or sensitive data protected by authentication context they would attempt to access; and the sign-in conditions under which access would be attempted.
2. Initiate a simulation run that evaluates your settings. Only policies that are enabled or in report-only mode are included in an evaluation run.
3. When the evaluation finishes, review the generated report of the affected policies.
4. To gather more information about a Conditional Access policy, use Conditional Access per-policy reporting or the Conditional Access insights and reporting workbook for details about policies in report-only mode or currently enabled.

## Validation
1. Navigate to the Microsoft Entra admin center > Protection > Conditional Access > What If. 2. Configure the sign-in scenario with the same user, cloud app, and conditions used in the simulation. 3. Click 'What If' and confirm the evaluation report lists the expected policies (enabled or report-only) and their effects (grant/block/report-only). 4. Verify that the report includes the policy names and decision details matching the original remediation simulation.

## Rollback
1. If the What If tool shows unexpected policy effects, review the policy configurations under Conditional Access > Policies. 2. Disable or adjust any policy that was incorrectly enabled or misconfigured during remediation. 3. Re-run the What If simulation to confirm the corrected policy behavior. 4. If needed, restore previous policy states using backup or change tracking logs.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if>
