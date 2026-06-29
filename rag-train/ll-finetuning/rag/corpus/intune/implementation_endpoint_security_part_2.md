# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to configure Microsoft Defender for Endpoint integration with Intune for mobile devices including Android and iOS/iPadOS?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Microsoft Defender for Endpoint integration settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Connect services
2. Configure integration settings
3. Onboard devices
4. Configure compliance policies
5. Configure app protection policies
6. Set up Conditional Access

## Validation
1. Verify service-to-service connection: In Microsoft Intune admin center, navigate to 'Tenant administration' > 'Connectors and tokens' > 'Microsoft Defender for Endpoint'. Confirm the status shows 'Enabled' and the connection state is 'Active'.
2. Check integration settings: In Intune, go to 'Endpoint security' > 'Microsoft Defender for Endpoint'. Ensure 'Allow Microsoft Defender for Endpoint to enforce compliance' and 'Allow Microsoft Defender for Endpoint to collect device signals' are both set to 'On'.
3. Validate device onboarding: For Android, confirm that the Microsoft Defender for Endpoint app is installed and activated on test devices. For iOS/iPadOS, verify the app is installed and the device is registered via the Company Portal.
4. Confirm compliance policies: In Intune, navigate to 'Devices' > 'Compliance policies' > 'Policies'. Select the policy for Android/iOS and verify that 'Require the device to be at or under the machine risk score' is set to 'Medium' or 'Low'.
5. Verify app protection policies: Go to 'Apps' > 'App protection policies' > 'Policies'. Select the policy for Android/iOS and confirm 'Require Defender for Endpoint threat scan on apps' is enabled.
6. Test Conditional Access: Sign in to a test device and attempt to access a protected resource (e.g., Exchange Online). Verify that access is blocked if the device has a high-risk alert in Defender for Endpoint.

## Rollback
1. Disable service connection: In Intune admin center, navigate to 'Tenant administration' > 'Connectors and tokens' > 'Microsoft Defender for Endpoint'. Set the toggle to 'Disabled' and confirm disconnection.
2. Turn off integration settings: Go to 'Endpoint security' > 'Microsoft Defender for Endpoint'. Set both 'Allow Microsoft Defender for Endpoint to enforce compliance' and 'Allow Microsoft Defender for Endpoint to collect device signals' to 'Off'.
3. Remove compliance policies: In 'Devices' > 'Compliance policies' > 'Policies', select the policies that reference Defender for Endpoint risk score and delete them or set the risk score requirement to 'Unrestricted'.
4. Remove app protection policies: In 'Apps' > 'App protection policies' > 'Policies', select the policies that require Defender for Endpoint threat scan and delete them or disable the threat scan setting.
5. Disable Conditional Access: In Azure AD admin center, navigate to 'Security' > 'Conditional Access' > 'Policies'. Locate policies that require device compliance with Defender for Endpoint and set them to 'Off' or delete them.
6. Uninstall Defender for Endpoint app: For Android, instruct users to uninstall the Microsoft Defender for Endpoint app. For iOS/iPadOS, remove the app via MDM or instruct users to delete it.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
