# Troubleshooting: Device Identity (AAD_CLOUDAP_E_OAUTH_USERNAME_IS_MALFORMED (-1073445812/ 0xc004844c))

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve AAD_CLOUDAP_E_OAUTH_USERNAME_IS_MALFORMED (-1073445812/ 0xc004844c) error during hybrid join?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The user's UPN isn't in the expected format

## Error Codes
- `AAD_CLOUDAP_E_OAUTH_USERNAME_IS_MALFORMED (-1073445812/ 0xc004844c)`

## Root Causes
1. For Microsoft Entra joined devices, the UPN is the text that's entered by the user in the LoginUI
2. For Microsoft Entra hybrid joined devices, the UPN is returned from the domain controller during the login process
3. User's UPN should be in the internet-style login name, based on the internet standard RFC 822

## Remediation Steps
1. For hybrid-joined devices, ensure that the domain controller is configured to return the UPN in the correct format
2. In the domain controller, whoami /upn should display the configured UPN

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
