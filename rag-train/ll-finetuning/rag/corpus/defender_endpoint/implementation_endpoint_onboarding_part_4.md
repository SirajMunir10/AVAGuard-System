# Implementation: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
How to onboard endpoints to Microsoft Defender for Endpoint using Configuration Manager?

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
1. Use Configuration Manager to onboard endpoints to the Microsoft Defender for Endpoint service.
2. Options include: Onboard devices using System Center Configuration Manager, Tenant attach.
3. Create a detection rule on a Configuration Manager application to continuously check if a device has been onboarded.
4. If a device is not yet onboarded (due to pending OOBE completion or any other reason), Configuration Manager reattempts to onboard the device until the rule detects the status change.

## Validation
1. In Configuration Manager console, navigate to 'Assets and Compliance' > 'Endpoint Protection' > 'Microsoft Defender for Endpoint Policies'. Verify the policy is deployed to the target collection. 2. On a test device, open 'Settings' > 'Privacy & security' > 'Windows Security' > 'Virus & threat protection' > 'Manage settings' and confirm 'Tamper Protection' is enabled. 3. Run the PowerShell command 'Get-MpComputerStatus | Select-Object AMRunningMode, AMProductVersion, AMServiceEnabled' on the device to confirm Defender is active. 4. In Microsoft 365 Defender portal (security.microsoft.com), go to 'Devices' and verify the device appears in the inventory with 'Active' status.

## Rollback
1. In Configuration Manager, delete or disable the Microsoft Defender for Endpoint onboarding policy from the target collection. 2. On affected devices, run the PowerShell command 'Set-MpPreference -DisableRealtimeMonitoring $true' to disable real-time protection temporarily. 3. In Microsoft 365 Defender portal, remove the device from the inventory if needed via 'Devices' > select device > 'Remove device'. 4. If tenant attach was used, detach the Configuration Manager site from the Microsoft Defender for Endpoint tenant by running the PowerShell cmdlet 'Disconnect-CMCloudAttach' on the site server.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
