# Troubleshooting: Data Map (ResourceSetNoMatch)

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Troubleshooting

## Scenario / Query
How do I resolve a 'ResourceSetNoMatch' error when scanning an Azure Data Lake Storage Gen2 account in Microsoft Purview?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Purview Data Map with an ADLS Gen2 source registered and a scan rule set that includes resource set pattern rules.

## Symptoms
- Scan completes but no assets appear in the Data Map for the expected folders.
- The scan status shows 'CompletedWithWarnings' and the warning message includes 'ResourceSetNoMatch'.
- Folders that match a known pattern (e.g., /year=*/month=*/) are not grouped into resource sets.

## Error Codes
- `ResourceSetNoMatch`

## Root Causes
1. The scan rule set does not include a resource set pattern rule that matches the folder structure.
2. The pattern rule is defined but has a syntax error (e.g., missing wildcard or incorrect path prefix).

## Remediation Steps
1. Navigate to the Purview governance portal > Data Map > Scan rule sets.
2. Select the scan rule set used for the ADLS Gen2 scan.
3. Under 'Resource set', verify that a pattern rule exists for the folder hierarchy (e.g., /{Year}/{Month}/).
4. If missing, add a new pattern rule using the documented syntax: start with the container name, then use curly braces for dynamic segments, e.g., /container/{Year}/{Month}/.
5. Save the rule set and re-run the scan.

## Validation
After the scan completes, verify that the expected folders appear as resource set assets in the Data Map and that the scan status is 'Completed'.

## Rollback
Remove the added pattern rule from the scan rule set and re-run the scan to revert to the previous behavior.

## References
- <https://learn.microsoft.com/en-us/purview/concept-resource-sets>
