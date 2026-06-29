# Troubleshooting: Hybrid Azure AD Join

**Domain:** Entra ID
**Subdomain:** Hybrid Azure AD Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot a Windows device that fails to complete Hybrid Azure AD Join?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Hybrid Azure AD Join with Windows current devices

## Symptoms
- Device shows as not joined to Azure AD despite being domain-joined
- User state shows WorkplaceJoined: NO
- AzureAdPrt: NO

## Error Codes
N/A

## Root Causes
1. Device registration failed during the join process
2. Connectivity issues to Azure AD endpoints
3. Misconfigured service connection points
4. User does not have sufficient permissions

## Remediation Steps
1. Verify the device can reach the following endpoints: login.windows.net, login.microsoftonline.com, enterpriseregistration.windows.net, enrollment.manage-beta.microsoft.com
2. Check the device registration status using dsregcmd /status
3. Ensure the device is domain-joined (DomainJoined: YES)
4. Verify Azure AD PRT status (AzureAdPrt: YES)
5. Review the output of dsregcmd /status for the following sections: Device State, User State, and SSO State

## Validation
Run dsregcmd /status and confirm DomainJoined: YES, WorkplaceJoined: YES, AzureAdPrt: YES

## Rollback
Disjoin the device from Azure AD using dsregcmd /leave

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
