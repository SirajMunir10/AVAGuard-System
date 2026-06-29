# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy to exclude content in Microsoft 365 Copilot location?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with action 'Exclude content in Copilot location Microsoft 365 Copilot (preview)'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Note: Only content in SharePoint and OneDrive for Business can be excluded from being processed by Microsoft 365 Copilot.
2. Configure the DLP policy action: 'Exclude content in Copilot location Microsoft 365 Copilot (preview)'.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was configured with the 'Exclude content in Copilot location Microsoft 365 Copilot (preview)' action. 3. Under 'Locations', confirm that 'SharePoint sites' and 'OneDrive accounts' are selected. 4. Under 'Actions', verify that the action 'Exclude content in Copilot location Microsoft 365 Copilot (preview)' is present and enabled. 5. Use the DLP policy test functionality (if available) to simulate a document in SharePoint or OneDrive and confirm that the policy correctly excludes it from Copilot processing. 6. Optionally, use the Microsoft 365 Copilot audit log to verify that excluded content is not appearing in Copilot responses.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was modified. 3. Under 'Actions', remove or disable the 'Exclude content in Copilot location Microsoft 365 Copilot (preview)' action. 4. Save the policy. 5. Confirm that the policy no longer shows the exclusion action. 6. If the policy was newly created, delete the policy entirely to revert to the previous state.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
