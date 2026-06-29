# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot hybrid-joined devices when the on-premises domain name is nonroutable (e.g., jdoe@contoso.local)?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Hybrid-joined devices with nonroutable on-premises domain name

## Symptoms
- User's UPN is in nonroutable format (e.g., jdoe@contoso.local)

## Error Codes
N/A

## Root Causes
1. On-premises domain name is nonroutable

## Remediation Steps
1. Configure Alternate Login ID (AltID). References: Prerequisites; Configure Alternate Login ID.
2. Ensure that the domain controller is configured to return the UPN in the correct format (internet-style login name based on RFC 822).
3. On the domain controller, run 'whoami /upn' to verify the configured UPN.

## Validation
Event 1144 (Microsoft Entra analytics logs) contains the UPN provided.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
