# Implementation: Endpoint deployment

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint deployment
**Incident Type:** Implementation

## Scenario / Query
How to deploy Defender endpoint security on Windows and Linux devices using the Defender deployment tool?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Defender deployment tool

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Defender deployment tool to deploy Defender endpoint security on Windows and Linux devices.
2. The tool is a lightweight, self-updating application that streamlines the deployment process.
3. For more information, see Deploy Microsoft Defender endpoint security to Windows devices using the Defender deployment tool and Deploy Microsoft Defender endpoint security to Linux devices using the Defender deployment tool (preview).

## Validation
1. On a Windows device, open the Defender deployment tool and verify that the device status shows 'Protected' or 'Managed' under the 'Devices' tab. 2. On a Linux device, run 'mdatp health' in the terminal and confirm that 'healthy' is true and 'org_id' matches your tenant. 3. In the Microsoft 365 Defender portal, navigate to Assets > Devices and confirm the devices appear with an active sensor status.

## Rollback
1. On Windows, uninstall the Defender deployment tool via 'Add or remove programs' and remove the onboarding package by running 'C:\Program Files\Windows Defender\MpCmdRun.exe -RemoveDefinitions -All'. 2. On Linux, run 'sudo apt-get remove mdatp' (or equivalent package manager command) and then 'sudo rm -rf /etc/opt/microsoft/mdatp'. 3. In the Microsoft 365 Defender portal, navigate to Settings > Endpoints > Offboarding and generate an offboarding package for each affected device, then run the offboarding script on the device.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
