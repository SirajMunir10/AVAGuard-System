# Implementation: Endpoint detection and response

**Domain:** Intune
**Subdomain:** Endpoint detection and response
**Incident Type:** Implementation

## Scenario / Query
How to offboard a Windows device from Microsoft Defender for Endpoint using an EDR policy in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint security > Endpoint detection and response (EDR) policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the navigation pane, select Endpoint security > Manage > Endpoint detection and response.
2. Under Endpoint detection and response (EDR) policies, select Create policy.
3. In the Create a profile slide out, select Windows as Platform and Endpoint detection and response and select Create.
4. Enter a value for Name and select Next.
5. Under Configuration settings, select Offboard for the setting Microsoft Defender for Endpoint client configuration package type.
6. Copy the value from the content of the WindowsDefenderATP_valid_until_YYYY-MM-DD offboarding file and paste it in the Offboarding (Device) setting. Then select Next.
7. Specify any scope tags if needed, make the appropriate group assignments and on the Review + create step, select Create.

## Validation
1. In Microsoft Intune, navigate to Endpoint security > Manage > Endpoint detection and response and select the newly created EDR policy. 2. Confirm the policy shows 'Succeeded' status for assigned devices. 3. On a target Windows device, open PowerShell as Administrator and run: Get-MpComputerStatus | select AMRunningMode. Verify the output shows 'Passive' or 'Off' (not 'Active'). 4. On the same device, run: Get-MpPreference | select DisableRealtimeMonitoring. Confirm the value is 'True' (real-time protection is off). 5. In the Microsoft 365 Defender portal (https://security.microsoft.com), go to Assets > Devices and search for the device. Confirm its status shows 'Inactive' or 'Offboarded'.

## Rollback
1. In Microsoft Intune, navigate to Endpoint security > Manage > Endpoint detection and response and select the offboarding policy. 2. Change the assignment to 'Not assigned' or delete the policy. 3. Create a new EDR policy with the same name but set 'Microsoft Defender for Endpoint client configuration package type' to 'Onboard' and paste the onboarding package content into the 'Onboarding (Device)' setting. 4. Assign the new onboarding policy to the same device groups. 5. On a target Windows device, run: Get-MpComputerStatus | select AMRunningMode. Verify the output shows 'Active'. 6. Confirm the device reappears in the Microsoft 365 Defender portal with an 'Active' status.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-mdm>
