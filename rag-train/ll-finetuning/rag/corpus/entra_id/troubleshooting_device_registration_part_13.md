# Troubleshooting: Device Registration (0xcaa82f8f)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Entra hybrid join failure due to TLS certificate validation error ERROR_ADAL_INTERNET_SECURE_FAILURE (0xcaa82f8f/-894947441)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Client time skew, TLS/SSL certificates

## Symptoms
- Device fails to join Microsoft Entra hybrid
- Error code 0xcaa82f8f/-894947441 appears

## Error Codes
- `0xcaa82f8f`
- `-894947441`

## Root Causes
1. The Transport Layer Security (TLS) certificate (previously known as the Secure Sockets Layer [SSL] certificate) sent by the server couldn't be validated

## Remediation Steps
1. Check the client time skew
2. Retry the join after a while
3. Try joining from another stable network location

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
