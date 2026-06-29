# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I define the rule logic for a custom detection rule in Microsoft Sentinel?

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
1. Paste the query you designed, built, and tested into the Rule query window.
2. Expand Entity mapping and define up to 10 entity types recognized by Microsoft Sentinel onto fields in your query results.
3. Expand Custom details and define any fields in your query results you want to surface in your alerts as custom details.
4. Expand Alert details and customize otherwise-standard alert properties according to the content of various fields in each individual alert.

## Validation
1. In Microsoft Sentinel, navigate to Analytics > Rule templates and locate your custom rule. Select it and click 'Edit'. 2. On the 'Set rule logic' tab, verify the query in the 'Rule query' window matches the intended KQL logic. 3. Expand 'Entity mapping' and confirm that each entity type (e.g., Account, Host, IP) is mapped to the correct field from the query results. 4. Expand 'Custom details' and confirm that the defined fields appear in the alert details when a test alert is generated. 5. Expand 'Alert details' and verify that the customized properties (e.g., Alert Name, Severity) are populated as expected. 6. Run the rule on a sample data set (e.g., using the 'Test with current data' option) and confirm alerts are created with the correct entities, custom details, and alert properties.

## Rollback
1. In Microsoft Sentinel, navigate to Analytics > Active rules and select the custom rule. 2. Click 'Edit' and revert the 'Rule query' to the previous known working query. 3. Under 'Entity mapping', remove any newly added mappings or restore previous mappings. 4. Under 'Custom details', remove any newly added fields or restore previous custom details. 5. Under 'Alert details', reset any customized properties to their default values. 6. Click 'Review and create' and then 'Save' to apply the rollback. 7. If the rule was newly created and causes issues, disable or delete the rule entirely.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
