# Implementation: Endpoint Deployment

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Deployment
**Incident Type:** Implementation

## Scenario / Query
How to deploy Microsoft Defender endpoint security to Linux devices using the Defender deployment tool (preview)?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** Defender deployment tool (preview)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Defender deployment tool to deploy Defender endpoint security on Linux devices.
2. The tool is a lightweight, self-updating application that streamlines the deployment process.

## Validation
1. On a Linux device targeted for deployment, run: 'mdatp health' to verify the Microsoft Defender for Endpoint agent is installed and running. Confirm the output shows 'healthy: true' and 'org_id' matches your tenant. 2. In the Microsoft 365 Defender portal (https://security.microsoft.com), navigate to 'Endpoints' > 'Device inventory' and confirm the Linux device appears with status 'Active'. 3. Verify the deployment tool logs: check '/var/log/microsoft/mdatp/install.log' for successful installation entries.

## Rollback
1. On the affected Linux device, uninstall the Defender agent: 'sudo apt-get remove mdatp' (for Debian-based) or 'sudo yum remove mdatp' (for RHEL-based). 2. If the deployment tool was used, remove its configuration: 'sudo rm -rf /etc/opt/microsoft/mdatp' and 'sudo rm -rf /var/opt/microsoft/mdatp'. 3. In the Microsoft 365 Defender portal, remove the device from the device inventory if it appears as 'Inactive' or 'Unhealthy' to avoid stale entries.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-mdm>
- <https://learn.microsoft.com/en-us/defender-endpoint/deploy-defender-endpoint-linux-defender-deployment-tool>
