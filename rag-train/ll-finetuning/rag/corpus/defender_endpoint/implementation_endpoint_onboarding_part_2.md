# Implementation: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
How to onboard devices to Microsoft Defender for Endpoint using Group Policy?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Group Policy Management Console (GPMC), Active Directory domain

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the device. You should have a folder called OptionalParamsPolicy and the file WindowsDefenderATPOnboardingScript.cmd.
2. To create a new GPO, open the Group Policy Management Console (GPMC), right-click Group Policy Objects you want to configure and click New. Enter the name of the new GPO in the dialog box that is displayed and click OK.
3. Open the Group Policy Management Console (GPMC), right-click the Group Policy Object (GPO) you want to configure and click Edit.
4. In the Group Policy Management Editor, go to Computer configuration, then Preferences, and then Control panel settings.
5. Right-click Scheduled tasks, point to New, and then click Immediate Task (At least Windows 7).
6. In the Task window that opens, go to the General tab. Under Security options click Change User or Group and type SYSTEM and then click Check Names then OK. NT AUTHORITY\SYSTEM appears as the user account the task will run as.
7. Select Run whether user is logged on or not and check the Run with highest privileges check box.
8. In the Name field, type an appropriate name for the scheduled task (for example, Defender for Endpoint Deployment).
9. Go to the Actions tab and select New... Ensure that Start a program is selected in the Action field. Enter the UNC path, using the file server's fully qualified domain name (FQDN), of the shared WindowsDefenderATPOnboardingScript.cmd file.
10. Select OK and close any open GPMC windows.
11. To link the GPO to an Organization Unit (OU), right-click and select Link an existing GPO. In the dialog box that is displayed, select the Group Policy Object that you wish to link. Click OK.

## Validation
1. On a target device in the linked OU, run 'gpupdate /force' from an elevated command prompt. 2. Open Task Scheduler and verify that the immediate task (e.g., 'Defender for Endpoint Deployment') exists under Task Scheduler Library. 3. Manually trigger the task and confirm it completes with exit code 0. 4. On the device, open PowerShell as administrator and run 'Get-MpComputerStatus | Select-Object AMProductVersion, AMServiceEnabled, AntispywareEnabled, AntivirusEnabled'. Verify that AMProductVersion is not empty and the three *Enabled fields are True. 5. In the Microsoft 365 Defender portal (https://security.microsoft.com), navigate to Devices list and confirm the device appears within 1 hour.

## Rollback
1. In Group Policy Management Console, right-click the linked GPO and select 'Delete' to remove the link from the OU. 2. Under Group Policy Objects, right-click the GPO and select 'Delete', confirming the deletion. 3. On each affected device, run 'gpupdate /force' from an elevated command prompt to remove the scheduled task. 4. Open Task Scheduler, locate the immediate task (e.g., 'Defender for Endpoint Deployment'), right-click and select 'Delete'. 5. On the device, open an elevated PowerShell and run 'Uninstall-WindowsFeature -Name Windows-Defender' (if Defender was not originally installed) or 'Set-MpPreference -DisableRealtimeMonitoring $true' to revert onboarding. 6. In Microsoft 365 Defender portal, verify the device no longer appears in the Devices list.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
