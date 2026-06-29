# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot a Conditional Access policy that is interrupting a user's sign-in?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
- User sign-in failure or interruption

## Error Codes
N/A

## Root Causes
1. Device not meeting compliance requirements

## Remediation Steps
1. Find the sign-in event that corresponds to the user's sign-in failure
2. Select the Conditional Access tab to see the specific policy or policies that resulted in the sign-in interruption
3. Review information in the Troubleshooting and support tab for a clear reason why sign-in failed
4. Drill down into the configuration of the policies by selecting the Policy Name
5. Review and edit the policy configuration in the policy configuration user interface

## Validation
1. Sign in as the affected user and attempt the resource access that previously failed. 2. In the Entra admin center, go to Identity > Monitoring & health > Sign-in logs. 3. Locate the user's most recent sign-in event for that resource. 4. Select the event, then select the Conditional Access tab. 5. Verify that the policy previously causing interruption now shows 'Success' or is not listed as a failure. 6. Check the Troubleshooting and support tab to confirm no new policy-related errors are reported.

## Rollback
1. In the Entra admin center, go to Protection > Conditional Access > Policies. 2. Locate the policy that was edited during remediation. 3. Select the policy and restore its original configuration (e.g., revert grant controls, assignments, or conditions). 4. If the policy was disabled, re-enable it; if it was enabled, disable it. 5. Confirm the change by selecting Save. 6. Instruct the affected user to retry sign-in and monitor sign-in logs for recurrence of the original interruption.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
