# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret threat remediation actions and statuses in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Threat detected but not remediated
- Event 1116 generated for detection telemetry
- Event 1117 with Allow action indicates threat detected but not remediated

## Error Codes
N/A

## Root Causes
1. ThreatSeverityDefaultAction set to None
2. Non-remediating threat actions (Allow, No action, None) configured

## Remediation Steps
1. Use standard remediation actions (Clean, Quarantine, or Remove) in all other environments
2. Review the error description then follow the relevant User action steps
3. Update the definitions then verify that the removal was successful

## Validation
1. Run Get-MpThreatDetection to list recent detections and confirm that the threat's RemediationAction is Clean, Quarantine, or Remove (not Allow, No action, or None).
2. Check Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational for Event 1117 with a Remediation Action of Clean, Quarantine, or Remove.
3. Verify that Event 1116 is followed by a corresponding Event 1117 with a successful remediation status.
4. Run Get-MpComputerStatus and confirm that the AntivirusSignatureVersion is up to date.
5. Perform a full scan with Start-MpScan -ScanType FullScan and confirm no threats remain.

## Rollback
1. If the remediation action was changed to Clean, Quarantine, or Remove and caused false positives, restore the original threat action by running Set-MpPreference -ThreatIDDefaultAction_Ids <ThreatID> -ThreatIDDefaultAction_Action <OriginalAction>.
2. If definitions were updated and caused issues, roll back to the previous definition version using MpCmdRun.exe -Rollback.
3. If a file was quarantined or removed in error, restore it from quarantine via the Microsoft 365 Defender portal or using Get-MpThreat -ThreatID <ID> | Restore-MpThreat.
4. Re-run Get-MpThreatDetection to confirm the threat is now handled with the original action.
5. Re-check Event 1117 to ensure the rollback action is logged.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
