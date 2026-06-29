# Hardening: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Hardening

## Scenario / Query
How to configure Microsoft Defender Antivirus in passive mode when using Microsoft Defender for Endpoint with a non-Microsoft antivirus?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender for Endpoint, non-Microsoft antivirus, Microsoft Defender Antivirus

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use passive mode to allow Microsoft Defender Antivirus to scan files and update itself, but not remediate threats
2. Note: Behavior monitoring via Real Time Protection is not available in passive mode unless Endpoint data loss prevention (DLP) is deployed

## Validation
1. Open PowerShell as Administrator and run: Get-MpComputerStatus | Select-Object AMRunningMode, AMServiceEnabled, AntivirusEnabled. Confirm AMRunningMode shows 'Passive Mode' and AMServiceEnabled is True. 2. Verify that Microsoft Defender Antivirus is not performing remediation by checking that no quarantine actions are logged in Event Viewer under Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. 3. Confirm that the non-Microsoft antivirus is active and reporting its status via the Microsoft Defender for Endpoint portal (Security Center > Endpoints > Antivirus status).

## Rollback
1. Open PowerShell as Administrator and run: Set-MpPreference -DisableRealtimeMonitoring $false to re-enable active mode. 2. If passive mode was set via registry, delete the registry key HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\PassiveMode (if present) and restart the service: Restart-Service WinDefend. 3. Verify active mode by running: Get-MpComputerStatus | Select-Object AMRunningMode, AMServiceEnabled. Confirm AMRunningMode shows 'Normal' and AMServiceEnabled is True. 4. If issues persist, reinstall Microsoft Defender Antivirus via 'Turn Windows Defender Antivirus on or off' in Windows Security settings.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus-when-migrating>
