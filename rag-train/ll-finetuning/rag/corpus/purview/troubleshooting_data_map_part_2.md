# Troubleshooting: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that a custom classification rule in Microsoft Purview is not being applied to any assets during a scan, even though the rule appears active and the scan completes successfully. What are the likely causes and how do you resolve this?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Custom classification rule created in the Microsoft Purview compliance portal, assigned to a sensitivity label policy, and a scan rule set that includes the custom rule.

## Symptoms
- Scan completes without errors
- Custom classification rule never triggers on any asset
- Built-in classification rules work as expected

## Error Codes
N/A

## Root Causes
1. The custom classification rule uses a regular expression that does not match any content in the scanned assets
2. The classification rule is not included in the scan rule set applied to the scan
3. The classification rule is in a 'Disabled' state or its priority is too low relative to other rules

## Remediation Steps
1. Verify that the custom classification rule is enabled in the Microsoft Purview compliance portal under Data classification > Classifiers
2. Ensure the rule is added to the scan rule set used by the scan. In the Microsoft Purview governance portal, navigate to Management > Scan rule sets, select the relevant rule set, and confirm the custom rule is listed
3. Test the regular expression of the custom rule against sample data using the 'Test' feature in the classification rule editor
4. If the rule is still not applied, create a new scan with a dedicated scan rule set that includes only the custom rule to isolate the issue

## Validation
After remediation, run a full scan on a small test data source that contains content matching the custom rule's pattern. Verify in the Purview Data Map that the assets are labeled with the corresponding sensitivity label.

## Rollback
Remove the custom classification rule from the scan rule set and revert to the previous scan rule set configuration. If the rule was disabled, re-enable it only after confirming the root cause.

## References
- <https://learn.microsoft.com/en-us/purview/troubleshoot-classification>
