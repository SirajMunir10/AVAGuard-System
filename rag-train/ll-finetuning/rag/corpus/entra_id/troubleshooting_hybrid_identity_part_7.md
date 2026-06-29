# Troubleshooting: Hybrid Identity (AAD_CLOUDAP_E_HTTP_CERTIFICATE_URI_IS_EMPTY (-1073445748/0xc004848C))

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error AAD_CLOUDAP_E_HTTP_CERTIFICATE_URI_IS_EMPTY (-1073445748/0xc004848C) during hybrid join?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Hybrid-joined devices

## Symptoms
- MEX endpoint is incorrectly configured; MEX response doesn't contain any certificate endpoint URLs

## Error Codes
- `AAD_CLOUDAP_E_HTTP_CERTIFICATE_URI_IS_EMPTY (-1073445748/0xc004848C)`

## Root Causes
1. Network proxy interfering with and modifying the server response
2. MEX configuration in the identity provider is incorrect

## Remediation Steps
1. Ensure that the network proxy isn't interfering with and modifying the server response.
2. Fix the MEX configuration in the identity provider to return valid certificate URLs in response.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
