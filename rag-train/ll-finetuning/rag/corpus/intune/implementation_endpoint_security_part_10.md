# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to configure Microsoft Defender for Endpoint integration with Intune for vulnerability management and compliance?

## Environment Context
- **Tenant Type:** Microsoft Intune with Microsoft Defender for Endpoint
- **Configuration:** Advanced features Intune integration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure Security tasks with Vulnerability Management to remediate device vulnerabilities.
2. Configure Device compliance policies for comprehensive compliance management.
3. Configure App protection policies for mobile app data protection.
4. Configure Mobile app protection policies for Android and iOS/iPadOS devices to set device risk levels, working with both enrolled and unenrolled devices.
5. Configure Security Management for unenrolled devices to manage Defender for Endpoint security configurations on devices that aren't enrolled with Intune (including Linux devices).
6. Configure Microsoft Defender for Endpoint Conditional Access integration for advanced access control scenarios.
7. Configure Microsoft Defender for Endpoint reports for threat monitoring and response.

## Validation
1. Verify that Security tasks are enabled: In Microsoft Intune admin center, go to 'Endpoint security' > 'Vulnerability management' > 'Security tasks'. Confirm that the 'Security tasks' page displays tasks from Microsoft Defender for Endpoint. 2. Verify device compliance policies: Navigate to 'Devices' > 'Compliance policies' > 'Policies'. Ensure a policy exists that uses 'Microsoft Defender for Endpoint' as a compliance setting (e.g., requiring a device risk score). 3. Verify app protection policies: Go to 'Apps' > 'App protection policies'. Confirm that a policy for iOS/iPadOS or Android includes the setting 'Require device risk level' under 'Conditional launch' and that it references Microsoft Defender for Endpoint. 4. Verify security management for unenrolled devices: In 'Endpoint security' > 'Security management for unenrolled devices', confirm that the integration is enabled and that devices appear in the 'Managed devices' list. 5. Verify Conditional Access integration: In Microsoft Entra admin center, go to 'Protection' > 'Conditional Access' > 'Policies'. Confirm a policy exists that uses 'Require device to be marked as compliant' or 'Require Microsoft Defender for Endpoint risk score' as a grant control. 6. Verify reports: In Microsoft Defender portal, go to 'Reports' > 'Vulnerability management' and confirm that data from Intune-managed devices is present.

## Rollback
1. Disable Security tasks: In Intune admin center, go to 'Endpoint security' > 'Vulnerability management' > 'Security tasks' and turn off the integration toggle. 2. Remove or modify device compliance policies: Navigate to 'Devices' > 'Compliance policies' > 'Policies'. Delete or edit any policy that uses Microsoft Defender for Endpoint risk settings, removing those conditions. 3. Remove or modify app protection policies: Go to 'Apps' > 'App protection policies'. Delete or edit policies that reference device risk level from Microsoft Defender for Endpoint. 4. Disable security management for unenrolled devices: In 'Endpoint security' > 'Security management for unenrolled devices', turn off the integration. 5. Remove or modify Conditional Access policies: In Microsoft Entra admin center, go to 'Protection' > 'Conditional Access' > 'Policies'. Delete or edit policies that require Microsoft Defender for Endpoint compliance or risk. 6. Disable the Microsoft Defender for Endpoint integration in Intune: In Intune admin center, go to 'Tenant administration' > 'Connectors and tokens' > 'Microsoft Defender for Endpoint' and set the toggle to 'Off'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
