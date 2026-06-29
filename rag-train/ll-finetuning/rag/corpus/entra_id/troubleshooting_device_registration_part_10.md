# Troubleshooting: Device Registration (0xcaa90023)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra hybrid join failures on Windows devices when encountering error ERROR_ADAL_COULDNOT_DISCOVER_USERNAME_PASSWORD_ENDPOINT (0xcaa90023/-894894045)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** On-premises identity provider settings, WS-Trust endpoints

## Symptoms
- Device fails to complete Microsoft Entra hybrid join
- Error code 0xcaa90023/-894894045 appears in logs

## Error Codes
- `0xcaa90023`
- `-894894045`

## Root Causes
1. WS-Trust endpoints are not enabled
2. MEX response does not contain correct endpoints

## Remediation Steps
1. Check the on-premises identity provider settings
2. Ensure that the WS-Trust endpoints are enabled
3. Ensure that the MEX response contains these correct endpoints

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
