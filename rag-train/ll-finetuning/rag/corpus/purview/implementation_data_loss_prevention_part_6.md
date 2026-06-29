# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to create a printer group in Microsoft Purview DLP endpoint settings?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open the Microsoft Purview portal and go to Data Loss Prevention > Overview > settings gear icon in the upper right corner > Data Loss Prevention > Endpoint DLP settings > Printer groups.
2. Select + Create printer group.
3. Enter a name for the group.
4. Select Add printer.
5. Enter a Friendly name for the printer. Make sure the name matches the value from the printer's device property details in Device Manager.
6. Select the parameters and provide the values to unambiguously identify the specific printer.
7. Select Add.
8. Add other printers as needed.
9. Select Save and then Close.

## Validation
1. Navigate to Microsoft Purview portal > Data Loss Prevention > Overview > Settings (gear icon) > Data Loss Prevention > Endpoint DLP settings > Printer groups. 2. Confirm the newly created printer group appears in the list with the correct name. 3. Select the group and verify that each added printer displays the expected Friendly name and parameters. 4. Optionally, run a test print from an endpoint device to ensure the printer is correctly identified and DLP policies apply as expected.

## Rollback
1. In the same Printer groups section, select the printer group to be removed. 2. Click the delete icon or select 'Delete group' from the action menu. 3. Confirm the deletion when prompted. 4. If only specific printers need to be removed, edit the group, select the printer, and choose 'Remove printer'. 5. Save the changes and close the settings.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
