# Remediation: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Remediation

## Scenario / Query
How to remediate a security recommendation in Microsoft Defender for Cloud?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Defender for Cloud, Microsoft cloud security benchmark standard

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Azure portal.
2. Go to Microsoft Defender for Cloud > Recommendations.
3. Select a recommendation.
4. Select Take action.
5. Locate the Remediate section and follow the remediation instructions.

## Validation
1. Sign in to the Azure portal (https://portal.azure.com).
2. Navigate to Microsoft Defender for Cloud > Recommendations.
3. Locate the previously selected recommendation and verify its status is now 'Completed' or 'Resolved'.
4. Optionally, run the following Azure CLI command to confirm the recommendation status: az security recommendation list --query "[?name=='<recommendation-name>'].{status:properties.remediationSteps[0].status}" --output table (replace <recommendation-name> with the actual recommendation ID).
5. Check the 'Healthy resources' count for the recommendation has increased as expected.

## Rollback
1. Sign in to the Azure portal (https://portal.azure.com).
2. Navigate to Microsoft Defender for Cloud > Recommendations.
3. Select the same recommendation and review the 'Remediate' section to identify the specific changes applied.
4. Manually revert each change (e.g., disable a security control, remove a policy assignment, or restore a previous configuration) based on the remediation instructions.
5. If the remediation involved a policy or initiative, use Azure Policy to reset the assignment: az policy assignment delete --name '<assignment-name>' --resource-group '<resource-group>' (if applicable).
6. Verify the recommendation status returns to 'Unhealthy' or 'Not completed' after rollback.

## References
- <https://learn.microsoft.com/en-us/azure/security-center/security-center-remediate-recommendations>
