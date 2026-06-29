# Implementation: Microsoft Defender for Endpoint integration

**Domain:** Intune
**Subdomain:** Microsoft Defender for Endpoint integration
**Incident Type:** Implementation

## Scenario / Query
How to connect Microsoft Defender for Endpoint to Microsoft Intune and configure compliance and Conditional Access policies using device risk levels?

## Environment Context
- **Tenant Type:** Microsoft Intune with Microsoft Defender for Endpoint
- **Configuration:** Integration prerequisites and task-specific requirements

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review general integration prerequisites.
2. Follow step-by-step instructions to connect Microsoft Defender for Endpoint to Microsoft Intune.
3. Onboard devices to Defender for Endpoint by platform.
4. Configure compliance and Conditional Access policies that use device risk levels to control access to corporate resources.

## Validation
1. Verify that the Microsoft Defender for Endpoint connector is enabled in Microsoft Intune: navigate to Microsoft Intune admin center > Endpoint security > Microsoft Defender for Endpoint and confirm the status shows 'Enabled'.
2. Confirm that devices are successfully onboarded to Defender for Endpoint by checking the Microsoft 365 Defender portal > Assets > Devices and verifying the device list shows the expected devices with 'Active' status.
3. Validate that a compliance policy using device risk level is created and assigned: in Intune admin center > Devices > Compliance policies, select the policy and confirm that 'Require the device to be at or under the Device Threat Level' is set to a specific level (e.g., Low, Medium, High).
4. Test Conditional Access: sign in to a test device that meets the compliance policy and verify access to a protected resource (e.g., Exchange Online) is granted; then simulate a high-risk device (e.g., by triggering a test alert in Defender) and confirm access is blocked.
5. Run the following PowerShell command to check the connector status: Get-MgDeviceManagementAdvancedThreatProtectionOnboardingStateSummary (requires Microsoft Graph PowerShell SDK).

## Rollback
1. Disable the Microsoft Defender for Endpoint connector: in Intune admin center > Endpoint security > Microsoft Defender for Endpoint, set the toggle to 'Off' and save.
2. Remove any compliance policies that reference device risk levels: in Intune admin center > Devices > Compliance policies, select the policy and click 'Delete'.
3. Remove or disable Conditional Access policies that use device risk: in Azure AD admin center > Security > Conditional Access, locate the policy and set 'Enable policy' to 'Off' or delete the policy.
4. If devices were onboarded to Defender for Endpoint via Intune, remove the onboarding configuration profile: in Intune admin center > Devices > Configuration profiles, select the Defender for Endpoint onboarding profile and click 'Delete'.
5. Revert any test changes made to device risk levels in Defender for Endpoint (e.g., clear test alerts) by following Microsoft Defender for Endpoint documentation for removing test indicators.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
