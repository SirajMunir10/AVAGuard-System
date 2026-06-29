# Hardening: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Hardening

## Scenario / Query
How to configure Microsoft Defender Antimalware compliance settings for Windows devices in Intune?

## Environment Context
- **Tenant Type:** Intune managed
- **Configuration:** Windows compliance policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set Microsoft Defender Antimalware to Require to turn on the Microsoft Defender anti-malware service and prevent users from turning it off.
2. Enter the minimum allowed version of Microsoft Defender anti-malware service, for example 4.11.0.0.
3. Set Microsoft Defender Antimalware security intelligence up-to-date to Require to force the Microsoft Defender security intelligence be up-to-date.
4. Set Real-time protection to Require to turn on real-time protection, which scans for malware, spyware, and other unwanted software.

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > Compliance policies > Policies and select the Windows compliance policy that was configured. 2. Under Compliance settings > Microsoft Defender Antimalware, verify that 'Microsoft Defender Antimalware' is set to 'Require', 'Minimum allowed version of Microsoft Defender anti-malware service' is set to '4.11.0.0', 'Microsoft Defender Antimalware security intelligence up-to-date' is set to 'Require', and 'Real-time protection' is set to 'Require'. 3. On a targeted Windows device, open the Microsoft Defender Antimalware client and confirm that the service is running, the version is at least 4.11.0.0, security intelligence is up-to-date, and real-time protection is enabled. 4. Run the PowerShell command 'Get-MpComputerStatus' on the device and verify that 'AMServiceEnabled' is True, 'AntivirusEnabled' is True, 'AMProductVersion' is at least 4.11.0.0, 'AntispywareEnabled' is True, 'RealTimeProtectionEnabled' is True, and 'IsTamperProtected' is True (if applicable).

## Rollback
1. In the Microsoft Intune admin center, navigate to Devices > Compliance policies > Policies and select the Windows compliance policy that was modified. 2. Under Compliance settings > Microsoft Defender Antimalware, set 'Microsoft Defender Antimalware' to 'Not configured', clear the 'Minimum allowed version of Microsoft Defender anti-malware service' field, set 'Microsoft Defender Antimalware security intelligence up-to-date' to 'Not configured', and set 'Real-time protection' to 'Not configured'. 3. Save the policy and allow it to sync with targeted devices. 4. On a targeted Windows device, open the Microsoft Defender Antimalware client and confirm that the service is running with its previous configuration. 5. Run the PowerShell command 'Get-MpComputerStatus' to verify that the settings have reverted to the previous state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
