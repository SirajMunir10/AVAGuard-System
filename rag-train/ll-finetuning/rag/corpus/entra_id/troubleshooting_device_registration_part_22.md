# Troubleshooting: Device Registration (0x801c03f2)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve a sync-join registration failure where diagnostics tests pass but registration fails with DirectoryError and error code 0x801c03f2?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- AD Connectivity Test : PASS
- AD Configuration Test : PASS
- DRS Discovery Test : PASS
- DRS Connectivity Test : PASS
- Token acquisition Test : PASS
- Fallback to Sync-Join : ENABLED
- Previous Registration : 2019-01-31 09:16:43.000 UTC
- Registration Type : sync
- Error Phase : join
- Client ErrorCode : 0x801c03f2
- Server ErrorCode : DirectoryError
- Server Message : The device object by the given id (aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb) isn't found.

## Error Codes
- `0x801c03f2`
- `DirectoryError`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. Run 'dsregcmd /status' and verify that 'AzureAdJoined' is 'YES' and 'DomainJoined' is 'YES'. 2. Confirm that the device object with ID 'aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb' exists in Entra ID by running 'Get-AzureADDevice -ObjectId aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb' (or the equivalent Microsoft Graph PowerShell command). 3. Check that the device's registration timestamp is recent and matches the expected sync cycle. 4. Re-run the diagnostics tests (AD Connectivity, AD Configuration, DRS Discovery, DRS Connectivity, Token Acquisition) and confirm all pass. 5. Verify that the 'Previous Registration' timestamp has been updated to the current time.

## Rollback
1. If the device object was deleted during remediation, re-create it in Entra ID using the original device ID 'aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb' via 'New-AzureADDevice -AccountEnabled $true -DeviceId aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb -DisplayName <originalDisplayName>'. 2. If the device was re-joined, unjoin it from Entra ID by running 'dsregcmd /leave' on the device. 3. Restore the original device registration state by re-running the sync-join process from the on-premises AD using the original device ID. 4. If any configuration changes were made (e.g., to the service connection point), revert them to the previous values. 5. Confirm that the error code 0x801c03f2 and DirectoryError no longer appear in the registration logs.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
