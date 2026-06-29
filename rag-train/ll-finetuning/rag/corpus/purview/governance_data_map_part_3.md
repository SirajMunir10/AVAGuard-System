# Governance: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Governance

## Scenario / Query
A user reports that a newly created custom classification rule in Microsoft Purview is not being applied to any assets during scanning. The rule uses a regular expression pattern that matches sample data in test files, but scans complete without error and no assets are classified. What is the likely root cause and how should it be resolved?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Custom classification rule created in Microsoft Purview compliance portal, assigned to a classification rule set, and that rule set is included in a scan rule set used by a scan.

## Symptoms
- Custom classification rule does not appear in the classification results after a scan completes successfully.
- No errors are reported during the scan execution.
- The rule's regex pattern matches sample data when tested manually outside of Purview.

## Error Codes
N/A

## Root Causes
1. The custom classification rule is not associated with a classification rule set, or the classification rule set is not included in the scan rule set used by the scan.
2. The custom classification rule may be in a 'Disabled' state or its minimum confidence level is set too high, preventing matches from being recorded.

## Remediation Steps
1. Verify that the custom classification rule is published and enabled in the Microsoft Purview compliance portal (Data classification > Classifiers > Custom classifier).
2. Ensure the custom classification rule is added to a classification rule set (Data classification > Classifiers > Rule sets).
3. Confirm that the classification rule set is included in the scan rule set used by the scan (Map > Scans > select scan > Edit scan rule set).
4. If the rule uses a minimum confidence level, lower it to a value that matches the test data (e.g., 60 or lower) and rescan.

## Validation
After applying the remediation steps, run a full scan on the affected data source and verify that the custom classification appears in the classification results for the expected assets.

## Rollback
Remove the custom classification rule from the classification rule set, or disable the rule in the custom classifier settings.

## References
- <https://learn.microsoft.com/en-us/purview/create-custom-classifier>
- <https://learn.microsoft.com/en-us/purview/create-classification-rule-set>
