# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
Unable to sign in or enroll devices when you have multiple verified domains

## Environment Context
- **Tenant Type:** Microsoft 365 with AD FS 2.0
- **Configuration:** Multiple verified domains with different UPN suffixes (e.g., @contoso.com, @fabrikam.com) and single sign-on through AD FS 2.0

## Symptoms
- Users with the UPN suffix of the second domain may not be able to log into the portals
- Users with the UPN suffix of the second domain may not be able to enroll devices

## Error Codes
N/A

## Root Causes
1. Adding a second verified domain to AD FS without proper configuration for multiple UPN suffixes

## Remediation Steps
1. Deploy a separate instance of the AD FS 2.0 Federation Service for each suffix if using SSO through AD FS 2.0 and having multiple top-level domains for users' UPN suffixes
2. Alternatively, use a rollup for AD FS 2.0 in conjunction with the SupportMultipleDomain switch to enable the AD FS server to support this scenario without requiring additional AD FS 2.0 servers

## Validation
1. Verify that each UPN suffix (e.g., @contoso.com, @fabrikam.com) has a corresponding AD FS 2.0 instance or that the SupportMultipleDomain switch is enabled. Run: Get-ADFSProperties | Select-Object SupportMultipleDomain. If the value is False and you have not deployed separate instances, proceed with rollup configuration. 2. Test sign-in for a user with the second domain UPN suffix (e.g., user@fabrikam.com) at https://portal.office.com. Confirm successful authentication without errors. 3. Attempt device enrollment for a user with the second domain UPN suffix using a supported device (e.g., Windows 10). Ensure enrollment completes without error messages related to domain or federation.

## Rollback
1. If a separate AD FS 2.0 instance was deployed, remove the additional instance by running: Remove-ADFSFarmNode -ServiceAccountCredential (Get-Credential) on the secondary server, then uninstall the AD FS role. 2. If the SupportMultipleDomain switch was enabled, disable it by running: Set-ADFSProperties -SupportMultipleDomain $false. 3. Restore the original AD FS configuration from backup if available, or reconfigure AD FS to support only the primary domain (e.g., @contoso.com). 4. Verify that users with the second domain UPN suffix can no longer sign in or enroll, confirming rollback to the original state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
