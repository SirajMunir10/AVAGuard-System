# Implementation: Endpoint Configuration

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Configuration
**Incident Type:** Implementation

## Scenario / Query
How to monitor device configuration for Microsoft Defender for Endpoint using Configuration Manager?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Configuration Manager current branch or System Center 2012 R2 Configuration Manager

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If using Microsoft Configuration Manager current branch, use the built-in Defender for Endpoint dashboard in the Configuration Manager console.
2. If using System Center 2012 R2 Configuration Manager, monitoring consists of two parts: Confirming the configuration package has been correctly deployed and is running (or has successfully run) on the devices in your network. Checking that the devices are compliant with the Defender for Endpoint service (this ensures the device can complete the onboarding process and can continue to report data to the service).

## Validation
1. For Configuration Manager current branch: Open the Configuration Manager console, navigate to 'Monitoring' > 'Security' > 'Microsoft Defender for Endpoint' and verify the dashboard shows devices as 'Onboarded' and 'Healthy'. 2. For System Center 2012 R2: In the Configuration Manager console, go to 'Monitoring' > 'Deployments' and confirm the Defender for Endpoint configuration package deployment status is 'Success' for target devices. 3. On a sample device, open the Configuration Manager client in Control Panel, go to the 'Actions' tab, and verify the 'Machine Policy Retrieval & Evaluation Cycle' and 'Software Inventory Cycle' have run successfully. 4. Run the following PowerShell command on a device to confirm the Defender for Endpoint service is running: Get-Service -Name 'Sense' | Select-Object Status, StartType. Ensure Status is 'Running' and StartType is 'Automatic'.

## Rollback
1. If the dashboard or deployment shows errors, redeploy the configuration package: In the Configuration Manager console, navigate to 'Assets and Compliance' > 'Endpoint Protection' > 'Microsoft Defender for Endpoint Policies', right-click the policy, and select 'Deploy' to target devices again. 2. If devices fail to onboard, remove and re-add the onboarding configuration: In the same policy, under 'Onboarding' settings, clear the current configuration, apply, then re-enter the correct onboarding blob from the Microsoft Defender portal. 3. For System Center 2012 R2, if the configuration package fails, delete the existing deployment from 'Monitoring' > 'Deployments', then create a new deployment from 'Software Library' > 'Application Management' > 'Packages' using the original Defender for Endpoint package source. 4. If the Sense service is not running, set it to automatic and start it manually: Set-Service -Name 'Sense' -StartupType Automatic; Start-Service -Name 'Sense'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
