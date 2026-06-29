# Troubleshooting: Password Reset Writeback (ADUserNotFoundError)

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot ADUserNotFoundError event in SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback configuration

## Symptoms
- User trying to reset or change password not found in on-premises directory

## Error Codes
- `ADUserNotFoundError`

## Root Causes
1. User deleted on-premises but not in the cloud
2. Problem with sync

## Remediation Steps
1. Check sync logs and the last few sync run details for more information

## Validation
1. Open the Microsoft Entra admin center, navigate to Identity > Hybrid management > Microsoft Entra Connect > Connect Sync. 2. Select the most recent sync run and review the 'Synchronization Errors' tab for any errors related to the affected user. 3. On the on-premises server, open the Synchronization Service Manager (start → Synchronization Service). 4. Go to the 'Operations' tab and locate the last successful import and export runs. 5. For each run, click 'Connector Space' and search for the user's distinguished name or userPrincipalName. 6. Verify that the user object exists in the on-premises Active Directory connector space and that its 'objectGUID' matches the cloud user's 'ImmutableId'. 7. If the user is missing from the connector space, confirm the user is present in the on-premises AD and that the sync scope includes the user's OU.

## Rollback
1. If the user was incorrectly deleted from on-premises AD, restore the user from the Active Directory Recycle Bin (if enabled) or re-create the user object with the same attributes (especially userPrincipalName, objectGUID, and proxyAddresses). 2. If the user was accidentally excluded from sync scope, modify the Microsoft Entra Connect filtering rules to include the user's OU or group. 3. Run a full synchronization cycle: on the Microsoft Entra Connect server, open PowerShell as an administrator and execute 'Start-ADSyncSyncCycle -PolicyType Delta'. 4. After the sync completes, verify the user appears in the on-premises connector space and that no new errors are reported in the sync logs. 5. If the issue persists, consider performing a full import and full synchronization: 'Start-ADSyncSyncCycle -PolicyType Initial'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
