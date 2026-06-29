# Implementation: Endpoint security

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint security
**Incident Type:** Implementation

## Scenario / Query
How to offboard devices using Configuration Manager in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Configuration Manager

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Download the offboarding package from the Microsoft Defender portal.
2. Deploy the offboarding package to devices using Configuration Manager.
3. Ensure the offboarding package is deployed within 7 days of download, as it expires after that date.
4. Do not deploy onboarding and offboarding policies on the same device at the same time to avoid unpredictable collisions.

## Validation
1. In the Configuration Manager console, go to Monitoring > Deployments and verify that the offboarding package deployment completed successfully (status 'Compliant' or 'Success').
2. On a sample offboarded device, open PowerShell as administrator and run: Get-MpComputerStatus | select AMRunningMode. Confirm the output shows 'Passive' or 'Not Running' (not 'Active').
3. On the same device, run: Get-Service -Name Sense. Verify the service status is 'Stopped' or 'Disabled'.
4. Check the Microsoft Defender portal (security.microsoft.com) > Devices list; confirm the device no longer appears as an active onboarded device.

## Rollback
1. Download a fresh onboarding package from the Microsoft Defender portal (Settings > Endpoints > Onboarding).
2. In Configuration Manager, create a new application or package for the onboarding script (.cmd or .ps1).
3. Deploy the onboarding package to the same device collection that received the offboarding package, ensuring the deployment is mandatory and immediate.
4. On a sample device, run: Get-MpComputerStatus | select AMRunningMode. Confirm the output shows 'Active'.
5. Verify the Sense service is running: Get-Service -Name Sense | select Status (should be 'Running').
6. In the Microsoft Defender portal, confirm the device reappears as active within 1 hour.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
