# Troubleshooting: Device Registration (STATUS_REQUEST_NOT_ACCEPTED (-1073741616/ 0xc00000d0))

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra hybrid join failures on Windows current devices when encountering STATUS_REQUEST_NOT_ACCEPTED (-1073741616/0xc00000d0)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Federated authentication with WS-Trust endpoint

## Symptoms
- Received an error response (HTTP 400) from the Microsoft Entra authentication service or WS-Trust endpoint

## Error Codes
- `STATUS_REQUEST_NOT_ACCEPTED (-1073741616/ 0xc00000d0)`

## Root Causes
1. Device unable to connect to the Microsoft Entra authentication service

## Remediation Steps
1. Check Events 1081 and 1088 (Microsoft Entra operational logs) for server error code and error description for errors originating from Microsoft Entra authentication service and WS-Trust endpoint, respectively
2. Check the first instance of event 1022 (Microsoft Entra analytics logs), preceding events 1081 or 1088, for the URL that's being accessed

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
