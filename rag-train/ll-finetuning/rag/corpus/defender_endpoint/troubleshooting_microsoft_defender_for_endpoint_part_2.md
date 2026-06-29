# Troubleshooting: Microsoft Defender for Endpoint (577)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
Microsoft Defender for Endpoint service does not start after onboarding, with error 577 or 1058

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Devices that have not yet received the August 2020 (version 4.18.2007.8) update to Microsoft Defender Antivirus

## Symptoms
- Onboarding successfully completes
- Error 577 when trying to start the service
- Error 1058 when trying to start the service

## Error Codes
- `577`
- `1058`

## Root Causes
1. Microsoft Defender Antivirus is disabled by a system policy
2. Third-party antimalware client is running and the Early Launch Antimalware (ELAM) driver is not enabled
3. DisableAntiSpyware or DisableAntiVirus policy is set

## Remediation Steps
1. Verify that the following Windows Defender policies are cleared: DisableAntiSpyware, DisableAntiVirus
2. In Group Policy, ensure there are no entries such as: <Key Path="SOFTWARE\Policies\Microsoft\Windows Defender"><KeyValue Value="0" ValueKind="DWord" Name="DisableAntiSpyware"/></Key> or <Key Path="SOFTWARE\Policies\Microsoft\Windows Defender"><KeyValue Value="0" ValueKind="DWord" Name="DisableAntiVirus"/></Key>
3. After clearing the policy, run the onboarding steps again

## Validation
Check the registry key HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender to verify that the policy is disabled

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
