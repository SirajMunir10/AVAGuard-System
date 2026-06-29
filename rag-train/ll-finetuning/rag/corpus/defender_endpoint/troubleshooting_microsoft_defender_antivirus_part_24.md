# Troubleshooting: Microsoft Defender Antivirus (1015)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1015 (MALWAREPROTECTION_BEHAVIOR_DETECTED) when Microsoft Defender Antivirus detects suspicious behavior?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1015 is logged with message: The antimalware platform detected suspicious behavior.

## Error Codes
- `1015`

## Root Causes
1. Microsoft Defender Antivirus detected a suspicious behavior.

## Remediation Steps
1. Review the following details in the event: Name: Threat name, Name: Threat name ID: Threat ID, ID: Threat ID, Severity: Severity. Examples: Low, Moderate, High, or Severe, Severity: Severity. Examples: Low, Moderate, High, or Severe, Category: Category description, for example, any threat or malware type., Category: Category description, for example, any threat or malware type., Path: File path, Path: File path, Detection Origin: Detection origin. Examples: Unknown, Local computer, Network share, Internet, Incoming traffic, or Outgoing traffic, Detection Origin: Detection origin. Examples: Unknown, Local computer, Network share, Internet, Incoming traffic, or Outgoing traffic, Detection Type: Detection type. Examples: Heuristics, Generic, Concrete, or Dynamic signature, Detection Type: Detection type. Examples: Heuristics, Generic, Concrete, or Dynamic signature, Detection Source: Detection source for example: User: user initiated, System: system initiated, Real-time: real-time component initiated, IOAV: IE Downloads and Outlook Express Attachments initiated, NIS: Network inspection system, IEPROTECT: IE - IExtensionValidation; this source protects against malicious webpage controls., Early Launch Antimalware (ELAM). This source includes malware detected by the boot sequence., Remote attestation, Antimalware Scan Interface (AMSI). Primarily used to protect scripts (PowerShell, VBS), though it can be invoked by third parties as well., UAC, Status: Status, User: Domain\User, Process Name: Process in the PID, Signature ID: Enumeration matching severity.

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for Event ID 1015 with the message 'The antimalware platform detected suspicious behavior.'
4. Verify the event details include: Name (threat name), Name (threat ID), ID (threat ID), Severity (Low, Moderate, High, or Severe), Category (threat or malware type), Path (file path), Detection Origin (e.g., Unknown, Local computer, Network share, Internet, Incoming traffic, Outgoing traffic), Detection Type (e.g., Heuristics, Generic, Concrete, Dynamic signature), Detection Source (e.g., User, System, Real-time, IOAV, NIS, IEPROTECT, ELAM, Remote attestation, AMSI, UAC), Status, User (Domain\User), Process Name (PID), and Signature ID.
5. Confirm that the threat name and ID match known malware or suspicious behavior patterns.
6. Ensure the file path points to a legitimate location or a known malicious file.
7. Check that the detection origin and type align with the expected behavior (e.g., Heuristics for suspicious behavior).
8. Validate that the detection source is appropriate (e.g., Real-time for active monitoring).
9. If the event is expected (e.g., from a test file), no further action is needed. If unexpected, proceed with remediation (e.g., run a full scan, isolate the device).

## Rollback
1. If the remediation (e.g., quarantine or removal) caused issues (e.g., false positive), restore the file from quarantine:
   - Open Windows Security > Virus & threat protection > Protection history.
   - Find the quarantined item related to Event ID 1015.
   - Select 'Restore' to return the file to its original location.
2. Alternatively, use PowerShell: `Get-MpThreatDetection | Where-Object {$_.ThreatID -eq '<ThreatID>'}` to find the detection, then `Restore-MpThreatDetection -ThreatID <ThreatID>` to restore.
3. If the device was isolated, reconnect it: In Microsoft 365 Defender, go to Device inventory, select the device, and choose 'Release from isolation'.
4. If a full scan was initiated and caused performance issues, stop the scan via Windows Security or PowerShell: `Stop-MpScan`.
5. If the detection was a false positive, submit the file to Microsoft for analysis: https://www.microsoft.com/en-us/wdsi/filesubmission.
6. After rollback, verify the system returns to normal operation and no further alerts are generated.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
