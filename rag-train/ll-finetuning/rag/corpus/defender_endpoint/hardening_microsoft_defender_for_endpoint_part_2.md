# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
How to reduce CPU utilization caused by Microsoft Defender Antivirus by disabling file hash computation?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Group Policy: Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > MpEngine

## Symptoms
- High CPU utilization from Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
1. File hash computation feature enabled, increasing CPU usage

## Remediation Steps
1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > MpEngine
2. Enable file hash computation features (note: disabling this may reduce security but lower CPU utilization)

## Validation
1. Open Group Policy Management Console (GPMC) and navigate to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > MpEngine. 2. Verify that the policy 'Enable file hash computation feature' is set to 'Disabled'. 3. On a target client, run 'gpupdate /force' and then open PowerShell as Administrator. 4. Execute 'Get-MpPreference | Select-Object -ExpandProperty DisableHashCalculation' and confirm the output is 'True'. 5. Monitor CPU usage via Task Manager or Performance Monitor to confirm reduction in MsMpEng.exe CPU utilization.

## Rollback
1. In the same Group Policy path, set 'Enable file hash computation feature' to 'Not Configured' or 'Enabled'. 2. Run 'gpupdate /force' on affected clients. 3. In PowerShell, execute 'Set-MpPreference -DisableHashCalculation $false' to re-enable hash computation. 4. Verify with 'Get-MpPreference | Select-Object -ExpandProperty DisableHashCalculation' that the value is 'False'. 5. Restart the Microsoft Defender Antivirus service or reboot the system to ensure settings take effect.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
