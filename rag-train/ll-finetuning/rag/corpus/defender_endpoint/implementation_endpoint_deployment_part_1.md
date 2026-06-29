# Implementation: Endpoint Deployment

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Deployment
**Incident Type:** Implementation

## Scenario / Query
How to deploy Defender for Endpoint offboarding script via Group Policy scheduled task?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Group Policy Management Console (GPMC), scheduled task with highest privileges

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Run whether user is logged on or not and check the Run with highest privileges check-box.
2. In the Name field, type an appropriate name for the scheduled task (for example, Defender for Endpoint Deployment).
3. Go to the Actions tab and select New... . Ensure that Start a program is selected in the Action field.
4. Enter the UNC path, using the file server's fully qualified domain name (FQDN), of the shared WindowsDefenderATPOffboardingScript_valid_until_YYYY-MM-DD.cmd file.
5. Select OK and close any open GPMC windows.

## Validation
1. On a target client, open Task Scheduler and verify that the scheduled task (e.g., 'Defender for Endpoint Deployment') exists under Task Scheduler Library. 2. Confirm the task is configured with 'Run whether user is logged on or not' and 'Run with highest privileges'. 3. On the Actions tab, verify that the action is 'Start a program' pointing to the correct UNC path (e.g., \\fileserver\share\WindowsDefenderATPOffboardingScript_valid_until_YYYY-MM-DD.cmd). 4. Run the task manually and check the last run result for success (0x0). 5. Verify that the offboarding script executed by checking the client's Microsoft Defender for Endpoint status (e.g., via PowerShell: Get-MpComputerStatus | Select-Object AMRunningMode).

## Rollback
1. On the Domain Controller or management machine, open Group Policy Management Console (GPMC). 2. Navigate to the GPO containing the scheduled task and edit it. 3. Under Computer Configuration > Preferences > Control Panel Settings > Scheduled Tasks, delete the scheduled task entry (e.g., 'Defender for Endpoint Deployment'). 4. Alternatively, disable the task by unchecking 'Run whether user is logged on or not' and 'Run with highest privileges', or change the action to a benign script. 5. Force a gpupdate on affected clients (gpupdate /force) and verify the task is removed or disabled. 6. If the offboarding script already ran, re-onboard the device using the appropriate onboarding script or package from Microsoft Defender portal.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
