# Implementation: Custom configuration policy

**Domain:** Intune
**Subdomain:** Custom configuration policy
**Incident Type:** Implementation

## Scenario / Query
How to offboard a Windows device from Microsoft Defender for Endpoint using a custom configuration policy in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Devices > By platform > Windows > Manage Devices > Configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the navigation pane, select Devices > By platform > Windows > Manage Devices > Configuration.
2. Under Policies select Create > New Policy.
3. In the Create a profile slide out, select Windows 10 and later as Platform and Templates as Profile Type.
4. Under Template Name, select the Custom template and select Create.
5. Enter a value for Name and select Next.
6. Under Configuration settings, select Add and use the following OMA-URI settings: - Name: Provide a name - OMA-URI: ./Device/Vendor/MSFT/WindowsAdvancedThreatProtection/Offboarding - Date type: String - Value: Copy and paste the value from the content of the WindowsDefenderATP_valid_until_YYYY-MM-DD offboarding file.
7. Make the appropriate group assignments, applicability rules, and on the Review + create step, select Create.

## Validation
1. On a Windows device that received the policy, open the Microsoft Defender for Endpoint client and verify the device shows as 'Offboarded' or 'Inactive'. 2. Run the following PowerShell command as Administrator: Get-MpComputerStatus | Select-Object -Property AMRunningMode, AMProductVersion, AntivirusEnabled. Confirm that AMRunningMode is 'Passive' or 'Disabled' and AntivirusEnabled is 'False'. 3. In the Microsoft 365 Defender portal, navigate to Assets > Devices, search for the device, and confirm its status is 'Offboarded' or 'Inactive'. 4. On the device, check the registry key HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status and verify the value 'OnboardingState' is 0.

## Rollback
1. In the Microsoft Intune admin center, navigate to Devices > By platform > Windows > Manage Devices > Configuration. 2. Locate the custom configuration policy created for offboarding and select it. 3. Select Properties, then under Configuration settings, edit the OMA-URI setting for 'Offboarding'. 4. Change the OMA-URI value to: ./Device/Vendor/MSFT/WindowsAdvancedThreatProtection/Onboarding and set the Data type to String. 5. Obtain the onboarding blob from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding) and paste it as the Value. 6. Select Review + save to apply the change. 7. On the target device, run the command: Get-MpComputerStatus | Select-Object -Property AMRunningMode to confirm it returns 'Normal'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-mdm>
