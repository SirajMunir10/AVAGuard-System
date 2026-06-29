# Troubleshooting: Device Identity (WININET_E_CANNOT_CONNECT (0x80072efd/-2147012867))

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot network errors during Microsoft Entra hybrid join on Windows 10/11?

## Environment Context
- **Tenant Type:** federated
- **Configuration:** Windows 10/11 devices, on-premises outbound proxy

## Symptoms
- Connection with the server couldn't be established
- General network timeout
- Network stack unable to decode the response from the server

## Error Codes
- `WININET_E_CANNOT_CONNECT (0x80072efd/-2147012867)`
- `WININET_E_TIMEOUT (0x80072ee2/-2147012894)`
- `WININET_E_DECODING_FAILED (0x80072f8f/-2147012721)`

## Root Causes
1. Network connectivity to required Microsoft resources is missing
2. Network proxy interfering and modifying server response

## Remediation Steps
1. Ensure network connectivity to the required Microsoft resources. For more information, see Network connectivity requirements.
2. Ensure that the network proxy isn't interfering and modifying the server response.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
