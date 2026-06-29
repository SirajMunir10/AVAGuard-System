# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I run all hunting queries or a selected subset in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Defender
- **Configuration:** Threat management > Hunting > Queries tab

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Threat management > Hunting, then the Queries tab.
2. Select the Run all queries button, or select a subset of queries using the check boxes to the left of each row and select the Run selected queries button.

## Validation
1. Navigate to Threat management > Hunting > Queries tab.
2. Confirm that the 'Run all queries' button is visible and enabled.
3. Select a subset of queries using check boxes and verify the 'Run selected queries' button appears and is enabled.
4. Run all queries or selected queries and confirm that results are generated and displayed in the 'Results' pane.
5. Check that the query execution status shows 'Completed' for each query run.

## Rollback
1. If running all queries causes performance issues, stop any running queries by selecting the 'Cancel' button next to each query in the 'Results' pane.
2. If unintended queries were executed, clear the results by selecting 'Clear results' from the 'Results' pane options.
3. To revert to the default query set, refresh the Queries tab by selecting the 'Refresh' icon.
4. If custom query selections were saved, remove any saved query groups by navigating to 'Saved queries' and deleting the unwanted group.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
