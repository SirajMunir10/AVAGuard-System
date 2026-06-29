# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate a Conditional Access sign-in failure using Microsoft Entra sign-in logs?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
- User sign-in interruption
- Error page with More Details option

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Reports Reader.
2. Browse to Entra ID > Monitoring & health > Sign-in logs.
3. Find the event for the sign-in to review.
4. Add or remove filters and columns to filter out unnecessary information. Narrow the scope by adding filters like: Correlation ID when you have a specific event to investigate; Conditional Access to see policy failure and success; Scope your filter to show only failures to limit results; Username to see information related to specific users; Date scoped to the time frame in question; Resource to see information related to the resource called.
5. After finding the sign-in event that corresponds to the user's sign-in failure, select the Conditional Access tab.
6. The Conditional Access tab shows the specific policy or policies that resulted in the sign-in interruption.
7. Information in the Troubleshooting and support tab might provide a clear reason as to why a sign-in failed such as a device that didn't meet compliance requirements.
8. To investigate further, drill down into the configuration of the policies by selecting the Policy Name. Selecting the Policy Name shows the policy configuration user interface for the selected policy for review and editing.

## Validation
1. Sign in to the Microsoft Entra admin center as at least a Reports Reader.
2. Browse to Entra ID > Monitoring & health > Sign-in logs.
3. Locate the sign-in event that previously failed by applying filters such as Correlation ID, Username, Date range, or Resource.
4. Confirm the sign-in event now shows a status of 'Success' or that the Conditional Access tab no longer lists the policy that caused the failure.
5. Verify that the user can complete the sign-in without interruption and that the error page with 'More Details' option no longer appears.

## Rollback
1. Sign in to the Microsoft Entra admin center as at least a Conditional Access Administrator.
2. Browse to Entra ID > Protection > Conditional Access > Policies.
3. Locate the policy that was modified during remediation.
4. Revert any changes made to the policy (e.g., re-enable a disabled policy, restore original grant controls, or re-add excluded users/groups).
5. If the policy was deleted, recreate it from backup or original configuration notes.
6. Test the sign-in again to confirm the original failure behavior is restored.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
