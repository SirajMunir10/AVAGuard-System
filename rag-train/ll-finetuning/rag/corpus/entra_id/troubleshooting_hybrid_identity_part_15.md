# Troubleshooting: Hybrid Identity (AAD_CLOUDAP_E_OAUTH_USER_SID_IS_EMPTY (-1073445822/0xc0048442))

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error AAD_CLOUDAP_E_OAUTH_USER_SID_IS_EMPTY (-1073445822/0xc0048442) during hybrid join?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Hybrid-joined devices

## Symptoms
- User SID is missing in the ID token returned by the Microsoft Entra authentication service

## Error Codes
- `AAD_CLOUDAP_E_OAUTH_USER_SID_IS_EMPTY (-1073445822/0xc0048442)`

## Root Causes
1. Network proxy interfering with and modifying the server response

## Remediation Steps
1. Ensure that the network proxy isn't interfering with and modifying the server response.

## Validation
1. On a hybrid-joined device that previously experienced the error, run `dsregcmd /status` and verify that the 'AzureAdJoined' status is 'YES' and that the 'Last Error' field is empty or shows no AAD_CLOUDAP_E_OAUTH_USER_SID_IS_EMPTY error. 2. Check the Device Registration event logs (Event Viewer > Applications and Services Logs > Microsoft > Windows > DeviceRegistration) for Event ID 304 or 306 indicating successful hybrid join. 3. Confirm that the user SID is present in the ID token by reviewing the authentication logs in Entra ID under 'Sign-in logs' for a successful device authentication event. 4. Temporarily bypass the network proxy by adding the device registration endpoints (https://enterpriseregistration.windows.net, https://login.microsoftonline.com) to the proxy's allowlist or direct access list, then re-run `dsregcmd /join` and verify no recurrence of the error.

## Rollback
1. If the remediation (bypassing proxy inspection) causes connectivity issues for other services, remove the proxy bypass entries for the device registration endpoints and restore the original proxy configuration. 2. Re-enable any proxy inspection or modification rules that were disabled for the device registration traffic. 3. On the affected device, run `dsregcmd /leave` to unjoin from Entra ID, then run `dsregcmd /join` to re-attempt hybrid join under the restored proxy settings. 4. If the error persists after rollback, verify that the proxy is not modifying the server response by reviewing proxy logs for any manipulation of the 'user_sid' claim in the ID token.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
