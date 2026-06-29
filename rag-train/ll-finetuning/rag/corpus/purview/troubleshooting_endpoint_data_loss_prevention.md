# Troubleshooting: Endpoint Data Loss Prevention

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
What unexpected behavior can occur when blocking specific file extensions in DLP policies, and how can I mitigate it?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with 'Apply restrictions to only unsupported file extensions' option

## Symptoms
- Applications marked as unallowed might fail to function properly.
- Errors or incomplete workflows may occur.
- Enforcement pop-ups unrelated to user intent may appear.

## Error Codes
N/A

## Root Causes
1. Certain apps might read or temporarily open files like .dll, .json, .tmp during routine processes such as rendering, caching, or validating content.
2. Blocking these extensions can disrupt normal app operations.

## Remediation Steps
1. Before implementing extension-based restrictions, make sure you know which apps interact with these file types during standard operations.
2. Consider alternative controls such as app restrictions or contextual rules to achieve the security goal without disrupting functionality.

## Validation
1. Verify that the DLP policy with 'Apply restrictions to only unsupported file extensions' is not blocking critical file types by reviewing the policy configuration in the Microsoft Purview compliance portal: navigate to Data Loss Prevention > Policies, select the policy, and check the 'Unsupported file extensions' list. 2. On an endpoint, trigger a DLP policy evaluation by attempting to copy or upload a file with an extension (e.g., .dll, .json, .tmp) that is commonly used by applications. 3. Confirm that no unexpected enforcement pop-ups appear and that the application (e.g., a browser or development tool) continues to function without errors. 4. Review DLP activity reports in the compliance portal for any blocked activities related to these extensions to ensure no legitimate workflows are disrupted.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the problematic DLP policy. 2. Edit the policy and remove the specific file extensions (e.g., .dll, .json, .tmp) from the 'Unsupported file extensions' list under the 'Apply restrictions to only unsupported file extensions' setting. 3. Save the policy and allow up to 24 hours for the change to propagate to all endpoints. 4. Alternatively, if the policy is causing widespread disruption, disable the policy temporarily by setting its status to 'Off' until a refined policy can be deployed.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
