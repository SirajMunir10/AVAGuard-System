# Troubleshooting: Device Identity (ERROR_ADAL_PROTOCOL_NOT_SUPPORTED (0xcaa90017/-894894057))

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve configuration errors during Microsoft Entra hybrid join related to ADAL protocol and XML parsing?

## Environment Context
- **Tenant Type:** federated
- **Configuration:** On-premises identity provider, Federation Service MEX endpoint

## Symptoms
- ADAL authentication protocol not supported
- Federation Service didn't return an XML response

## Error Codes
- `ERROR_ADAL_PROTOCOL_NOT_SUPPORTED (0xcaa90017/-894894057)`
- `ERROR_ADAL_FAILED_TO_PARSE_XML (0xcaa9002c/-894894036)`

## Root Causes
1. On-premises identity provider doesn't support WS-Trust
2. Federation Service MEX endpoint not returning valid XML
3. Proxy interfering and returning non-XML responses

## Remediation Steps
1. The on-premises identity provider must support WS-Trust.
2. Ensure that the Metadata Exchange (MEX) endpoint is returning a valid XML.
3. Ensure that the proxy isn't interfering and returning non-XML responses.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
