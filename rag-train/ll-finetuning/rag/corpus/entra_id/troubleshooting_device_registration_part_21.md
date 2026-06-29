# Troubleshooting: Device Registration (0x801c0021)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose a device registration failure with DRS Discovery Test failing and error code 0x801c0021/0x801c000c?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- DRS Discovery Test : FAIL [0x801c0021/0x801c000c]
- DRS Connectivity Test : SKIPPED
- Token acquisition Test : SKIPPED
- Fallback to Sync-Join : ENABLED
- Error Phase : discover
- Client ErrorCode : 0x801c0021

## Error Codes
- `0x801c0021`
- `0x801c000c`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. Run 'dsregcmd /status' and verify that the 'Device State' section shows 'AzureAdJoined : YES' and 'DomainJoined : NO' (or appropriate state).
2. In the 'Diagnostic Data' section of dsregcmd output, confirm that 'DRS Discovery Test' shows 'PASSED' and no error codes (0x801c0021 or 0x801c000c) appear.
3. Verify that 'DRS Connectivity Test' and 'Token acquisition Test' are no longer 'SKIPPED' and show 'PASSED'.
4. Check that 'Fallback to Sync-Join' is 'DISABLED' (if not required) or correctly reflects intended configuration.
5. Confirm that the device can successfully register or re-register with Entra ID by initiating a new registration (e.g., via 'dsregcmd /join' if needed) and observing no errors.

## Rollback
1. If the remediation involved modifying DNS or network settings, restore the original DNS server addresses and network configuration.
2. If firewall or proxy changes were made, revert those rules to allow only previously permitted endpoints.
3. If the device was unjoined and rejoined, rejoin the device to the original on-premises domain (if applicable) using 'dsregcmd /leave' followed by domain join steps.
4. If registry keys were altered (e.g., under 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CDJ'), restore from backup or revert to previous values.
5. If group policy or Intune settings were changed, revert those policies to their prior state and force a policy refresh with 'gpupdate /force'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
