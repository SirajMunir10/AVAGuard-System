# Troubleshooting: Compliance Policy

**Domain:** Intune
**Subdomain:** Compliance Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve conflicts between Intune compliance policy and Group Policy Object settings for Windows Firewall?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Windows Firewall compliance policy

## Symptoms
- Group policy object overrides the Intune policy

## Error Codes
N/A

## Root Causes
1. Conflicting group policy settings override Intune policy

## Remediation Steps
1. Remove any conflicting group policy settings
2. Migrate Firewall-related group policy settings to Intune device configuration policy
3. Keep default settings, including blocking inbound connections

## Validation
1. On a Windows 10/11 device targeted by both Intune and Group Policy, open an elevated PowerShell prompt and run: 'netsh advfirewall show allprofiles'. Verify that the firewall state, inbound/outbound rules, and default inbound action match the Intune compliance policy settings (e.g., inbound connections blocked).
2. In the Microsoft Intune admin center, navigate to 'Devices' > 'Compliance policies' > select the relevant Windows Firewall compliance policy > 'Device compliance'. Confirm the device shows a 'Compliant' status.
3. Run 'gpresult /h gpresult.html' on the device and open the report. Under 'Computer Configuration' > 'Windows Settings' > 'Security Settings' > 'Windows Defender Firewall with Advanced Security', ensure no GPO settings conflict with the Intune policy (e.g., no GPO enabling inbound connections).
4. In Intune, go to 'Devices' > 'Configuration profiles' and verify that the migrated Firewall settings are applied and show 'Succeeded' status.

## Rollback
1. If conflicts persist, reapply the original Group Policy settings: On a Domain Controller, open 'Group Policy Management Console', edit the relevant GPO, and restore the previous Firewall rules (e.g., set 'Windows Defender Firewall: Allow inbound connections' to 'Enabled').
2. In Intune, delete or disable the migrated Firewall device configuration profile: Navigate to 'Devices' > 'Configuration profiles', select the profile, and choose 'Delete'.
3. On affected devices, run 'gpupdate /force' to reapply Group Policy, then verify with 'netsh advfirewall show allprofiles' that the original GPO settings are active.
4. In Intune, re-evaluate compliance: Go to 'Devices' > 'Compliance policies' > select the policy > 'Device compliance' and confirm the device returns to its previous compliance state (if it was compliant before).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
