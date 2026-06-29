# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose device key health and recovery status using dsregcmd post-join diagnostics?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Device joined to cloud

## Symptoms
- AadRecoveryEnabled value is YES
- KeySignTest value is FAILED

## Error Codes
N/A

## Root Causes
1. Keys stored in the device are not usable
2. Device keys are in poor health

## Remediation Steps
1. If AadRecoveryEnabled is YES, the device is marked for recovery; the next sign-in will trigger the recovery flow and re-register the device.
2. If KeySignTest fails, the device is usually marked for recovery; the next sign-in will trigger the recovery flow and re-register the device.
3. For Microsoft Entra hybrid joined devices, the recovery is silent.
4. For Microsoft Entra joined or Microsoft Entra registered devices, user authentication is prompted to recover and re-register the device, if necessary.

## Validation
Run 'dsregcmd /status' on the device. Verify that 'AadRecoveryEnabled' is NO and 'KeySignTest' is PASSED. Confirm that the device state shows 'AzureAdJoined : YES' and 'DomainJoined : YES' (if hybrid) or 'AzureAdJoined : YES' (if cloud-joined). Check that 'Last ErrorCode' is 0 and 'Last ErrorTime' is empty or recent. For hybrid joined devices, ensure no user authentication prompt appears; for Entra joined/registered devices, confirm that a user sign-in successfully completed the recovery flow.

## Rollback
If the remediation fails or causes issues, run 'dsregcmd /leave' to unjoin the device from Entra ID. Then rejoin the device using 'dsregcmd /join' (for Entra joined) or ensure the device reconnects to on-premises AD and syncs to Entra ID (for hybrid joined). Alternatively, if the device is in a broken state, perform a manual device reset via the Entra admin center: navigate to Identity > Devices > All devices, select the device, and choose 'Delete' to remove it, then rejoin the device from the client.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
