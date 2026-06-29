# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why are screens disabled in the Windows Autopilot profile shown during a Windows Autopilot for existing devices deployment?

## Environment Context
- **Tenant Type:** Configuration Manager task sequence
- **Configuration:** Windows Autopilot for existing devices deployment

## Symptoms
- Screens that are disabled in the Windows Autopilot profile are shown, such as the Windows License Agreement screen

## Error Codes
N/A

## Root Causes
1. Windows deletes the AutopilotConfigurationFile.json file when Sysprep.exe runs with the /Generalize parameter
2. The Prepare Windows for Capture task in a Configuration Manager task sequence runs Sysprep.exe with the /Generalize parameter

## Remediation Steps
1. Edit the Configuration Manager task sequence and disable the Prepare Windows for Capture step
2. Add a new Run command-line step that runs the following command: C:\Windows\System32\sysprep\sysprep.exe /oobe /reboot

## Validation
1. In the Configuration Manager console, navigate to the task sequence used for Windows Autopilot for existing devices. Verify that the 'Prepare Windows for Capture' step is disabled (e.g., right-click the step and select 'Disable'). 2. Confirm that a new 'Run Command Line' step exists with the command: C:\Windows\System32\sysprep\sysprep.exe /oobe /reboot. 3. Deploy the updated task sequence to a test device. After the deployment completes, check that the Windows Autopilot deployment shows only the screens enabled in the Autopilot profile (e.g., the Windows License Agreement screen should not appear). 4. On the test device, verify that the file C:\Windows\Provisioning\Autopilot\AutopilotConfigurationFile.json exists and contains the expected Autopilot profile settings.

## Rollback
1. In the Configuration Manager console, edit the task sequence. 2. Enable the previously disabled 'Prepare Windows for Capture' step (right-click the step and select 'Enable'). 3. Delete the 'Run Command Line' step that runs sysprep.exe /oobe /reboot. 4. Redeploy the original task sequence to affected devices. 5. On a test device, run the deployment to confirm that the Windows Autopilot for existing devices process reverts to the previous behavior (i.e., the Windows License Agreement screen may appear again). 6. If needed, restore any other customizations made to the task sequence from a backup.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
