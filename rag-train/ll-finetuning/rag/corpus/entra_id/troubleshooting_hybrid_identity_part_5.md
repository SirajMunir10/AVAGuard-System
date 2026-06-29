# Troubleshooting: Hybrid Identity (AAD_CLOUDAP_E_WSTRUST_SAML_TOKENS_ARE_EMPTY (--1073445695/0xc00484c1))

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error AAD_CLOUDAP_E_WSTRUST_SAML_TOKENS_ARE_EMPTY (--1073445695/0xc00484c1) during hybrid join?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Hybrid-joined devices with federated authentication

## Symptoms
- Received an error from the WS-Trust endpoint

## Error Codes
- `AAD_CLOUDAP_E_WSTRUST_SAML_TOKENS_ARE_EMPTY (--1073445695/0xc00484c1)`

## Root Causes
1. Network proxy interfering with and modifying the WS-Trust response

## Remediation Steps
1. Ensure that the network proxy isn't interfering with and modifying the WS-Trust response.
2. Check Event 1088 (Microsoft Entra operational logs) for the server error code and error description from the WS-Trust endpoint.
3. Refer to common server error codes and their resolutions listed in the next section of the documentation.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
