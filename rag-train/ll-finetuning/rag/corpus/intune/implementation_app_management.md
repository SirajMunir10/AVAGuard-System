# Implementation: App Management

**Domain:** Intune
**Subdomain:** App Management
**Incident Type:** Implementation

## Scenario / Query
What app types are supported on ARM64 devices in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** ARM64 device app deployment

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure web apps do not require a managed browser to open.
2. For Microsoft Store for Business apps or Windows Universal LOB apps (.appx), verify TargetDeviceFamily includes Desktop apps, Universal apps, or Windows8x apps (Windows8x apps apply only as Online Microsoft Store for Business apps).
3. Ensure ProcessorArchitecture includes x86 apps, ARM apps, ARM64 apps, or neutral apps.
4. For Win32 apps, set the requirement rule to 32-bit.
5. For Windows Office click-to-run apps, select 32-bit or x86 architecture.
6. Consider adding 'ARM64' to the name of ARM64 apps in the Company Portal for better recognition.

## Validation
1. In the Intune admin center, navigate to Apps > All apps and select the web app. Under Settings, confirm that 'Require a managed browser to open this link' is set to 'No'.
2. For Microsoft Store for Business apps or Windows Universal LOB apps (.appx), open the app properties and verify that the TargetDeviceFamily includes 'Desktop', 'Universal', or 'Windows.8x' (Windows.8x only for online Microsoft Store for Business apps).
3. In the same app properties, confirm that ProcessorArchitecture includes 'x86', 'ARM', 'ARM64', or 'Neutral'.
4. For Win32 apps, go to the app properties and under Requirements, verify that the architecture requirement rule is set to '32-bit'.
5. For Windows Office click-to-run apps, in the app properties under Architecture, confirm that '32-bit' or 'x86' is selected.
6. In the Company Portal, verify that ARM64 apps have 'ARM64' in their display name for better user recognition.

## Rollback
1. For web apps, set 'Require a managed browser to open this link' back to 'Yes' if it was previously enabled.
2. For Microsoft Store for Business or Windows Universal LOB apps, revert TargetDeviceFamily to its original values (e.g., remove 'Desktop', 'Universal', or 'Windows.8x' if they were added).
3. In the same apps, revert ProcessorArchitecture to its original values (e.g., remove 'x86', 'ARM', 'ARM64', or 'Neutral' if they were added).
4. For Win32 apps, change the requirement rule back to the original architecture setting (e.g., '64-bit' if it was previously set).
5. For Windows Office click-to-run apps, revert the architecture selection to the original value (e.g., '64-bit' if it was previously selected).
6. Remove 'ARM64' from the display name of ARM64 apps in the Company Portal if it was added.

## References
- <https://learn.microsoft.com/en-us/mem/intune/apps/troubleshoot-app-install>
