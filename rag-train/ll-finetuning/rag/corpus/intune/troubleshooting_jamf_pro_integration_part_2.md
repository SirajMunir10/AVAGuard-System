# Troubleshooting: Jamf Pro Integration

**Domain:** Intune
**Subdomain:** Jamf Pro Integration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Jamf-Intune integration issues by collecting basic information and verifying prerequisites?

## Environment Context
- **Tenant Type:** Microsoft Intune and Microsoft Entra ID P1 licenses required
- **Configuration:** Jamf Pro integration with Intune

## Symptoms
- Jamf-Intune integration-related issue encountered

## Error Codes
N/A

## Root Causes
1. Prerequisites not met

## Remediation Steps
1. Review the prerequisites from the following articles, depending on how you configure Jamf Pro integration with Intune: Use the Jamf Cloud Connector to integrate Jamf Pro with Intune; Integrate Jamf Pro with Intune
2. Ensure all users have Microsoft Intune and Microsoft Entra ID P1 licenses
3. Ensure you have a user account that has Microsoft Intune Integration permissions in the Jamf Pro console
4. Ensure you have a user account that has Global Admin permissions in Azure
5. Collect the following information when investigating Jamf Pro integration with Intune: Exact error message(s); Location of the error message(s); When the problem started, and whether your Jamf Pro integration with Intune worked previously; How many users are affected (all users or just some); How many devices are affected (all devices or just some)

## Validation
1. Verify that all users have Microsoft Intune and Microsoft Entra ID P1 licenses assigned by running: Get-MgUser -All | Where-Object { $_.AssignedLicenses -match 'Intune' -and $_.AssignedLicenses -match 'AAD_P1' } | Select-Object DisplayName, UserPrincipalName. 2. Confirm the Jamf Pro user account has Microsoft Intune Integration permissions by checking the Jamf Pro console under Settings > System > Microsoft Intune Integration. 3. Confirm the Azure user account has Global Admin permissions by running: Get-MgDirectoryRole -Filter 'displayName eq Global Administrator' | Get-MgDirectoryRoleMember | Select-Object DisplayName, Id. 4. Collect the exact error message(s), location, start time, previous working status, and scope of affected users/devices as per the troubleshooting guide.

## Rollback
1. If license assignment caused issues, remove the Intune or Entra ID P1 license from affected users by running: Set-MgUserLicense -UserId <UserId> -RemoveLicenses @('<SkuId>'). 2. If Jamf Pro permissions were changed, revert the Microsoft Intune Integration permissions to the previous state in the Jamf Pro console under Settings > System > Microsoft Intune Integration. 3. If Azure Global Admin permissions were modified, remove the Global Admin role from the user by running: Remove-MgDirectoryRoleMember -DirectoryRoleId <RoleId> -DirectoryObjectId <UserId>. 4. If information collection steps caused configuration changes, restore any modified settings from backup or previous known-good state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
