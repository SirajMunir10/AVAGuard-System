# Remediation: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Remediation

## Scenario / Query
How to use the Fix option to remediate a recommendation in Microsoft Defender for Cloud?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Defender for Cloud

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Azure portal.
2. Go to Microsoft Defender for Cloud > Recommendations.
3. Select a recommendation to remediate.
4. Select Take action > Fix.
5. Follow the rest of the remediation steps.

## Validation
1. Sign in to the Azure portal. 2. Navigate to Microsoft Defender for Cloud > Recommendations. 3. Locate the recommendation that was remediated. 4. Verify that the recommendation status shows 'Completed' or 'Resolved' and that the resource count is zero. 5. Optionally, run the following Azure CLI command to confirm the recommendation is no longer active for the subscription: az security recommendation list --query "[?name=='<recommendation-name>' && properties.state=='Completed']" --output table

## Rollback
1. Sign in to the Azure portal. 2. Go to Microsoft Defender for Cloud > Recommendations. 3. Select the recommendation that was remediated. 4. Review the remediation details to identify the specific changes applied (e.g., resource configurations). 5. Manually revert each change to its previous state using the Azure portal, Azure CLI, or PowerShell. For example, if the fix enabled a security setting, disable it again. 6. If the fix deployed a resource (e.g., a Log Analytics workspace), delete or deprovision that resource. 7. Confirm the resource is restored to its original configuration by checking the recommendation status returns to 'Unhealthy' or 'Open'.

## References
- <https://learn.microsoft.com/en-us/azure/security-center/security-center-remediate-recommendations>
