# Troubleshooting: Microsoft Defender for Endpoint onboarding (Event ID 1: Offboarding data was found but couldn't be deleted)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot onboarding failures when deploying Microsoft Defender for Endpoint via script in Configuration Manager?

## Environment Context
- **Tenant Type:** Microsoft Configuration Manager version 1606 (July 2016) or later
- **Configuration:** Onboarding configuration files deployed via applications or endpoint protection policies; local scripts for manual onboarding of small number of devices

## Symptoms
- Devices not showing up in the Devices list after one hour
- Onboarding script fails with error events in Event Viewer

## Error Codes
- `Event ID 1: Offboarding data was found but couldn't be deleted`
- `Event ID 2: Onboarding data couldn't be written to registry`
- `Event ID 3: Failed to start SENSE service`
- `System error 577`
- `Error 1058`

## Root Causes
1. Permissions issue on registry key HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection
2. Script not run as administrator
3. SENSE service in intermediate state (Pending_Stopped, Pending_Running)
4. Windows 10 version 1607 with START_PENDING state for SENSE service
5. Microsoft Defender Antivirus ELAM driver disabled by policy

## Remediation Steps
1. Check the result of the script on the device: Open Event Viewer, go to Windows Logs > Application, look for an event from WDATPOnboarding event source
2. For Event ID 1 (Offboarding data found but couldn't be deleted): Check permissions on registry HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection
3. For Event ID 2 (Onboarding data couldn't be written to registry): Check permissions on registry HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection and verify script run as administrator
4. For Event ID 3 (Failed to start SENSE service): Check service health using 'sc query sense' command; ensure not in intermediate state (Pending_Stopped, Pending_Running); rerun script with administrator rights
5. If device is Windows 10 version 1607 and 'sc query sense' returns START_PENDING: reboot the device; if issue persists, upgrade to KB4015217 and try onboarding again
6. If error message is 'System error 577' or 'error 1058': enable Microsoft Defender Antivirus ELAM driver (see Ensure that Microsoft Defender Antivirus is not disabled by a policy)

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
