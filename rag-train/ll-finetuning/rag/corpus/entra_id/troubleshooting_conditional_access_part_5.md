# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to use the What If tool to troubleshoot Conditional Access policies?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Conditional Access policies configured

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the What If tool to troubleshoot Conditional Access policies
2. Review sign-in activity reports

## Validation
1. Navigate to the Microsoft Entra admin center (https://entra.microsoft.com).
2. Go to Protection > Conditional Access > What If.
3. Configure the What If tool with the user, application, and conditions that match the sign-in scenario you are troubleshooting.
4. Click 'What If' and confirm that the tool returns the expected policy evaluation results (e.g., which policies would apply, grant controls, session controls).
5. Cross-reference the What If results with actual sign-in logs by going to Identity > Monitoring & health > Sign-in logs, selecting a relevant sign-in event, and reviewing the 'Conditional Access' tab to verify that the policies listed match the What If evaluation.

## Rollback
1. If the What If tool reveals unexpected policy application, review the affected Conditional Access policies by navigating to Protection > Conditional Access > Policies.
2. For each policy that should not apply, either disable the policy by setting 'Enable policy' to 'Off' and saving, or modify the policy's assignments (e.g., users/groups, cloud apps, conditions) to exclude the affected scenario.
3. If a policy is missing from the expected results, enable or adjust the policy as needed.
4. After changes, re-run the What If tool with the same parameters to confirm the corrected evaluation.
5. Monitor sign-in logs for the affected user to ensure the desired policy behavior is enforced.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
