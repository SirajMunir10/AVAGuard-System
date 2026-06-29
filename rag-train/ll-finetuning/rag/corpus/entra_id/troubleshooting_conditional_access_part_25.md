# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot user blocks caused by service dependencies in Conditional Access policies?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
- Users are blocked because cloud apps depend on resources that a Conditional Access policy blocks

## Error Codes
N/A

## Root Causes
1. Cloud apps depend on resources that a Conditional Access policy blocks

## Remediation Steps
1. Review the sign-in log for the application and resource called by the sign-in
2. Combine all the applications and resources in the Conditional Access policy to target this scenario

## Validation
1. Sign in to the Azure portal as a Conditional Access administrator or Global Administrator. 2. Navigate to Identity > Monitoring & health > Sign-in logs. 3. Filter by the affected user and time range. 4. Select the sign-in that was blocked. 5. In the 'Conditional Access' tab, review the policy details and note the 'Resource' column. 6. Confirm that the resource listed is a dependency of the cloud app (e.g., SharePoint Online for Microsoft Teams). 7. Verify that the Conditional Access policy now includes both the cloud app and its dependent resource in the 'Cloud apps or actions' assignment. 8. Ask the user to attempt the sign-in again and confirm the block is resolved.

## Rollback
1. Sign in to the Azure portal as a Conditional Access administrator or Global Administrator. 2. Navigate to Identity > Protection > Conditional Access > Policies. 3. Locate the policy that was modified. 4. Edit the policy and remove the dependent resource from the 'Cloud apps or actions' assignment, reverting to the original app selection. 5. Save the policy. 6. Monitor sign-in logs for the affected user to ensure the original blocking behavior is restored. 7. If the issue persists, consider creating a separate policy for the dependent resource with appropriate exclusions.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
