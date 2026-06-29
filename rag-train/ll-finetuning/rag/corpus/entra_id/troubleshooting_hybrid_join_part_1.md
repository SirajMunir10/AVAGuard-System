# Troubleshooting: Hybrid Join (AADSTS90002)

**Domain:** Entra ID
**Subdomain:** Hybrid Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve sync-join server error AADSTS90002: Tenant UUID not found?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** N/A

## Symptoms
- DirectoryError AADSTS90002: Tenant UUID not found

## Error Codes
- `AADSTS90002`

## Root Causes
1. There are no active subscriptions for the tenant
2. The tenant ID in the service connection point object is incorrect

## Remediation Steps
1. Check with your subscription administrator
2. Ensure that the service connection point object is configured with the correct Microsoft Entra tenant ID and active subscriptions or that the service is present in the tenant

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
