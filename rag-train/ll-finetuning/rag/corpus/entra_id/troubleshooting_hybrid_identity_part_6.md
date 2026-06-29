# Troubleshooting: Hybrid Identity (AAD_CLOUDAP_E_HTTP_PASSWORD_URI_IS_EMPTY (-1073445749/0xc004848b))

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error AAD_CLOUDAP_E_HTTP_PASSWORD_URI_IS_EMPTY (-1073445749/0xc004848b) during hybrid join?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Hybrid-joined devices

## Symptoms
- MEX endpoint is incorrectly configured; MEX response doesn't contain any password URLs

## Error Codes
- `AAD_CLOUDAP_E_HTTP_PASSWORD_URI_IS_EMPTY (-1073445749/0xc004848b)`

## Root Causes
1. Network proxy interfering with and modifying the server response
2. MEX configuration is incorrect

## Remediation Steps
1. Ensure that the network proxy isn't interfering with and modifying the server response.
2. Fix the MEX configuration to return valid URLs in response.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
