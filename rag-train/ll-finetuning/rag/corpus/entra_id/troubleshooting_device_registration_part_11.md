# Troubleshooting: Device Registration (0xcaa82ee2)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Entra hybrid join failures caused by network timeout error ERROR_ADAL_INTERNET_TIMEOUT (0xcaa82ee2/-894947614)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Network connectivity, system context access

## Symptoms
- Device fails to join Microsoft Entra hybrid
- Error code 0xcaa82ee2/-894947614 appears

## Error Codes
- `0xcaa82ee2`
- `-894947614`

## Root Causes
1. General network timeout
2. https://login.microsoftonline.com is not accessible in the system context
3. On-premises identity provider is not accessible in the system context

## Remediation Steps
1. Ensure that https://login.microsoftonline.com is accessible in the system context
2. Ensure that the on-premises identity provider is accessible in the system context
3. For more information, see Network connectivity requirements

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
