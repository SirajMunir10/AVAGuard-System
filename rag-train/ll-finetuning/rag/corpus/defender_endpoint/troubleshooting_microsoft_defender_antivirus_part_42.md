# Troubleshooting: Microsoft Defender Antivirus (2020)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 2020 indicating that Microsoft Defender Antivirus downloaded a clean file?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2020 is logged with the symbolic name MALWAREPROTECTION_CLOUD_CLEAN_RTORE_FILE_DOWNLOADED

## Error Codes
- `2020`

## Root Causes
1. The antimalware engine downloaded a clean file.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that Event ID 2020 is logged with the symbolic name MALWAREPROTECTION_CLOUD_CLEAN_RTORE_FILE_DOWNLOADED.
4. Confirm the event details show the file was downloaded from the cloud and marked as clean.
5. Optionally, run Get-MpThreatDetection | Where-Object {$_.Resources -like '*<filepath>*'} to verify no active threats are associated with the file.

## Rollback
1. No rollback is required because Event ID 2020 indicates a clean file download and is informational only.
2. If the event is unexpected, review the file path in the event details and verify the file's legitimacy.
3. If the file is suspicious, submit it to Microsoft Defender Security Center for analysis or run a manual scan with 'Start-MpScan -ScanType CustomScan -ScanPath <filepath>'.
4. To suppress logging, configure the event log size or filter rules, but this is not recommended.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
