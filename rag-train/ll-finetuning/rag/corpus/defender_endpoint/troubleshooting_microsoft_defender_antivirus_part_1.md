# Troubleshooting: Microsoft Defender Antivirus (1006)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1006 (MALWAREPROTECTION_MALWARE_DETECTED) when Microsoft Defender Antivirus detects malware or potentially unwanted software?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1006 is logged with the message: The antimalware engine found malware or other potentially unwanted software.

## Error Codes
- `1006`

## Root Causes
1. Malware or potentially unwanted software detected by the antimalware engine.

## Remediation Steps
1. Review the event details including: Name (Threat name), Name (Threat name ID), Severity (e.g., Low, Moderate, High, or Severe), Category (e.g., Any threat or malware type), Path (File path), Detection Origin (e.g., Unknown, Local computer, Network share, Internet, Incoming traffic, or Outgoing traffic), Detection Type (e.g., Heuristics, Generic, Concrete, or Dynamic signature), Detection Source (e.g., User, System, Real-time, IOAV, NIS, IEPROTECT, Early Launch Antimalware (ELAM), Remote attestation, Antimalware Scan Interface (AMSI), UAC), Status, User (Domain\User), Process Name (Process in the PID), Signature Version (Definition version), Engine Version (Antimalware Engine version).
2. For more information, see the following details as provided in the event.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
