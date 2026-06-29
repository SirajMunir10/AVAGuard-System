# Implementation: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
How to onboard devices to Microsoft Defender for Endpoint using Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Intune MDM

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Check out Identify Defender for Endpoint architecture and deployment method to see the various paths in deploying Defender for Endpoint.
2. Follow the instructions from Intune.
3. For more information on using Defender for Endpoint CSP, see WindowsAdvancedThreatProtection CSP and WindowsAdvancedThreatProtection DDF file.

## Validation
1. In the Microsoft Intune admin center, go to Devices > Configuration profiles and confirm a profile using the 'WindowsAdvancedThreatProtection' CSP is assigned to the target device group. 2. On a test device, open Settings > Accounts > Access work or school and verify the device is enrolled in Intune MDM. 3. On the same device, run 'dsregcmd /status' and confirm the AzureAdJoined and DomainJoined statuses are correct. 4. Open Microsoft Defender Security Center, navigate to Devices list, and verify the device appears with an active status. 5. On the device, open PowerShell as administrator and run 'Get-MpComputerStatus | select AMRunningMode' to confirm the mode is 'Normal' or 'Passive' as expected.

## Rollback
1. In the Microsoft Intune admin center, go to Devices > Configuration profiles, select the Defender for Endpoint onboarding profile, and change the assignment to 'Not assigned' or delete the profile. 2. On each affected device, open Settings > Accounts > Access work or school, select the Intune enrollment, and click 'Disconnect' to remove MDM management. 3. On the device, open an elevated PowerShell prompt and run 'Remove-MpPreference -DisableRealtimeMonitoring $false' if real-time monitoring was disabled. 4. Restart the device to clear any Defender for Endpoint service state. 5. In Microsoft Defender Security Center, confirm the device no longer appears in the Devices list after a few hours.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-mdm>
