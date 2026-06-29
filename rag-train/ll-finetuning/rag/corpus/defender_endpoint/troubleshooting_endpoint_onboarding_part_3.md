# Troubleshooting: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot onboarding issues on Windows Server 2016 and earlier versions of Windows Server?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Windows Server 2016 and earlier versions

## Symptoms
- Devices not reflected in the Devices list in the portal

## Error Codes
N/A

## Root Causes
1. Microsoft Monitoring Agent (MMA) not installed or configured to report sensor data to the service
2. Server proxy and Internet connectivity settings not configured properly
3. Microsoft Defender for Endpoint Service not running in Task Manager
4. Errors in Event Viewer under Applications and Services Logs > Operation Manager
5. Microsoft Monitoring Agent service not running on the server
6. Workspace status in Microsoft Monitoring Agent > Azure Log Analytics (OMS) not running

## Remediation Steps
1. Ensure Microsoft Monitoring Agent (MMA) is installed and configured to report sensor data to the service
2. Ensure that the server proxy and Internet connectivity settings are configured properly
3. Check that there's a Microsoft Defender for Endpoint Service running in the Processes tab in Task Manager
4. Check Event Viewer > Applications and Services Logs > Operation Manager to see if there are any errors
5. In Services, check if the Microsoft Monitoring Agent is running on the server
6. In Microsoft Monitoring Agent > Azure Log Analytics (OMS), check the Workspaces and verify that the status is running
7. Check to see that devices are reflected in the Devices list in the portal

## Validation
1. On the Windows Server 2016 (or earlier) device, open Services.msc and verify that the 'Microsoft Monitoring Agent' service is running. 2. Open Task Manager, go to the Processes tab, and confirm that 'Microsoft Defender for Endpoint Service' (MsSense.exe) is listed and running. 3. Open Event Viewer, navigate to Applications and Services Logs > Operation Manager, and check for any error events. 4. Open Microsoft Monitoring Agent from Control Panel, select the Azure Log Analytics (OMS) tab, and verify that the workspace status shows 'Running'. 5. Log into the Microsoft Defender for Endpoint portal (https://security.microsoft.com), go to Devices list, and confirm the server appears within 15 minutes.

## Rollback
1. If the Microsoft Monitoring Agent (MMA) was newly installed, uninstall it via Control Panel > Programs and Features. 2. If proxy or connectivity settings were changed, revert them to the original configuration in the MMA properties (Proxy Settings tab). 3. If the Microsoft Monitoring Agent service was started, stop it via Services.msc and set startup type back to 'Disabled' if it was previously disabled. 4. If the workspace was added in MMA, remove it from the Azure Log Analytics (OMS) tab. 5. If the device appears incorrectly in the portal, contact Microsoft support to remove the device record.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
