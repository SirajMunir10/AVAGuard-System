# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure a Microsoft Purview DLP policy with understanding of each component's purpose and configuration behavior?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Purview DLP policy configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Understand the purpose of each component in a DLP policy.
2. Configure each component to alter the behavior of the policy as needed.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the newly created DLP policy and verify that each component (e.g., locations, conditions, actions, user notifications, policy tips) is configured as intended. 3. Use the 'Test' mode (if available) to simulate policy evaluation and confirm that the policy triggers correctly for sample sensitive data. 4. Review the DLP activity explorer to ensure policy matches are logged as expected.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the problematic DLP policy. 2. Disable the policy by setting its status to 'Off' to stop enforcement immediately. 3. If the policy was created incorrectly, delete it entirely. 4. Revert any changes to sensitive information types, condition rules, or actions by restoring from a backup or reconfiguring to the previous known-good state. 5. If the policy was deployed in production, consider re-enabling the previous working version of the policy.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
