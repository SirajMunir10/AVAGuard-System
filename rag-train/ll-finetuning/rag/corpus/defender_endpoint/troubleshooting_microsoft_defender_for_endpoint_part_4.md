# Troubleshooting: Microsoft Defender for Endpoint (Error code if there's failure in investigation package collection)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect and analyze investigation package data from a device in Microsoft Defender for Endpoint, including scheduled tasks, security event logs, services, SMB sessions, system information, temp directories, users and groups, and support logs?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Windows 10 version 1709 or later with February 2020 update rollup or more recent versions

## Symptoms
- Suspicious process and its state identified
- Suspicious code set to run automatically via scheduled tasks
- Records of sign-in or sign-out activity or other security-related events
- Data exfiltration or lateral movement via SMB sessions
- Suspicious files dropped on the system in temp directories

## Error Codes
- `Error code if there's failure in investigation package collection`

## Root Causes
1. Suspicious process activity
2. Automated routines from scheduled tasks
3. Security event log anomalies
4. SMB session anomalies indicating data exfiltration or lateral movement
5. Suspicious files in temp directories

## Remediation Steps
1. Collect investigation package from device
2. Review CollectionSummaryReport.xls to track data points, commands used, execution status, and error codes
3. Open security event log file using Event viewer
4. Check SMBInboundSessions and SMBOutboundSession files for shared access and communications
5. Review SystemInformation.txt for OS version and network cards
6. Check temp directories files for suspicious files; if message 'The system can't find the path specified' appears, it means no temp directory for that user
7. Review users and groups files for group members
8. Check WdSupportLogs folder for MpCmdRunLog.txt and MPSupportFiles.cab (only on Windows 10 version 1709 or later with specific updates)

## Validation
Use CollectionSummaryReport.xls to verify package includes all expected data and identify any errors

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
