# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot a Conditional Access policy that is not working as intended?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Policy not working as intended

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the ellipsis on the right side of the policy in a sign-in event to see policy details.
2. Review the left side for details collected at sign-in and the right side for details of whether those details satisfy the requirements of the applied Conditional Access policies.
3. If the information in the event isn't enough, use the sign-in diagnostic tool under Basic info > Troubleshoot Event.
4. Use the What If tool to troubleshoot Conditional Access policies.
5. If submitting a support incident, include the request ID, time, and date from the sign-in event.

## Validation
1. Navigate to Entra ID > Sign-in logs. 2. Locate the sign-in event that was not working as intended. 3. Select the ellipsis on the right side of the policy to view policy details. 4. Confirm the left side shows details collected at sign-in and the right side shows whether those details satisfy the Conditional Access policy requirements. 5. If needed, use the sign-in diagnostic tool under Basic info > Troubleshoot Event. 6. Use the What If tool to test the policy with the same conditions as the problematic sign-in. 7. Verify the policy now behaves as expected.

## Rollback
1. If the remediation steps caused issues, revert any changes made to the Conditional Access policy. 2. If the policy was modified, restore the previous policy configuration using the policy version history or manual reconfiguration. 3. If the policy was disabled, re-enable it. 4. If the sign-in diagnostic tool or What If tool was used, no rollback is needed as these are read-only tools. 5. If a support incident was submitted, note the request ID, time, and date for reference.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
