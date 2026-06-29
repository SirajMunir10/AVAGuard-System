# Troubleshooting: Hybrid Identity (WC_E_DTDPROHIBITED (-1072894385/0xc00cee4f))

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error WC_E_DTDPROHIBITED (-1072894385/0xc00cee4f) during hybrid join?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Hybrid-joined devices

## Symptoms
- XML response from the WS-Trust endpoint included a Document Type Definition (DTD)

## Error Codes
- `WC_E_DTDPROHIBITED (-1072894385/0xc00cee4f)`

## Root Causes
1. DTD is not expected in XML responses, and parsing fails if a DTD is included

## Remediation Steps
N/A

## Validation
1. Verify that the WS-Trust endpoint URL used by the device is correct and accessible: Invoke-WebRequest -Uri 'https://autologon.microsoftazuread-sso.com/wstrust/issue/usernamemixed' -Method Post -Body '<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope"><s:Header/><s:Body><wst:RequestSecurityToken xmlns:wst="http://schemas.xmlsoap.org/ws/2005/02/trust"><wst:RequestType>http://schemas.xmlsoap.org/ws/2005/02/trust/Issue</wst:RequestType><wst:AppliesTo><wsa:EndpointReference xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing"><wsa:Address>urn:federation:MicrosoftOnline</wsa:Address></wsa:EndpointReference></wst:AppliesTo></wst:RequestSecurityToken></s:Body></s:Envelope>' -ContentType 'application/soap+xml' -UseBasicParsing. 2. Confirm the response does not contain a DTD by checking the raw XML output for '<!DOCTYPE' or similar. 3. Run dsregcmd /status on the device and ensure the 'AzureAdJoined' status is 'YES' and 'DomainJoined' is 'YES'. 4. Check the Device Registration Service logs at 'Applications and Services Logs/Microsoft/Windows/User Device Registration/Admin' for error code 0xc00cee4f or related DTD errors.

## Rollback
1. If the WS-Trust endpoint was modified, restore the original endpoint URL in the device's local group policy or registry under 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CDP' (if applicable). 2. If a proxy or firewall rule was changed to allow the WS-Trust traffic, revert the rule to its previous state. 3. If the device's time or certificate was adjusted, reset the time synchronization and re-enroll the device certificate via 'certlm.msc' or 'gpupdate /force'. 4. If the device was removed from Azure AD, re-register it using 'dsregcmd /leave' followed by a reboot and automatic rejoin via scheduled task or manual 'dsregcmd /join'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
