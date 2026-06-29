# Troubleshooting: Device Registration (0xcaa90006)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Entra hybrid join failure due to token request error ERROR_ADAL_WSTRUST_TOKEN_REQUEST_FAIL (0xcaa90006/-894894074)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Token endpoint

## Symptoms
- Device fails to join Microsoft Entra hybrid
- Error code 0xcaa90006/-894894074 appears

## Error Codes
- `0xcaa90006`
- `-894894074`

## Root Causes
1. Received an error when trying to get access token from the token endpoint

## Remediation Steps
1. Look for the underlying error in the ADAL log

## Validation
1. Check the ADAL log for the underlying error: Open the ADAL log file (typically located at %LOCALAPPDATA%\Temp\ADAL.log) and search for entries containing 'ERROR_ADAL_WSTRUST_TOKEN_REQUEST_FAIL' or error code '0xcaa90006'. 2. Verify that the device can successfully obtain a token by running the dsregcmd /status command and confirming that the 'AzureAdJoined' status is 'YES' and the 'DomainJoined' status is 'YES'. 3. Confirm that the device is listed in the Microsoft Entra admin center under 'Devices' > 'All devices' with a status of 'Hybrid Azure AD joined'.

## Rollback
1. If the remediation fails, revert any changes made to the token endpoint configuration by restoring the original settings from backup or documentation. 2. If the underlying error indicates a misconfiguration in the service connection point (SCP), use the dsregcmd /leave command to remove the device from Microsoft Entra, then re-run the hybrid join process after correcting the SCP settings. 3. If the issue persists, disable and re-enable the device registration in the Microsoft Entra admin center under 'Devices' > 'Device settings' > 'Maximum number of devices per user' and then re-attempt the join.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
