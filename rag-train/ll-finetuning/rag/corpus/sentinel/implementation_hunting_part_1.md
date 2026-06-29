# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to use Microsoft Sentinel hunting queries to proactively search for security threats across organizational data sources?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Microsoft Sentinel hunting search and query tools to hunt for security threats across your organization's data sources.
2. Use hunting queries to guide you into asking the right questions to find issues in the data you already have on your network.
3. For example, use an out-of-the-box query that provides data about the most uncommon processes running on your infrastructure.

## Validation
1. In the Microsoft Sentinel workspace, navigate to the 'Hunting' blade. 2. Verify that the pre-built hunting queries are listed and can be executed. 3. Run a sample query (e.g., 'Uncommon processes') and confirm results are returned from the connected data sources. 4. Check that the query results include expected fields (e.g., TimeGenerated, ProcessName, Account). 5. Optionally, create a custom hunting query and save it; confirm it appears in the 'My saved queries' list.

## Rollback
1. Delete any custom hunting queries created during validation. 2. If the hunting blade is missing or queries fail, verify the Microsoft Sentinel workspace is properly connected to Log Analytics and data sources are streaming. 3. Reset any modified query parameters to defaults. 4. If the issue persists, re-enable the Microsoft Sentinel solution from the Content hub. 5. Contact support if the hunting feature remains non-functional.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
