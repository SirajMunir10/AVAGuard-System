# Implementation: Endpoint Device Management

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Device Management
**Incident Type:** Implementation

## Scenario / Query
How to offboard devices from Microsoft Defender for Endpoint using Group Policy?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Group Policy deployment method

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Get the offboarding package from the Microsoft Defender portal: In the navigation pane, select System > Settings > Endpoints > Device management > Offboarding.
2. Select the operating system.
3. In the Deployment method field, select Group policy.
4. Click Download package and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the device. You should have a file named WindowsDefenderATPOffboardingScript_valid_until_YYYY-MM-DD.cmd.
6. Open the Group Policy Management Console (GPMC), right-click the Group Policy Object (GPO) you want to configure and click Edit.
7. In the Group Policy Management Editor, go to Computer configuration, then Preferences, and then Control panel settings.
8. Right-click Scheduled tasks, point to New, and then click Immediate task.
9. In the Task window that opens, go to the General tab under Security options and select Change User or Group, enter SYSTEM, then select Check Names and then OK. NT AUTHORITY\SYSTEM appears as the user account that the task will run as.
10. Select Run whether user is logged on or not and check the Run with highest privileges check-box.

## Validation
1. On a target device, open an elevated command prompt and run: schtasks /query /tn "WindowsDefenderATPOffboarding" /v. Verify the task exists and its status is 'Ready' or 'Running'. 2. Check the task's last run time and result: schtasks /query /tn "WindowsDefenderATPOffboarding" /v | findstr /i "Last Run Time Last Result". 3. Confirm the device no longer appears in the Microsoft Defender portal under Devices. 4. Verify the Microsoft Defender for Endpoint service is stopped: sc query WinDefend | findstr /i "STATE". Expected: STOPPED.

## Rollback
1. On the domain controller, open Group Policy Management Console (GPMC). 2. Right-click the GPO used for offboarding and select Edit. 3. Navigate to Computer Configuration > Preferences > Control Panel Settings > Scheduled Tasks. 4. Delete the immediate task named 'WindowsDefenderATPOffboarding'. 5. Close the Group Policy Management Editor. 6. On affected devices, run gpupdate /force to apply the policy change. 7. Re-onboard the device using the onboarding package from the Microsoft Defender portal (System > Settings > Endpoints > Device management > Onboarding).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
