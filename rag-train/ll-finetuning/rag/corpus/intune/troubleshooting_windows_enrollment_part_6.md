# Troubleshooting: Windows Enrollment (0x8018002b)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Auto MDM Enroll: Failed error 0x8018002b when enrolling a Windows 10 device automatically via Group Policy?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Auto MDM enrollment via Group Policy

## Symptoms
- In Task Scheduler, under Microsoft > Windows > EnterpriseMgmt, the last run result of the Schedule created by enrollment client for automatically enrolling in MDM from Microsoft Entra ID task is: Event 76 Auto MDM Enroll: Failed (Unknown Win32 Error code: 0x8018002b)
- In Event Viewer, under Applications and Services Logs/Microsoft/Windows/DeviceManagement-Enterprise-Diagnostics-Provider/Admin, Event ID 76 is logged with Level: Error and Description: Auto MDM Enroll: Failed (Unknown Win32 Error code: 0x80180002b)

## Error Codes
- `0x8018002b`
- `0x80180002b`
- `Event ID 76`

## Root Causes
1. The UPN contains an unverified or non-routable domain, such as .local (like joe@contoso.local)
2. MDM user scope is set to None

## Remediation Steps
1. On the server that Active Directory Domain Services (AD DS) runs on, open Active Directory Users and Computers by typing dsa.msc in the Run dialog, and then click OK.
2. Click Users under your domain, and then follow these steps: If there's only one affected user, right-click the user, and then click Properties. On the Account tab, in the UPN suffix drop-down list under User logon name, select a valid UPN suffix such as contoso.com, and then click OK.
3. If there are multiple affected users, select the users, in the Action menu, click Properties. On the Account tab, select the UPN suffix check box, select a valid UPN suffix such as contoso.com in the drop-down list, and then click OK.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
