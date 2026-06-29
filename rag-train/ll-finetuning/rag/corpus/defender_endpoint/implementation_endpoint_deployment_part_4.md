# Implementation: Endpoint Deployment

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Deployment
**Incident Type:** Implementation

## Scenario / Query
How to deploy Microsoft Defender endpoint security to Windows devices using the Defender deployment tool?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** Defender deployment tool

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Defender deployment tool to deploy Defender endpoint security on Windows devices.
2. The tool is a lightweight, self-updating application that streamlines the deployment process.

## Validation
1. On a target Windows device, open the Microsoft Defender for Endpoint portal (https://security.microsoft.com) and navigate to 'Devices' to confirm the device appears in the inventory. 2. On the device, run 'Get-MpComputerStatus' in PowerShell and verify that 'AMProductVersion' and 'AMEngineVersion' are populated, and 'AntivirusEnabled' is True. 3. Check the deployment tool logs at 'C:\ProgramData\Microsoft\Windows Defender\Platform\<version>\MpCmdRun.log' for successful configuration entries.

## Rollback
1. On the affected Windows device, open PowerShell as Administrator and run 'Uninstall-WindowsFeature -Name Windows-Defender' (if applicable) or use 'MpCmdRun.exe -RemoveDefinitions -All' to reset Defender components. 2. In the Microsoft Defender for Endpoint portal, navigate to 'Settings > Endpoints > Onboarding' and generate a new package for 'Local Script' (not the deployment tool), then run the script on the device to revert to manual onboarding. 3. If the device was previously managed by a different MDM, re-enroll it via 'Settings > Accounts > Access work or school > Disconnect' and then reconnect using the original MDM configuration.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-mdm>
- <https://learn.microsoft.com/en-us/defender-endpoint/deploy-defender-endpoint-windows-defender-deployment-tool>
