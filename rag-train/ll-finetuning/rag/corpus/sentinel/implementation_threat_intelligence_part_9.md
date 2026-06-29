# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
How to visualize threat intelligence using a Microsoft Sentinel workbook?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with threat indicators imported via threat intelligence data connector

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. From the Azure portal, go to Microsoft Sentinel.
2. Choose the workspace to which you imported threat indicators by using either threat intelligence data connector.
3. Under the Threat management section of the Microsoft Sentinel menu, select Workbooks.
4. Find the workbook titled Threat Intelligence.
5. Verify that you have data in the ThreatIntelligenceIndicator table.
6. Select Save, and choose an Azure location in which to store the workbook. This step is required if you intend to modify the workbook in any way and save your changes.
7. Now select View saved workbook to open the workbook for viewing and editing.
8. You should now see the default charts provided by the template. To modify a chart, select Edit at the top of the page to start the editing mode for the workbook.
9. Add a new chart of threat indicators by threat type. Scroll to the bottom of the page and select Add Query.
10. Add the following text to the Log Analytics workspace Log Query text box: ThreatIntelligenceIndicator | summarize count() by ThreatType
11. On the Visualization dropdown menu, select Bar chart.
12. Select Done editing, and view the new chart for your workbook.

## Validation
1. Navigate to the Microsoft Sentinel workspace in the Azure portal.
2. Under Threat management, select Workbooks.
3. Confirm the 'Threat Intelligence' workbook appears in the list.
4. Run the following KQL query in the Log Analytics workspace associated with Sentinel:
   ThreatIntelligenceIndicator
   | take 10
   This verifies data exists in the ThreatIntelligenceIndicator table.
5. Open the saved workbook and verify the default charts display data.
6. Scroll to the bottom and confirm the new bar chart for threat indicators by ThreatType is present and populated.

## Rollback
1. Open the 'Threat Intelligence' workbook in edit mode.
2. Delete the custom query added for threat indicators by ThreatType:
   - Select the query item and choose 'Remove'.
3. Revert any other unsaved changes by closing the workbook without saving.
4. If the workbook was saved with unwanted modifications, delete the saved workbook instance:
   - In Workbooks, select the saved workbook, then 'Delete'.
5. Re-create the workbook from the template by selecting the 'Threat Intelligence' template and saving it again.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
