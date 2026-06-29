# Implementation: Endpoint Device Management

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Device Management
**Incident Type:** Implementation

## Scenario / Query
How to offboard devices from Microsoft Defender for Endpoint using Mobile Device Management (MDM) tools like Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Mobile Device Management / Microsoft Intune deployment method

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Get the offboarding package from the Microsoft Defender portal: In the navigation pane, select Settings > Endpoints > Device management > Offboarding.
2. Select Windows 10 or Windows 11 as the operating system.
3. In the Deployment method field, select Mobile Device Management / Microsoft Intune.
4. Select Download package, and save the .zip file.
5. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the network administrators who'll deploy the package. You should have a file named WindowsDefenderATP_valid_until_YYYY-MM-DD.offboarding.
6. In the Microsoft Intune admin center, use a custom configuration policy or an EDR policy.
7. For custom configuration policy: In the navigation pane, select Devices > By platform > Windows > Manage Devices > Configuration. Under Policies select Create > New Policy. In the Create a profile slide out, select Windows 10 and later as Platform and Templates as Profile Type. Under Template Name, select the Custom template and select Create. Enter a value for Name and select Next. Under Configuration settings, select Add and use the following OMA-URI settings: - Name: Provide a name - OMA-URI: ./Device/Vendor/MSFT/WindowsAdvancedThreatProtection/Offboarding - Date type: String - Value: Copy and paste the value from the content of the WindowsDefenderATP_valid_until_YYYY-MM-DD offboarding file. Make the appropriate group assignments, applicability rules, and on the Review + create step, select Create.

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > By platform > Windows > Manage Devices > Configuration. Select the custom configuration policy you created. Under Device status, verify that the policy is successfully applied to the target devices (status shows 'Succeeded').
2. On a target Windows 10/11 device, open an elevated PowerShell prompt and run: Get-MpComputerStatus | Select-Object -Property AMRunningMode, AMServiceEnabled, AntivirusEnabled. Confirm that AMRunningMode is not 'Normal' and that AMServiceEnabled and AntivirusEnabled are 'False'.
3. On the same device, run: Get-WmiObject -Namespace root\Microsoft\Windows\AdvancedThreatProtection -Class MSFT_MpWDATPStatus | Select-Object -Property OffboardingState. Confirm OffboardingState is '1' (offboarded).
4. In the Microsoft Defender portal (security.microsoft.com), navigate to Assets > Devices. Search for the device and confirm its status shows 'Inactive' or 'Offboarded'.

## Rollback
1. In the Microsoft Intune admin center, navigate to Devices > By platform > Windows > Manage Devices > Configuration. Select the custom offboarding policy and click Delete to remove the policy assignment from all devices.
2. Alternatively, create a new custom configuration policy with the OMA-URI ./Device/Vendor/MSFT/WindowsAdvancedThreatProtection/Onboarding and set the value to the onboarding package content (obtained from the Defender portal under Settings > Endpoints > Device management > Onboarding). Assign this policy to the affected devices.
3. On a target device, run: Get-WmiObject -Namespace root\Microsoft\Windows\AdvancedThreatProtection -Class MSFT_MpWDATPStatus | Select-Object -Property OffboardingState. Confirm OffboardingState is '0' (onboarded).
4. Verify the device appears as 'Active' in the Defender portal under Assets > Devices.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-mdm>
