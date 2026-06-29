# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to onboard devices to communicate with Defender for Endpoint using Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint detection and response policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure admin access to the Microsoft Intune admin center with Endpoint Security Manager role or equivalent permissions for Endpoint detection and response policies (custom roles require Assign, Create, Delete, Read, Update, and View Reports rights for the Endpoint Detection and Response permission).
2. Always use the latest Defender for Endpoint version for each platform to ensure optimal protection and compatibility.
3. For Windows: Use automatic onboarding package (recommended).
4. For macOS, Android, iOS/iPadOS: Manual configuration required.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Endpoint detection and response. Confirm that a policy exists for the target platform (Windows, macOS, Android, or iOS/iPadOS).
2. Select the policy and verify that the configuration profile is assigned to the correct device groups.
3. On a test device, open the Microsoft Defender for Endpoint security center (https://security.microsoft.com) and navigate to Devices list. Confirm the device appears with an active status.
4. On the device, run the command: `Get-MpComputerStatus | Select-Object AMRunningMode, AMProductVersion, OnboardingState` (Windows) or check the Defender for Endpoint app for a 'Connected' indicator (macOS, Android, iOS/iPadOS).
5. Verify that the device's onboarding state is 'Onboarded' and the AMRunningMode is 'Normal' (Windows) or the device shows as 'Active' in the Microsoft 365 Defender portal.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Endpoint detection and response.
2. Select the policy that was applied for onboarding and change its assignment to 'Not assigned' or remove the device group from the assignment list.
3. Wait for the policy to sync (up to 8 hours) or force a sync on the device: On Windows, go to Settings > Accounts > Access work or school > select the MDM enrollment > Info > Sync. On macOS, open Company Portal and click Check Status > Sync. On Android/iOS, open Company Portal and tap Devices > select device > Check Status.
4. On the device, confirm the Defender for Endpoint connection is removed: On Windows, run `Get-MpComputerStatus | Select-Object OnboardingState` and verify it shows 'Not onboarded'. On other platforms, the Defender for Endpoint app should show 'Disconnected' or the device should no longer appear in the Microsoft 365 Defender portal.
5. If the device remains onboarded, manually offboard using the offboarding script from the Microsoft 365 Defender portal (Settings > Endpoints > Offboarding) and redeploy the device if necessary.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
