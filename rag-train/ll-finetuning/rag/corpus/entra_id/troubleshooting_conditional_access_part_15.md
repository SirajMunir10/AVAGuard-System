# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How do I use the What If tool in Conditional Access to evaluate policy conditions?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Microsoft Entra admin center.
2. Go to Entra ID > Conditional Access > Policies > What If.
3. Provide the conditions you want to evaluate.
4. Run the What If evaluation.

## Validation
1. Open a browser and navigate to https://entra.microsoft.com. 2. Sign in with a Global Administrator, Security Administrator, or Conditional Access Administrator account. 3. In the left navigation, select 'Protection' > 'Conditional Access' > 'Policies'. 4. Click 'What If' on the top menu. 5. In the What If tool, configure the conditions (e.g., user, location, cloud app, device state) that match the scenario you want to test. 6. Click 'What If' to run the evaluation. 7. Confirm that the results page lists the applicable Conditional Access policies and their effects (e.g., grant controls, session controls) for the specified conditions. 8. Verify that the output matches the expected policy behavior based on your tenant's configuration.

## Rollback
1. If the What If evaluation produces unexpected results, review the conditions you entered for accuracy (e.g., user, location, app). 2. Check that the Conditional Access policies you expect to apply are enabled and correctly configured in 'Policies' > 'All policies'. 3. If a policy is misconfigured, edit the policy to correct its assignments or controls. 4. If a policy should not apply, adjust its 'Users and groups', 'Cloud apps or actions', or 'Conditions' settings. 5. Re-run the What If evaluation with the corrected conditions to confirm the desired outcome. 6. If the issue persists, consult the official troubleshooting guide at https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if>
