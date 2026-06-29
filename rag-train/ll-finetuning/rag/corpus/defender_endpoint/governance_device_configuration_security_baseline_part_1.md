# Governance: Device Configuration â€“ Security Baseline

**Domain:** Defender for Endpoint
**Subdomain:** Device Configuration â€“ Security Baseline
**Incident Type:** Governance

## Scenario / Query
How can I verify that all Windows devices in my tenant are compliant with the Microsoft Defender for Endpoint security baseline and remediate any non-compliant devices?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5 with Defender for Endpoint Plan 2)
- **Configuration:** Security baselines are managed through Microsoft Intune; devices are enrolled in Intune and targeted with the 'Microsoft Defender for Endpoint Baseline' policy.

## Symptoms
- Devices appear as 'Non-compliant' in the Microsoft 365 Defender portal under Device Compliance
- Security recommendations in Microsoft 365 Defender show 'Security baseline' alerts with high severity
- Administrators receive compliance alerts from Intune indicating devices do not meet the Defender for Endpoint baseline

## Error Codes
N/A

## Root Causes
1. Devices are not assigned to the Intune security baseline policy for Defender for Endpoint
2. Devices have outdated or conflicting Group Policy settings that override the Intune baseline
3. Devices are running an unsupported Windows version or are missing required updates

## Remediation Steps
1. In the Microsoft 365 Defender portal, navigate to 'Configuration management' > 'Endpoint security policies' and ensure the 'Microsoft Defender for Endpoint Baseline' policy is assigned to the appropriate device groups.
2. In Intune, go to 'Endpoint security' > 'Security baselines' and select the 'Microsoft Defender for Endpoint Baseline'. Review the settings and assign the policy to all devices.
3. For devices showing non-compliance, use the Intune 'Device compliance' report to identify specific settings that failed. Adjust the baseline settings or update the device as needed.
4. If Group Policy conflicts exist, remove or update the conflicting policies using Group Policy Management Console or by disabling the relevant GPOs.
5. Ensure devices are running a supported Windows version (Windows 10 version 20H2 or later, Windows 11) and have the latest quality updates installed.

## Validation
After remediation, verify compliance by checking the device status in the Microsoft 365 Defender portal under 'Device inventory' > select a device > 'Security baseline' tab. The status should show 'Compliant'.

## Rollback
If the baseline causes issues, remove the device from the Intune security baseline policy assignment. The device will revert to its previous configuration after the next policy refresh cycle (typically within 8 hours).

## References
- Microsoft Learn â€“ 'Use security baselines in Microsoft Defender for Endpoint'
- Microsoft Learn â€“ 'Manage security baselines in Microsoft Intune' (https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines)
