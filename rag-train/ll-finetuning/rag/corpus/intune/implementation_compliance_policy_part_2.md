# Implementation: Compliance Policy

**Domain:** Intune
**Subdomain:** Compliance Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure Antivirus compliance check in Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** DeviceStatus CSP - DeviceStatus/Antivirus/Status

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set Antivirus to 'Not configured' (default) to skip antivirus check
2. Set Antivirus to 'Require' to check compliance using antivirus solutions registered with Windows Security Center (e.g., Symantec, Microsoft Defender); device with antivirus disabled or out of date is noncompliant

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Antivirus and verify the policy is set to 'Not configured' or 'Require' as intended.
2. For a device targeted by the policy, run the following command in an elevated PowerShell: (Get-CimInstance -Namespace root\cimv2\security\MicrosoftAntimalware -ClassName MSFT_MpComputerStatus).AntivirusEnabled. Confirm the value matches the expected compliance state.
3. On the same device, check the DeviceStatus/Antivirus/Status CSP by running: (Get-CimInstance -Namespace root\cimv2\mdm\dmmap -ClassName MDM_DeviceStatus_Antivirus01).Status. Ensure the status is '1' (enabled) if 'Require' is set, or any value if 'Not configured'.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Antivirus and set the Antivirus policy back to 'Not configured' (default) to skip the antivirus compliance check.
2. Force a sync on affected devices by running: Start-Process -FilePath "C:\Program Files (x86)\Microsoft\Intune Management Extension\Microsoft.Management.Services.IntuneWindowsAgent.exe" -ArgumentList "-SyncPolicy" -NoNewWindow -Wait.
3. Verify the change by checking the DeviceStatus/Antivirus/Status CSP as in validation step 3; the status should no longer enforce compliance based on antivirus state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
