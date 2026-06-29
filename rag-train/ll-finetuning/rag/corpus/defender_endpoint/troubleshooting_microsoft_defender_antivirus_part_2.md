# Troubleshooting: Microsoft Defender Antivirus (1116)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1116 (MALWAREPROTECTION_STATE_MALWARE_DETECTED) when Microsoft Defender Antivirus detects malware or potentially unwanted software?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1116 is logged with symbolic name MALWAREPROTECTION_STATE_MALWARE_DETECTED
- Message: The antimalware platform detected malware or other potentially unwanted software

## Error Codes
- `1116`

## Root Causes
1. Microsoft Defender Antivirus detected malware or other potentially unwanted software

## Remediation Steps
1. Review the following details from the event: Name: Threat name, Name: Threat name ID, Threat ID: Threat ID, Severity: Severity (examples: Low, Moderate, High, or Severe), Category: Category description (e.g., any threat or malware type), Path: File path, Detection Origin: Detection origin (examples: Unknown, Local computer, Network share, Internet, Incoming traffic, or Outgoing traffic), Detection Type: Detection type (examples: Heuristics, Generic, Concrete, or Dynamic signature), Detection Source: Detection source (examples: User: user initiated, System: system initiated, Real-time: real-time component initiated, IOAV: IE Downloads and Outlook Express Attachments initiated, NIS: Network inspection system, IEPROTECT: IE - IExtensionValidation; this protects against malicious webpage controls, Early Launch Antimalware (ELAM); this includes malware detected by the boot sequence, Remote attestation, Antimalware Scan Interface (AMSI); primarily used to protect scripts (PowerShell, VBS), though it can be invoked by third parties as well, UAC), User: Domain\User, Process Name: Process in the PID, Signature Version: Definition version, Engine Version: Antimalware Engine version
2. User action: No action is required

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
