# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How do I create a compliance policy in Microsoft Intune that integrates with Microsoft Defender for Endpoint to enforce device risk levels?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Microsoft Defender for Endpoint integration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to compliance policies: In the Microsoft Intune admin center, select Devices > expand Manage devices and select Compliance > Policies tab > Create policy.
2. Select platform: Choose your target platform: Android device administrator (limited support), Android Enterprise (recommended for Android), iOS/iPadOS, Windows 10 and later. If necessary, select a Profile type, like Windows 10/11 compliance policy for the Windows platform.
3. Configure basics: Name: Enter a descriptive name (for example, 'MDE Risk Level - Windows Devices'). Description: Optional details about the policy purpose.
4. Set risk threshold: On the Compliance settings tab, expand Microsoft Defender for Endpoint and configure 'Require the device to be at or under the machine risk score'. Risk level options (determined by Microsoft Defender for Endpoint): Clear (Most Secure) - Allows: No threats, Blocks: Any detected threats, Use when: Maximum security required; Low - Allows: Low-level threats only, Blocks: Medium and high threats, Use when: Balanced security and productivity; Medium - Allows: Low and medium threats, Blocks: High-level threats only, Use when: Moderate security requirements; High (Least Secure) - Allows: All threat levels, Blocks: None (reporting only), Use when: Maximum productivity, minimal blocking. Recommended setting: Low provides the best balance of security and user productivity for most organizations.

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > Compliance > Policies. Confirm the new compliance policy (e.g., 'MDE Risk Level - Windows Devices') appears in the list with the correct platform and profile type. 2. Select the policy and view its properties; verify that under Compliance settings > Microsoft Defender for Endpoint, 'Require the device to be at or under the machine risk score' is set to the intended risk level (e.g., Low). 3. Enroll a test device that is managed by Intune and has Microsoft Defender for Endpoint onboarded. 4. On the test device, trigger a known low-risk alert (e.g., a test file from Microsoft's EICAR test file) and allow Defender for Endpoint to assess the risk. 5. In the Intune admin center, go to Devices > Compliance > Device compliance and locate the test device. Confirm its compliance status reflects the risk level (e.g., 'Noncompliant' if the risk exceeds the threshold). 6. Optionally, use the Graph API to query the device compliance state: GET https://graph.microsoft.com/v1.0/deviceManagement/managedDevices/{deviceId}/deviceCompliancePolicyStates. Verify the state matches the expected compliance result.

## Rollback
1. In the Microsoft Intune admin center, navigate to Devices > Compliance > Policies. 2. Locate the newly created compliance policy (e.g., 'MDE Risk Level - Windows Devices'). 3. Select the policy and choose 'Delete' from the top menu. Confirm deletion when prompted. 4. If the policy was already assigned to groups, remove those assignments before deletion: select the policy, go to 'Properties', and under 'Assignments', set all groups to 'Not assigned'. 5. Alternatively, to preserve the policy but disable enforcement, edit the policy: under Compliance settings > Microsoft Defender for Endpoint, set 'Require the device to be at or under the machine risk score' to 'Not configured' and save. 6. Verify that devices previously affected by the policy return to their prior compliance state by checking Device compliance in the admin center or via Graph API.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
