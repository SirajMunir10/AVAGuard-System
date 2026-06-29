# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify the registration status of a Microsoft Entra hybrid join on a legacy Windows device?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Hybrid join configuration for legacy Windows devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign on with the user account that performed the Microsoft Entra hybrid join.
2. Open the command prompt.
3. Type "%programFiles%\Microsoft Workplace Join\autoworkplace.exe" /i

## Validation
1. Sign in with the user account that performed the Microsoft Entra hybrid join.
2. Open a command prompt as an administrator.
3. Run the command: "%programFiles%\Microsoft Workplace Join\autoworkplace.exe" /i
4. Verify that the output shows a successful registration status, such as 'Joined to Azure AD' or 'Device is already joined'.
5. Optionally, check the device registration in the Microsoft Entra admin center by navigating to Identity > Devices > All devices and confirming the device appears with a 'Hybrid Azure AD joined' status.

## Rollback
1. Sign in with a local administrator account on the legacy Windows device.
2. Open a command prompt as an administrator.
3. Run the command: "%programFiles%\Microsoft Workplace Join\autoworkplace.exe" /leave
4. Confirm the device is unjoined by checking that the output indicates successful removal from Azure AD.
5. Verify in the Microsoft Entra admin center (Identity > Devices > All devices) that the device no longer appears or shows a 'Pending' or 'Unjoined' status.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-legacy>
