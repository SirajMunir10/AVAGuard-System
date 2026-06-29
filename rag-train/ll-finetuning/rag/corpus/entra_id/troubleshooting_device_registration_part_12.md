# Troubleshooting: Device Registration (0xcaa82efe)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix Microsoft Entra hybrid join failure due to connection aborted error ERROR_ADAL_INTERNET_CONNECTION_ABORTED (0xcaa82efe/-894947586)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Network stability

## Symptoms
- Device fails to join Microsoft Entra hybrid
- Error code 0xcaa82efe/-894947586 appears

## Error Codes
- `0xcaa82efe`
- `-894947586`

## Root Causes
1. Connection with the authorization endpoint was aborted

## Remediation Steps
1. Retry the join after a while
2. Try joining from another stable network location

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
