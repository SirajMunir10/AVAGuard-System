# Hardening: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Hardening

## Scenario / Query
How to handle risk detections that do not raise risk to the level where risk-based policies apply?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection
- **Configuration:** Risk-based policies configured with specific risk levels

## Symptoms
- Some risk detections do not raise risk to the level where the policy applies

## Error Codes
N/A

## Root Causes
1. Risk level of the sign-in or user does not match the configured policy level

## Remediation Steps
1. Administrators need to handle those situations manually
2. Administrators can determine that extra measures are necessary, such as blocking access from locations or lowering the acceptable risk in their policies

## Validation
1. Sign in to the Entra admin center (https://entra.microsoft.com) as a Security Administrator or Identity Protection Administrator. 2. Navigate to Protection > Identity Protection > Risky users. 3. Review the list of risky users and confirm that users with risk detections below the policy threshold are visible. 4. Select a user with a risk level lower than the policy threshold (e.g., Low or Medium) and verify that the 'Risk level' and 'Risk detail' fields show the detection without triggering a policy block. 5. Navigate to Protection > Identity Protection > Risky sign-ins and confirm that sign-ins with risk levels below the policy threshold are listed without being blocked. 6. Optionally, run the following Microsoft Graph PowerShell command to list risky users with risk level 'low': Get-MgRiskyUser -Filter "riskLevel eq 'low'"

## Rollback
1. If the remediation involved lowering the acceptable risk in a risk-based policy, revert the policy to its original risk level: a. Navigate to Protection > Identity Protection > Conditional Access policies. b. Select the policy that was modified. c. Under 'Assignments' > 'Risk level', restore the original risk level (e.g., change from 'Low and above' back to 'Medium and above'). d. Save the policy. 2. If the remediation involved blocking access from specific locations, remove those location blocks: a. Navigate to Protection > Conditional Access > Named locations. b. Delete or edit the location entry that was added. c. Update any Conditional Access policies that reference the location to remove the block. 3. If manual user dismissals or confirmations were performed, no automated rollback is possible; document the actions taken for audit purposes.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
