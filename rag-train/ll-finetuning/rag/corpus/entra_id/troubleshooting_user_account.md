# Troubleshooting: User Account (AADSTS50034)

**Domain:** Entra ID
**Subdomain:** User Account
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve AADSTS50034: The user account does not exist in the tenant directory during hybrid join?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event 1144 in Microsoft Entra analytics logs contains the UPN provided

## Error Codes
- `AADSTS50034`

## Root Causes
1. User account not found in the tenant
2. User typing incorrect UPN
3. On-premises user account not synced with Microsoft Entra ID

## Remediation Steps
1. Ensure that the user is typing the correct UPN
2. Ensure that the on-premises user account is being synced with Microsoft Entra ID

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
