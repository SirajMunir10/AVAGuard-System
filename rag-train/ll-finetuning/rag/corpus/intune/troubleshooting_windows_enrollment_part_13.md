# Troubleshooting: Windows Enrollment

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve a setup failure during bulk enrollment where Microsoft Entra user accounts in the provisioning package are not allowed to join devices to Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Device Settings > Users may join devices to Microsoft Entra ID

## Symptoms
- A setup failure has occurred during bulk enrollment

## Error Codes
N/A

## Root Causes
1. The Microsoft Entra user accounts in the account package (Package_GUID) for the respective provisioning package aren't allowed to join devices to Microsoft Entra ID

## Remediation Steps
1. Sign in to the Azure portal as administrator
2. Go to Microsoft Entra ID > Devices > Device Settings
3. Set Users may join devices to Microsoft Entra ID to All or Selected
4. If you choose Selected, click Selected, and then click Add Members to add all users who can join their devices to Microsoft Entra ID
5. Make sure that all Microsoft Entra accounts for the provisioning package are added

## Validation
1. Sign in to the Azure portal as an administrator.
2. Navigate to Microsoft Entra ID > Devices > Device Settings.
3. Verify that 'Users may join devices to Microsoft Entra ID' is set to 'All' or 'Selected'.
4. If set to 'Selected', click 'Selected' and then click 'Add Members' to confirm that all Microsoft Entra accounts from the provisioning package (Package_GUID) are listed.
5. Attempt a bulk enrollment using the provisioning package and confirm no setup failure occurs.

## Rollback
1. Sign in to the Azure portal as an administrator.
2. Navigate to Microsoft Entra ID > Devices > Device Settings.
3. If 'Users may join devices to Microsoft Entra ID' was changed from a previous setting, revert it to the original value (e.g., 'None' or remove specific users).
4. If specific users were added, click 'Selected', then 'Add Members', and remove the users that were added for the provisioning package.
5. Verify that the device settings are restored to the previous state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
