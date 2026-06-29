# Hardening: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Hardening

## Scenario / Query
How to configure sample sharing settings for enhanced threat detection in Defender for Endpoint via Intune?

## Environment Context
- **Tenant Type:** Intune and Defender for Endpoint connected
- **Configuration:** Sample Sharing

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set Sample Sharing to All to enable automatic sample sharing for enhanced threat detection.
2. Set Sample Sharing to None to disable sample sharing, which can reduce detection capabilities.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Antivirus > Windows 10 and later policies. Select the policy where sample sharing was configured. Under Configuration settings, confirm that 'Microsoft Defender Antivirus: Configure sample sharing' is set to 'All' (or 'None' if disabling).
2. On a managed Windows device, open PowerShell as Administrator and run: Get-MpPreference | Select-Object SubmitSamplesConsent. Verify the output matches the configured value (1 for 'All', 0 for 'None').
3. In the Microsoft 365 Defender portal, go to Settings > Endpoints > Advanced features. Confirm that 'Sample sharing' is enabled (if set to 'All') or disabled (if set to 'None').

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Antivirus > Windows 10 and later policies. Select the policy where sample sharing was configured. Under Configuration settings, change 'Microsoft Defender Antivirus: Configure sample sharing' back to the previous value (e.g., from 'All' to 'None' or vice versa).
2. On a managed Windows device, open PowerShell as Administrator and run: Set-MpPreference -SubmitSamplesConsent <previousValue> where <previousValue> is the original consent level (0 for 'None', 1 for 'All').
3. In the Microsoft 365 Defender portal, go to Settings > Endpoints > Advanced features. Toggle 'Sample sharing' to the original state (enable or disable as needed).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
