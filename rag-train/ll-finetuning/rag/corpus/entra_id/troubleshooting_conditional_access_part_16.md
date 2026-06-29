# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How do I evaluate which Conditional Access policies apply to a specific user or workload identity using the What If tool?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
- User or workload identity is unexpectedly blocked or allowed
- Need to determine which policies apply to a specific scenario

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select What If to start an evaluation
2. Review the evaluation result report which includes: an indicator showing whether classic policies exist in your environment, policies that apply to your user, agent, or workload identity, and policies that don't apply to your user or workload identity
3. For policies that apply, note the grant controls and session controls that must be satisfied
4. For policies that don't apply, review the reasons why these policies don't apply; for each listed policy, the reason represents the first condition that wasn't satisfied
5. Check the Has filter indicator to see whether the policy has app filters that use custom security attributes

## Validation
1. Navigate to the Microsoft Entra admin center (https://entra.microsoft.com).
2. Go to Protection > Conditional Access > What If.
3. In the What If tool, specify the user or workload identity (e.g., user principal name or service principal ID) and the target scenario (e.g., cloud apps, conditions).
4. Select 'What If' to run the evaluation.
5. Review the evaluation result report:
   - Confirm the 'Classic policies' indicator shows whether classic policies exist.
   - Verify the list of policies that apply to the user or workload identity.
   - Verify the list of policies that do not apply, along with the reason for each.
   - Check the 'Has filter' indicator for policies using app filters with custom security attributes.
6. For each applying policy, note the grant controls and session controls that must be satisfied.
7. Compare the evaluation results with the expected access behavior to confirm the remediation (e.g., the user is now correctly blocked or allowed).

## Rollback
1. If the What If evaluation reveals unintended policy application, identify the specific Conditional Access policy causing the issue.
2. Navigate to Protection > Conditional Access > Policies.
3. Select the problematic policy and set its state to 'Off' or adjust its assignments (e.g., remove the user or workload identity from the policy scope).
4. Alternatively, create a new policy with the correct conditions and exclusions to override the unintended behavior.
5. Re-run the What If tool with the same user or workload identity and scenario to verify the corrected policy application.
6. If the issue persists, review the policy evaluation order and ensure no other policies are conflicting.
7. For advanced recovery, export the current policy configuration via PowerShell (Get-MgIdentityConditionalAccessPolicy) before making changes, then import the previous configuration if needed.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if>
