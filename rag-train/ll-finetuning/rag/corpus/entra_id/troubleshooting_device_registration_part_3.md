# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to check the user state of a device using dsregcmd /status to verify Windows Hello key, Workplace Join, and WAM default settings?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Device registration status

## Symptoms
- NgcSet state is not YES when a Windows Hello key is expected
- NgcKeyId is missing or empty
- CanReset shows Unknown
- WorkplaceJoined state is not YES
- WamDefaultSet shows an error when run from elevated command prompt
- WamDefaultAuthority is not set to organizations
- WamDefaultId is not https://login.microsoft.com
- WamDefaultGUID is missing or incorrect

## Error Codes
N/A

## Root Causes
1. dsregcmd /status run from an elevated command prompt causing WamDefaultSet to display an error
2. Windows Hello key not set for the current logged-in user
3. Microsoft Entra registered accounts not added to the device in the current NTUSER context
4. Web Account Manager (WAM) default WebAccount not created for the logged-in user

## Remediation Steps
1. Run dsregcmd /status in a user context (not elevated) to retrieve valid status for WamDefaultSet
2. Set a Windows Hello key for the current logged-in user to change NgcSet to YES
3. Add Microsoft Entra registered accounts to the device in the current NTUSER context to set WorkplaceJoined to YES
4. Create a WAM default WebAccount for the logged-in user to set WamDefaultSet to YES

## Validation
Run dsregcmd /status and verify NgcSet is YES, NgcKeyId is present, CanReset is not Unknown, WorkplaceJoined is YES, WamDefaultSet is YES (without error), WamDefaultAuthority is organizations, WamDefaultId is https://login.microsoft.com, and WamDefaultGUID is correct

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
