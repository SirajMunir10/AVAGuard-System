# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to configure Windows Defender SmartScreen settings via Group Policy for Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** On-premises Active Directory with Group Policy management
- **Configuration:** Windows Defender SmartScreen Group Policy settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Browse to Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Defender SmartScreen > Explorer.
2. Browse to Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Defender SmartScreen > Microsoft Edge.

## Validation
1. Open Group Policy Management Console (GPMC).
2. Navigate to the GPO containing the SmartScreen settings.
3. Go to Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Defender SmartScreen > Explorer.
4. Verify that the policy 'Configure Windows Defender SmartScreen' is set to 'Enabled' and the option 'Turn on SmartScreen' is selected.
5. Navigate to Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Defender SmartScreen > Microsoft Edge.
6. Verify that the policy 'Configure Windows Defender SmartScreen' is set to 'Enabled' and the option 'Turn on SmartScreen' is selected.
7. On a target client, run 'gpupdate /force' and then open PowerShell as Administrator.
8. Run 'Get-MpPreference' and confirm that 'SmartScreenEnabled' is set to 'True'.
9. Run 'Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name "EnableSmartScreen"' and verify the value is 1.
10. For Microsoft Edge, run 'Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\MicrosoftEdge\PhishingFilter" -Name "EnabledV9"' and verify the value is 1.

## Rollback
1. Open Group Policy Management Console (GPMC).
2. Navigate to the GPO where SmartScreen settings were configured.
3. For Explorer: Go to Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Defender SmartScreen > Explorer.
4. Set the policy 'Configure Windows Defender SmartScreen' to 'Not Configured'.
5. For Microsoft Edge: Go to Computer Configuration > Policies > Administrative Templates > Windows Components > Windows Defender SmartScreen > Microsoft Edge.
6. Set the policy 'Configure Windows Defender SmartScreen' to 'Not Configured'.
7. On affected clients, run 'gpupdate /force' to apply the change.
8. Verify removal by running 'Get-MpPreference' and checking that 'SmartScreenEnabled' is not present or set to default.
9. Confirm registry keys are removed: 'Remove-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\System" -Name "EnableSmartScreen" -ErrorAction SilentlyContinue' and 'Remove-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\MicrosoftEdge\PhishingFilter" -Name "EnabledV9" -ErrorAction SilentlyContinue'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
