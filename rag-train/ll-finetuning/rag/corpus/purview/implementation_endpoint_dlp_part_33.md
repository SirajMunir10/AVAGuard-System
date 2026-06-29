# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure printer groups and assign DLP policy actions to printers in Microsoft Purview Endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policies with printer groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a printer group named Legal printers and add individual printers (with an alias) by their friendly name; for instance: legal_printer_001, legal_printer_002, and legal_color_printer. (You can select multiple parameters at once to help you unambiguously identify a specific printer.)
2. Assign the policy actions to the group in a DLP policy: Allow (audit with no user notifications or alerts), Audit only (you can add notifications and alerts), Block with override (blocks the action, but the user can override), Block (blocks no matter what).

## Validation
1. Verify the printer group exists: Run `Get-DlpPrinterGroup -Identity 'Legal printers'` in Exchange Online PowerShell. 2. Confirm printers are members: Run `Get-DlpPrinterGroup -Identity 'Legal printers' | Select-Object -ExpandProperty Members`. 3. Validate DLP policy assignment: Run `Get-DlpCompliancePolicy | Where-Object {$_.Mode -ne 'PendingDeletion'}` and check that the policy includes the printer group with the intended action (e.g., Block). 4. Test the policy by attempting to print a sensitive document to one of the listed printers and confirm the expected behavior (e.g., block with override prompt).

## Rollback
1. Remove the printer group from the DLP policy: Run `Set-DlpCompliancePolicy -Identity '<PolicyName>' -RemovePrinterGroups 'Legal printers'`. 2. Delete the printer group: Run `Remove-DlpPrinterGroup -Identity 'Legal printers'`. 3. If needed, restore any individual printer settings by re-adding printers to a default group or leaving them ungrouped. 4. Verify removal: Run `Get-DlpPrinterGroup` to confirm the group no longer exists.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
