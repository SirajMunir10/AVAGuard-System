# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to retrieve the join status of a Windows device for hybrid Azure AD join troubleshooting?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Windows device joined to on-premises AD and Azure AD

## Symptoms
- Device state shows AzureAdJoined: YES or NO
- KeySignTest requires elevated run

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open a Command Prompt window as an administrator.
2. Type dsregcmd /status.

## Validation
Run dsregcmd /status and verify the Device State section shows AzureAdJoined: YES and other relevant fields.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
