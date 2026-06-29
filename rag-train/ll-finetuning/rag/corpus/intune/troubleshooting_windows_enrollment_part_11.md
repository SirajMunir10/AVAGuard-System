# Troubleshooting: Windows Enrollment (80180026)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Windows 10 enrollment error 80180026 when MDM automatic enrollment is enabled and Intune PC agent is installed?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with Intune
- **Configuration:** MDM automatic enrollment enabled in Azure; Intune PC software client (Intune PC agent) installed on Windows 10 computer

## Symptoms
- Error message: 'Something went wrong. Confirm you are using the correct sign-in information and that your organization uses this feature. You can try to do this again or contact your system administrator with the error code 80180026.'

## Error Codes
- `80180026`

## Root Causes
1. MDM automatic enrollment is enabled in Azure and the Intune PC software client (Intune PC agent) is installed on the Windows 10 computer

## Remediation Steps
1. Use one of the following methods to address this issue: [No specific steps provided in excerpt]

## Validation
1. Verify that the Intune PC agent is uninstalled: Open 'Programs and Features' (appwiz.cpl) and confirm 'Microsoft Intune PC Agent' is not listed. 2. Confirm MDM automatic enrollment is enabled: In Azure portal, navigate to 'Microsoft Entra ID' > 'Mobility (MDM and MAM)' > 'Microsoft Intune', and verify 'MDM user scope' is set to 'All' or 'Some'. 3. Attempt enrollment again: On the Windows 10 device, go to 'Settings' > 'Accounts' > 'Access work or school' > 'Connect' and sign in with the user's credentials. Ensure no error 80180026 appears.

## Rollback
1. Reinstall the Intune PC agent: Download the Intune PC software client from the Microsoft Intune admin center (https://admin.microsoft.com) under 'Device enrollment' > 'Windows enrollment' > 'Intune PC agent'. Run the installer on the affected Windows 10 computer. 2. If MDM automatic enrollment was disabled, re-enable it: In Azure portal, go to 'Microsoft Entra ID' > 'Mobility (MDM and MAM)' > 'Microsoft Intune', set 'MDM user scope' back to its original value (e.g., 'All' or 'Some'). 3. Verify the device is back to its previous state: Check that the device appears in the Intune console under 'Devices' > 'All devices' with the expected management type (e.g., 'Intune PC agent').

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
