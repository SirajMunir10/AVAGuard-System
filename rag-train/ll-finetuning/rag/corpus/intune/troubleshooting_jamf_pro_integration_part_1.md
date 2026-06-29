# Troubleshooting: Jamf Pro integration

**Domain:** Intune
**Subdomain:** Jamf Pro integration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve a macOS device that enrolled with Intune directly instead of through Jamf Self Service?

## Environment Context
- **Tenant Type:** Microsoft Intune with Jamf Pro integration
- **Configuration:** Jamf Pro policy for Microsoft Entra ID registration; Company Portal app deployed via Jamf Pro

## Symptoms
- User opened Company Portal manually instead of through Jamf Self Service
- Company Portal app shows 'Not registered'
- Company Portal logs contain entry: 'Not registered Line 7783: <DATE> <IP ADDRESS> INFO com.microsoft.ssp.application TID=1 WelcomeViewController.swift: 253 (startLogin()) Portal launched without WPJ only arg while account is under partner management'

## Error Codes
N/A

## Root Causes
1. User did not use Jamf Self Service to open the Intune Company Portal; device enrolled and registered without its connection to Jamf

## Remediation Steps
1. Remove the macOS device from Intune
2. On the device, use Jamf Self Service to open the Company Portal app
3. Register the device with Microsoft Entra ID through the Company Portal
4. Prerequisites: Deploy the Company Portal app for macOS in Jamf Pro and create a policy in Jamf Pro to have users register their devices with Microsoft Entra ID
5. When the portal opens, sign in with work or school account
6. Confirm account information and check Device Enrollment and Device Compliance statuses
7. Click Begin to start enrollment
8. If prompted, type in computer's sign-in information
9. Wait for registration completion message

## Validation
After following steps, device should show as registered through Jamf in Company Portal and receive notification to open Self-Service app for changes.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
