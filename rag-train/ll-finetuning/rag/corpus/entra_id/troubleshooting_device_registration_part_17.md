# Troubleshooting: Device Registration (STATUS_LOGON_FAILURE (-1073741715/ 0xc000006d))

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra hybrid join failures on Windows current devices when encountering STATUS_LOGON_FAILURE (-1073741715/0xc000006d) or STATUS_WRONG_PASSWORD (-1073741718/0xc000006a)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Federated authentication with WS-Trust endpoint

## Symptoms
- Device unable to connect to Microsoft Entra authentication service
- Received an error response (HTTP 400) from the Microsoft Entra authentication service or WS-Trust endpoint

## Error Codes
- `STATUS_LOGON_FAILURE (-1073741715/ 0xc000006d)`
- `STATUS_WRONG_PASSWORD (-1073741718/ 0xc000006a)`

## Root Causes
1. Device unable to connect to the Microsoft Entra authentication service
2. On-premises environment requires an outbound proxy and the computer account of the device cannot discover and silently authenticate to the outbound proxy

## Remediation Steps
1. Ensure that the computer account of the device can discover and silently authenticate to the outbound proxy if the on-premises environment requires an outbound proxy
2. Check Events 1081 and 1088 (Microsoft Entra operational logs) for server error code for errors originating from the Microsoft Entra authentication service and error description for errors originating from the WS-Trust endpoint
3. Check the first instance of event 1022 (Microsoft Entra analytics logs), preceding events 1081 or 1088, for the URL that's being accessed

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
