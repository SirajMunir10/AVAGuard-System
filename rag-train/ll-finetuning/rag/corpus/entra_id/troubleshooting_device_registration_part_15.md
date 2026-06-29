# Troubleshooting: Device Registration (0xcaa90014)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix Microsoft Entra hybrid join failure due to WS-Trust fault error ERROR_ADAL_WSTRUST_REQUEST_SECURITYTOKEN_FAILED (0xcaa90014/-894894060)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Federation Server settings

## Symptoms
- Device fails to join Microsoft Entra hybrid
- Error code 0xcaa90014/-894894060 appears

## Error Codes
- `0xcaa90014`
- `-894894060`

## Root Causes
1. The Server WS-Trust response reported a fault exception, and it failed to get assertion

## Remediation Steps
1. Check the Federation Server settings
2. Look for the server error code in the authentication logs

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
