# Troubleshooting: Device Registration (0x801c03f2)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra hybrid join failures using Event Viewer logs and error codes?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Hybrid join configuration

## Symptoms
- Device registration fails with error phase 'join'
- Client ErrorCode: 0x801c03f2
- Server ErrorCode: DirectoryError
- Server Message: The device object by the given id (aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb) is not found. Https Status: 400

## Error Codes
- `0x801c03f2`
- `-2145647630`
- `0x801c0002`
- `-2145648638`
- `0x801c0006`
- `-2145648634`
- `0x80090016`
- `-2146893802`
- `0x80290407`
- `-2144795641`

## Root Causes
1. DSREG_E_DIRECTORY_FAILURE (0x801c03f2): Received an error response from DRS with ErrorCode: 'DirectoryError'
2. DSREG_E_DEVICE_AUTHENTICATION_ERROR (0x801c0002): Received an error response from DRS with ErrorCode: 'AuthenticationError' and ErrorSubCode is not 'DeviceNotFound'
3. DSREG_E_DEVICE_INTERNALSERVICE_ERROR (0x801c0006): Received an error response from DRS with ErrorCode: 'DirectoryError'
4. NTE_BAD_KEYSET (0x80090016): TPM operation failed or was invalid; keyset doesn't exist. This error happens when the TPM is cleared on the systems, or when there's a bad sysprep image.
5. TPM_E_PCP_INTERNAL_ERROR (0x80290407): Generic TPM error.

## Remediation Steps
1. Use Event Viewer logs to locate the phase and error code for the join failures. In Event Viewer, open the User Device Registration event logs. They're stored under Applications and Services Log > Microsoft > Windows > User Device Registration. Look for event ID 204.
2. For NTE_BAD_KEYSET: Avoid clearing the TPM in BIOS or Windows settings. If the TPM is cleared, users might need to recover by removing and readding accounts to fix the problem, especially when they have multiple WAM accounts. Ensure that the machine from which the sysprep image was created isn't Microsoft Entra joined, Microsoft Entra hybrid joined, or Microsoft Entra registered.
3. For TPM_E_PCP_INTERNAL_ERROR: Disable TPM on devices with this error. Windows 10 versions 1809 and later automatically detect TPM failures and complete Microsoft Entra hybrid join without using the TPM.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
