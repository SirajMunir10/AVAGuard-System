# Troubleshooting: Device Registration (0xcaa20003)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Entra hybrid join failure due to invalid SAML token error ERROR_ADAL_SERVER_ERROR_INVALID_GRANT (0xcaa20003/-895352829)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Federation Server settings

## Symptoms
- Device fails to join Microsoft Entra hybrid
- Error code 0xcaa20003/-895352829 appears

## Error Codes
- `0xcaa20003`
- `-895352829`

## Root Causes
1. The SAML token from the on-premises identity provider wasn't accepted by Microsoft Entra ID

## Remediation Steps
1. Check the Federation Server settings
2. Look for the server error code in the authentication logs

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
