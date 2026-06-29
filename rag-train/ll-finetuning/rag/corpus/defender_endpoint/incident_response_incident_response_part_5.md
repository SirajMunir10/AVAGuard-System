# Incident Response: Incident Response

**Domain:** Defender for Endpoint
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
During an incident response investigation in Microsoft Defender for Endpoint, you need to collect a full memory dump from a compromised Windows 10 device. What are the documented steps to initiate a live response session and collect a memory dump using the built-in tools?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Live response must be enabled in the Microsoft 365 Defender portal under Settings > Endpoints > Advanced features. The user must have the appropriate RBAC permissions (e.g., 'Live response' permission).

## Symptoms
- Suspicious process activity observed on a device
- Need to capture volatile memory for forensic analysis

## Error Codes
N/A

## Root Causes
1. Memory dump collection is required to analyze in-memory artifacts during incident response

## Remediation Steps
1. 1. In the Microsoft 365 Defender portal (https://security.microsoft.com), go to Device inventory and select the compromised device.
2. 2. Click 'Initiate Live Response' to start a live response session.
3. 3. In the live response console, run the command: `analyze` (or `memory dump` depending on the version; the documented command is `memory dump` to collect a full memory dump).
4. 4. Wait for the command to complete; the memory dump file will be available for download from the live response file collection.
5. 5. Download the memory dump file for offline analysis using a tool like WinDbg or Volatility.

## Validation
Verify that the memory dump file (e.g., Memory.dmp) appears in the live response file list and can be downloaded successfully.

## Rollback
No rollback needed; memory dump collection is a read-only forensic action.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/live-response-commands>
