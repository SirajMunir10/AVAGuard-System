# Troubleshooting: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix a Windows device showing Not compliant for Firewall setting when a group policy overrides Intune policy?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices with conflicting group policy
- **Configuration:** Device security Firewall set to Require

## Symptoms
- Device returns Not compliant for Firewall setting even though Intune device configuration policy turns Firewall on

## Error Codes
N/A

## Root Causes
1. Group policy object overrides the Intune policy when it configures Windows Firewall to allow all inbound traffic or turns off the firewall

## Remediation Steps
1. Remove any conflicting group policy settings
2. Migrate Firewall-related group policy settings to Intune device configuration policy

## Validation
1. Confirm that the conflicting group policy object (GPO) has been removed or disabled by running 'gpresult /h gpresult.html' on the affected device and reviewing the 'Applied Group Policy Objects' section to ensure the firewall-related GPO is no longer listed.
2. Verify that the Intune device configuration policy for Firewall is applied by checking the device's 'Settings > Network & Internet > Windows Firewall' to ensure it is turned on.
3. In the Microsoft Intune admin center, navigate to 'Devices > All devices', select the affected device, and under 'Device compliance' confirm the Firewall setting shows 'Compliant'.
4. Trigger a manual sync on the device by running 'Start-Process -FilePath "C:\Program Files (x86)\Microsoft Intune Management Extension\Microsoft.Management.Services.IntuneWindowsAgent.exe" -ArgumentList "-Sync"' and then recheck compliance status after 15 minutes.

## Rollback
1. Re-enable the previously removed group policy object by linking it back to the appropriate organizational unit in Group Policy Management Console (GPMC).
2. If firewall settings were migrated to Intune, delete the Intune device configuration policy for Firewall by navigating to 'Devices > Configuration profiles', selecting the policy, and clicking 'Delete'.
3. On the affected device, run 'gpupdate /force' to reapply the group policy settings.
4. Verify the device returns to the previous non-compliant state by checking compliance in the Intune admin center under 'Devices > All devices' and confirming the Firewall setting shows 'Not compliant'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
