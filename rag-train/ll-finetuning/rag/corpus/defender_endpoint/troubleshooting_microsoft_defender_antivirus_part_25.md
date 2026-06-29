# Troubleshooting: Microsoft Defender Antivirus (1117)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1117 (MALWAREPROTECTION_STATE_MALWARE_ACTION_TAKEN) when Microsoft Defender Antivirus takes action against malware?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1117 is logged with message: The antimalware platform performed an action to protect your system from malware or other potentially unwanted software.

## Error Codes
- `1117`

## Root Causes
1. Microsoft Defender Antivirus detected and took action against malware or other potentially unwanted software.

## Remediation Steps
1. Review the event details including: Name (threat name), Name ID (threat ID), Severity (e.g., Low, Moderate, High, or Severe), Category (e.g., any threat or malware type), Path (file path), Detection Origin (e.g., Unknown, Local computer, Network share, Internet, Incoming traffic, or Outgoing traffic), Detection Type (e.g., Heuristics, Generic, Concrete, or Dynamic signature), Detection Source (e.g., User, System, Real-time, IOAV, NIS, IEPROTECT, Early Launch Antimalware, Remote attestation, Antimalware Scan Interface (AMSI), UAC), User (Domain\User), Process Name (Process in the PID), Action (e.g., Clean or Quarantine).

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that Event ID 1117 is present with the expected details: Name (threat name), Name ID (threat ID), Severity, Category, Path, Detection Origin, Detection Type, Detection Source, User, Process Name, and Action (e.g., Clean or Quarantine).
4. Confirm the Action field shows the intended remediation (e.g., Clean or Quarantine) and that the file path is no longer accessible or the threat is removed.

## Rollback
1. If the action taken was Quarantine and the file is needed, restore it from quarantine using PowerShell: `Get-MpThreatDetection | Where-Object {$_.Action -eq 'Quarantine'} | Restore-MpThreatDetection`.
2. If the action taken was Clean and the file was modified, restore the original file from a known good backup.
3. If the action was incorrect, add an exclusion for the file path or process using: `Add-MpPreference -ExclusionPath "<Path>"` or `Add-MpPreference -ExclusionProcess "<ProcessName>"`.
4. Verify the exclusion is applied with `Get-MpPreference | Select-Object ExclusionPath, ExclusionProcess`.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
