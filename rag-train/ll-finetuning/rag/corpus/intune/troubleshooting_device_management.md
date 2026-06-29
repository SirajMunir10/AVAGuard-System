# Troubleshooting: Device Management (-2016281112)

**Domain:** Intune
**Subdomain:** Device Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender for Endpoint onboarding issues using Microsoft Intune when policies are not propagated on devices?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Automatic MDM enrollment may need to be configured

## Symptoms
- Configured policies in Intune are not propagated on devices

## Error Codes
- `-2016281112`

## Root Causes
1. Onboarding or offboarding failed on a wrong blob: wrong signature or missing PreviousOrgIds fields
2. Microsoft Defender for Endpoint Policy registry key doesn't exist or the OMA DM client doesn't have permissions to write to it
3. An attempt to remediate by read-only property
4. Attempt to deploy Microsoft Defender for Endpoint on non-supported SKU/Platform, particularly Holographic SKU

## Remediation Steps
1. Check the event IDs in the View agent onboarding errors in the device event log section
2. Check the MDM event logs in the following table or follow the instructions in Diagnose MDM failures in Windows
3. Ensure that the following registry key exists: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection. If it doesn't exist, open an elevated command and add the key
4. Check the troubleshooting steps in Troubleshoot onboarding issues on the device
5. Download the Local script from the Device management section of the portal, and run it in an elevated command prompt

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
