# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure USB printer enforcement in Microsoft Purview Endpoint DLP settings?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Endpoint DLP policy with printer restriction

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the option to enforce any USB printer while leaving the USB product ID and USB vendor ID unselected.
2. Alternatively, assign a specific USB printer by specifying its USB product ID and USB vendor ID.
3. Get the Device Instance path value from the printer device property details in device manager.
4. Convert that value to the Product ID and Vendor ID format. For more information, see Standard USB identifiers.

## Validation
1. Open Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Device settings. 2. Under 'USB printer enforcement', confirm that either 'All USB printers' is selected (with no specific VID/PID) or the specific printer's VID and PID are listed. 3. On a test Windows device, attempt to print to a USB printer. 4. Verify that the print job is blocked or allowed according to the policy. 5. Check the DLP activity explorer for 'Print' events matching the policy rule.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Device settings, under 'USB printer enforcement', select 'Do not enforce' to disable printer restriction. 2. If a specific printer was assigned, remove its VID and PID entries. 3. On a test device, confirm that printing to USB printers is no longer blocked. 4. Verify that no unintended print blocks are reported in DLP activity explorer.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
