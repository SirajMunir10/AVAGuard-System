# Troubleshooting: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot garbage characters appearing in source text when 'Collect original file as evidence' is enabled for paste to browser actions in Endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP rule with 'Collect original file as evidence for all selected file activities on Endpoint' enabled and 'Paste to supported browser' action configured

## Symptoms
- Garbage characters appear in the source text when viewing evidence of paste to browser actions

## Error Codes
N/A

## Root Causes
1. Windows device does not have Antimalware Client Version 4.18.23110 or newer installed

## Remediation Steps
1. Select Actions > Download to view the actual content
2. Ensure Windows devices have Antimalware Client Version 4.18.23110 or newer installed

## Validation
1. On a Windows device with Endpoint DLP, trigger a paste-to-browser action that matches the rule. 2. In Microsoft Purview compliance portal, go to Data Loss Prevention > Activity explorer and locate the event. 3. Select the event and choose Actions > Download to view the evidence file. 4. Confirm the downloaded file displays readable source text without garbage characters. 5. On the same device, run 'Get-MpComputerStatus | Select-Object AMProductVersion' in PowerShell and verify the version is 4.18.23110 or newer.

## Rollback
1. If garbage characters persist, revert the Endpoint DLP rule to not collect original file evidence for paste-to-browser actions: In Microsoft Purview compliance portal, edit the rule and uncheck 'Collect original file as evidence for all selected file activities on Endpoint'. 2. If the Antimalware Client version is older than 4.18.23110, update Windows Defender to the latest version via Microsoft Update or by downloading the latest update from Microsoft Security Intelligence. 3. After rollback, verify the paste-to-browser action no longer collects evidence or that the evidence file is not generated.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
