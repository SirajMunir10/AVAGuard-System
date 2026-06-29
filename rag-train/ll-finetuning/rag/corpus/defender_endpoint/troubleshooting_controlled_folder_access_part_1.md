# Troubleshooting: Controlled Folder Access

**Domain:** Defender for Endpoint
**Subdomain:** Controlled Folder Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate when exclusions do not work with controlled folder access and data loss prevention (DLP)?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** Exclusions don't work if you're using data loss prevention (DLP)

## Symptoms
- Exclusions don't work

## Error Codes
N/A

## Root Causes
1. Exclusions don't work if you're using data loss prevention (DLP)

## Remediation Steps
1. Download and install the Defender for Endpoint client analyzer
2. Run a trace for at least five minutes
3. In the resulting MDEClientAnalyzerResult.zip output file, extract the contents of the EventLogs folder
4. Search for instances of DLP EA in the available .evtx log files

## Validation
1. Download and install the Microsoft Defender for Endpoint Client Analyzer from https://aka.ms/BetaMDEAnalyzer. 2. Run the analyzer with a trace for at least five minutes: `MDEClientAnalyzer.cmd -t`. 3. Locate the output file MDEClientAnalyzerResult.zip and extract its contents. 4. Navigate to the EventLogs folder within the extracted files. 5. Open each .evtx file (e.g., Microsoft-Windows-Windows Defender/Operational.evtx) in Event Viewer or a log parser. 6. Search for events containing 'DLP EA' (Data Loss Prevention - Exchange ActiveSync). 7. Confirm that no such events appear, indicating that DLP is not interfering with Controlled Folder Access exclusions.

## Rollback
1. If the remediation fails or causes issues, re-enable Controlled Folder Access via Group Policy or Microsoft Defender for Endpoint: Set-MpPreference -EnableControlledFolderAccess Enabled. 2. Remove any temporary exclusions added during troubleshooting: Remove-MpPreference -ControlledFolderAccessExcludedPaths 'C:\Temp\ExcludedPath'. 3. If DLP policies were temporarily disabled, re-enable them in the Microsoft Purview compliance portal. 4. Restart the Microsoft Defender Antivirus service: `Restart-Service WinDefend`. 5. Verify that Controlled Folder Access is functioning as expected by testing with a known blocked application.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
