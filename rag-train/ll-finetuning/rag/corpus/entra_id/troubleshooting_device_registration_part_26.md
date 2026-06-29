# Troubleshooting: Device Registration (0xcaa82efd)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix Microsoft Entra hybrid join failure due to connection failure error ERROR_ADAL_INTERNET_CANNOT_CONNECT (0xcaa82efd/-894947587)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Network connectivity to login.microsoftonline.com

## Symptoms
- Device fails to join Microsoft Entra hybrid
- Error code 0xcaa82efd/-894947587 appears

## Error Codes
- `0xcaa82efd`
- `-894947587`

## Root Causes
1. The attempt to connect to https://login.microsoftonline.com failed

## Remediation Steps
1. Check the network connection to https://login.microsoftonline.com

## Validation
1. From the affected device, run: Test-NetConnection login.microsoftonline.com -Port 443. Ensure the result shows TcpTestSucceeded: True.
2. Open a browser on the device and navigate to https://login.microsoftonline.com. Confirm the page loads without certificate or connectivity errors.
3. Run dsregcmd /status and verify that the 'AzureAdJoined' field shows 'YES' and 'DomainJoined' shows 'YES'.
4. Check the device registration status in the Microsoft Entra admin center under Devices > All devices. Confirm the device appears as 'Hybrid Azure AD joined'.

## Rollback
1. If the device was manually unjoined or reconfigured, rejoin it to the on-premises Active Directory domain: Ensure the computer object exists in AD and the device is domain-joined.
2. If network changes were made (e.g., proxy or firewall rules), revert those changes to the previous configuration.
3. On the device, run dsregcmd /leave to remove any partial Entra registration, then reboot and allow the scheduled task to reattempt hybrid join.
4. If the device was removed from Entra ID, re-register it by running dsregcmd /join from an elevated command prompt.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
