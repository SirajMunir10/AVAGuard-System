# Troubleshooting: Incident Investigation

**Domain:** Sentinel
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
Why can't I investigate an incident in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Analytics rule with entity mapping

## Symptoms
- Unable to investigate incident
- Investigation graph not available

## Error Codes
N/A

## Root Causes
1. Entity mapping fields were not used when setting up the analytics rule
2. Original incident does not include entities

## Remediation Steps
1. Ensure entity mapping fields are used when setting up the analytics rule
2. Verify that the original incident includes entities

## Validation
1. In Microsoft Sentinel, navigate to Analytics > Active rules and select the relevant analytics rule. 2. Click Edit and review the Entity mapping configuration; confirm that at least one entity type (e.g., Account, Host, IP) is mapped to a field from the query output. 3. Save the rule if changes were made. 4. Trigger a new incident by generating matching events. 5. Open the new incident and click Investigate; verify the investigation graph loads and displays connected entities. 6. Confirm the original incident (if still open) now shows entities in the Entities tab.

## Rollback
1. If the remediation causes issues (e.g., rule fails to run or generates false positives), revert the analytics rule to its previous version: navigate to Analytics > Active rules, select the rule, click Edit, and remove or revert entity mappings to the original state. 2. Save the rule. 3. If the rule was re-created, delete the new rule and restore the original rule from backup or recreate it without entity mappings. 4. Verify the rule runs without errors by checking its trigger history. 5. For incidents that were incorrectly modified, note that entity mappings only affect new incidents; existing incidents remain unchanged and may still lack entities.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
