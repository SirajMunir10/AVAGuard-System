# Troubleshooting: Hybrid Join (0x80090031)

**Domain:** Entra ID
**Subdomain:** Hybrid Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve NTE_AUTHENTICATION_IGNORED (0x80090031/-2146893775) error during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** N/A

## Symptoms
- NTE_AUTHENTICATION_IGNORED (0x80090031/-2146893775) error

## Error Codes
- `0x80090031`
- `-2146893775`

## Root Causes
1. TPM is locked out

## Remediation Steps
1. Wait for the cool-down period. The join attempt should succeed after a while.

## Validation
1. After waiting the cool-down period (typically 1-2 hours), attempt the hybrid join again using the command: dsregcmd /join. 2. Verify the join status by running: dsregcmd /status. Confirm that 'AzureAdJoined' is set to 'YES' and 'DomainJoined' is 'YES'. 3. Check the Device Registration event logs (Event Viewer > Applications and Services Logs > Microsoft > Windows > DeviceRegistration) for successful join events (Event ID 304 or similar). 4. Validate that the device appears in the Microsoft Entra admin center under Identity > Devices > All devices.

## Rollback
1. If the join fails again with the same error, verify the TPM lockout state by running: Get-Tpm | Select-Object IsLocked. If IsLocked is True, wait longer (up to 24 hours) and retry. 2. If the issue persists, reset the TPM lockout by running: Clear-Tpm (requires local admin and may reboot). 3. After reset, reattempt the hybrid join: dsregcmd /join. 4. If the device was previously joined and needs to be removed, unjoin from Entra ID using: dsregcmd /leave, then rejoin.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
