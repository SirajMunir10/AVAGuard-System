# Troubleshooting: Password Reset

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve connectivity issues with Microsoft Entra Connect Sync service for SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect Sync service running on a server

## Symptoms
- Connectivity issues with Microsoft Entra Connect Sync service
- Transient problems with the service

## Error Codes
N/A

## Root Causes
1. Connectivity issues or other transient problems with the Microsoft Entra Connect Sync service

## Remediation Steps
1. As an administrator on the server that runs Microsoft Entra Connect, select Start.
2. Enter services.msc in the search field and select Enter.
3. Look for the Azure AD Sync entry.
4. Right-click the service entry, select Restart, and wait for the operation to finish.

## Validation
These steps re-establish your connection with Microsoft Entra ID and should resolve your connectivity issues.

## Rollback
If restarting the Microsoft Entra Connect Sync service doesn't resolve your problem, try to disable and then re-enable the password writeback feature.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
