# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to evaluate the join status of a Windows device for Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Hybrid join configuration

## Symptoms
- Device is not joined to Microsoft Entra ID
- AzureAdJoined field value is NO

## Error Codes
N/A

## Root Causes
1. Device is not joined to on-premises Active Directory (DomainJoined is NO)
2. Device is registered with Microsoft Entra ID as a personal device (WorkplaceJoined is YES) before hybrid join completion

## Remediation Steps
1. Review the DomainJoined field: if value is NO, the device cannot do Microsoft Entra hybrid join
2. Review the WorkplaceJoined field: if value is YES, a work or school account was added before completion of hybrid join; this account is ignored when using Windows 10 version 1607 or later
3. Review the AzureAdJoined field: if value is NO, the join to Microsoft Entra ID has not finished yet; continue to next steps for further troubleshooting

## Validation
1. Open an elevated PowerShell console on the device. 2. Run: dsregcmd /status 3. Confirm that the 'AzureAdJoined' field displays 'YES'. 4. Confirm that the 'DomainJoined' field displays 'YES'. 5. Confirm that the 'WorkplaceJoined' field displays 'NO'. 6. Run: dsregcmd /status | Select-String 'AzureAdJoined' 7. Verify the output shows 'AzureAdJoined : YES'.

## Rollback
1. If the device is incorrectly joined to Microsoft Entra ID, sign in as a local administrator. 2. Open an elevated PowerShell console. 3. Run: dsregcmd /leave 4. Restart the device. 5. Re-run: dsregcmd /status 6. Confirm that 'AzureAdJoined' now displays 'NO'. 7. If the device was previously registered (WorkplaceJoined = YES), remove the work or school account via Settings > Accounts > Access work or school, select the account, and click 'Disconnect'. 8. Re-attempt the hybrid join process by ensuring the device is domain-joined and the Microsoft Entra Connect sync has completed.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
