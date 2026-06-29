# Implementation: Endpoint Deployment

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Deployment
**Incident Type:** Implementation

## Scenario / Query
How to configure Windows 10 devices using mobile device management (MDM) solutions for Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** MDM OMA-URIs for Defender for Endpoint CSP

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use mobile device management (MDM) solutions to configure Windows 10 devices.
2. Create policies using OMA-URIs provided by Defender for Endpoint.
3. Refer to WindowsAdvancedThreatProtection CSP and WindowsAdvancedThreatProtection DDF file for more information.

## Validation
1. Verify that the MDM policy has been applied to a test Windows 10 device by navigating to Settings > Accounts > Access work or school > select the MDM enrollment > Info. Confirm that the 'Microsoft Defender for Endpoint' configuration source shows 'MDM' and the policy name. 2. On the same device, open an elevated PowerShell prompt and run: Get-MpComputerStatus | Select-Object -Property AMProductVersion, AMServiceEnabled, AntispywareEnabled, AntivirusEnabled, BehaviorMonitorEnabled, IoavProtectionEnabled, NISEnabled, OnAccessProtectionEnabled, RealTimeProtectionEnabled. Verify that all properties show 'True' except AMProductVersion which should show a version number. 3. In the Microsoft 365 Defender portal (https://security.microsoft.com), navigate to Devices > Inventory, search for the test device, and confirm its 'Onboarding status' is 'Onboarded' and 'Sensor health' is 'Active'.

## Rollback
1. In the MDM console (e.g., Microsoft Intune), locate the policy created for Defender for Endpoint configuration and either delete the policy or remove the assignment from the test device group. 2. On the affected Windows 10 device, force a sync with MDM by going to Settings > Accounts > Access work or school > select the MDM enrollment > Info > Sync. 3. After the sync completes, verify that the Defender for Endpoint configuration is removed by running the same PowerShell command from validation step 2 and confirming that the previously enabled protections are now disabled or reverted to default. 4. If the device remains in a degraded state, manually re-enable Microsoft Defender for Endpoint by running the following command in an elevated PowerShell prompt: & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -EnableContinuousCloudProtection. 5. As a last resort, unenroll the device from MDM by going to Settings > Accounts > Access work or school > select the MDM enrollment > Disconnect, then re-enroll if needed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-mdm>
- <https://learn.microsoft.com/en-us/windows/client-management/mdm/windowsadvancedthreatprotection-csp>
- <https://learn.microsoft.com/en-us/windows/client-management/mdm/windowsadvancedthreatprotection-ddf>
