# Governance: Device Configuration â€“ Security Baselines

**Domain:** Defender for Endpoint
**Subdomain:** Device Configuration â€“ Security Baselines
**Incident Type:** Governance

## Scenario / Query
A security operations team notices that several Windows 10 devices in the organization are not compliant with the Microsoft Defender for Endpoint security baseline. The devices are enrolled in Microsoft Intune and the baseline was assigned to all devices. How can the team identify the non-compliant devices and enforce the baseline settings to meet governance requirements?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Intune and Defender for Endpoint
- **Configuration:** Microsoft Defender for Endpoint security baseline profile assigned to all Windows 10 devices via Intune

## Symptoms
- Devices show 'Not compliant' status in Microsoft Intune compliance reports
- Security baseline settings (e.g., attack surface reduction rules, Windows Defender Antivirus settings) are not applied on some devices
- Security operations team cannot enforce baseline settings automatically

## Error Codes
N/A

## Root Causes
1. The security baseline profile is not assigned to all device groups
2. Devices are not checking in to Intune to receive the baseline policy
3. Conflicting policies (e.g., custom configuration profiles) override baseline settings

## Remediation Steps
1. Review the security baseline assignment in Microsoft Intune: ensure the baseline is assigned to the correct Azure AD device groups
2. Verify device check-in status: use the Intune console to check if devices have synced within the last 24 hours
3. Resolve policy conflicts: identify and remove or reorder any custom configuration profiles that override baseline settings
4. Force a device sync: on a test device, go to Settings > Accounts > Access work or school > Info > Sync to trigger policy retrieval
5. Use the Microsoft 365 Defender portal to generate a device compliance report and export the list of non-compliant devices for follow-up

## Validation
After remediation, run the Intune compliance report for the security baseline profile; all assigned devices should show 'Compliant' status. Additionally, verify that the baseline settings are applied on a sample device by reviewing the Windows Security app or using Get-MpPreference in PowerShell.

## Rollback
To roll back a security baseline assignment, remove the baseline profile assignment from the device group in Intune. Devices will revert to their previous configuration after the next policy sync.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines-monitor>
