# Troubleshooting: Device Identity (DSREG_DISCOVERY_TENANT_NOT_FOUND (0x801c003a/-2145648582))

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve HTTP errors during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** federated
- **Configuration:** Service connection point object configured with tenant ID

## Symptoms
- Service connection point object configured with wrong tenant ID
- No active subscriptions found in the tenant
- HTTP 503 from DRS server

## Error Codes
- `DSREG_DISCOVERY_TENANT_NOT_FOUND (0x801c003a/-2145648582)`
- `DSREG_SERVER_BUSY (0x801c0025/-2145648603)`

## Root Causes
1. Service connection point object configured with wrong Microsoft Entra tenant ID
2. No active subscriptions in the tenant
3. DRS server temporarily unavailable

## Remediation Steps
1. Ensure that the service connection point object is configured with the correct Microsoft Entra tenant ID and active subscriptions or that the service is present in the tenant.
2. Future join attempts will likely succeed after the server is back online.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
