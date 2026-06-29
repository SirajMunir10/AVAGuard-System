# Troubleshooting: Hybrid Join (0x80072efe)

**Domain:** Entra ID
**Subdomain:** Hybrid Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve WININET_E_CONNECTION_ABORTED (0x80072efe/-2147012866) error during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** N/A

## Symptoms
- WININET_E_CONNECTION_ABORTED (0x80072efe/-2147012866) error

## Error Codes
- `0x80072efe`
- `-2147012866`

## Root Causes
1. The connection with the server was terminated abnormally

## Remediation Steps
1. Retry the join after a while, or try joining from another stable network location

## Validation
1. On the affected device, open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > User Device Registration > Admin. Verify that no new WININET_E_CONNECTION_ABORTED (0x80072efe) errors appear. 2. Run 'dsregcmd /status' from an elevated command prompt and confirm that 'AzureAdJoined' is 'YES' and 'DomainJoined' is 'YES'. 3. Check the device in the Microsoft Entra admin center (https://entra.microsoft.com) under Identity > Devices > All devices; confirm the device is listed with a 'Hybrid Azure AD joined' state.

## Rollback
1. If the remediation fails, ensure the device is on a stable network with access to the required endpoints (e.g., https://device.login.microsoftonline.com). 2. Retry the hybrid join process by running 'dsregcmd /join' from an elevated command prompt. 3. If issues persist, temporarily move the device to a different network location (e.g., corporate wired connection) and retry the join. 4. As a last resort, unjoin the device from Microsoft Entra by running 'dsregcmd /leave' and then reattempt the hybrid join.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
