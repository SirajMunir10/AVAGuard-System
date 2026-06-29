# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure printer groups in Microsoft Purview Endpoint DLP to restrict printing of contracts to only legal department printers?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Endpoint DLP policy with printer restrictions; Windows 10/11 21H1+, Windows Server 2022 with KB5020030/KB5019157/KB5020044/KB5020032

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define printer groups using the Printer groups setting in Endpoint DLP configuration.
2. Assign printers to each group using parameters: Friendly printer name, USB printer (with optional USB product ID and USB vendor ID), IP range, Print to file (Microsoft Print to PDF or Microsoft XPS Document Writer), Universal print deployed on a printer, Corporate printer (e.g., \print-server\contoso.com\legal_printer_001), Print to local.
3. Use the printer group in DLP policies scoped to Devices to apply different actions (e.g., block printing except to legal printers).
4. Maximum of 20 printer groups, each with up to 50 printers.

## Validation
1. Verify that the printer groups are correctly defined by navigating to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Printer groups. Confirm that the 'Legal Department Printers' group exists and contains the expected printers (e.g., friendly name, USB IDs, IP range, or network path).
2. Create a test DLP policy scoped to Devices that includes a rule blocking printing of contracts to all printers except those in the 'Legal Department Printers' group. Apply the policy to a test device.
3. On the test device, attempt to print a contract document to a printer not in the group (e.g., a local USB printer). Verify that the print action is blocked and a DLP policy tip appears.
4. On the same device, attempt to print the same contract to a printer listed in the 'Legal Department Printers' group (e.g., \print-server\contoso.com\legal_printer_001). Verify that the print action is allowed.
5. Check the DLP activity explorer for the test device to confirm that the blocked and allowed print events are logged with the correct policy match details.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Printer groups, delete the 'Legal Department Printers' group or remove specific printers from the group as needed.
2. If a test DLP policy was created, navigate to Data Loss Prevention > Policies, locate the test policy, and either delete it or disable it to restore previous printing behavior.
3. On the test device, attempt to print a contract to any printer to confirm that no DLP restrictions are applied.
4. If the issue was caused by misconfiguration (e.g., incorrect printer group definition), correct the printer group settings (e.g., update USB vendor ID or IP range) and reapply the policy.
5. Monitor DLP activity explorer to ensure that no unintended blocks or allows occur after rollback.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
