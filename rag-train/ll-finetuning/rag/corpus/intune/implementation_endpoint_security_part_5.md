# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to configure Defender for Endpoint onboarding in Intune for disconnected environments?

## Environment Context
- **Tenant Type:** Intune and Defender for Endpoint connected
- **Configuration:** Defender for Endpoint client configuration package type

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set Defender for Endpoint client configuration package type to Auto from connector (recommended) to use the automatic onboarding package from Microsoft Defender for Endpoint.
2. For disconnected environments, paste the WindowsDefenderATP.onboarding blob content into the Onboard field.
3. Configure Sample Sharing: set to All to enable automatic sample sharing for enhanced threat detection, or None to disable sample sharing.
4. Note: Telemetry Reporting Frequency is deprecated and doesn't affect new devices; the setting remains visible for older policy compatibility.
5. Add scope tags if needed, then select Next.
6. In Assignments, select device groups that receive this profile. Device groups are recommended for immediate deployment; user groups require user sign-in before policy applies.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Endpoint detection and response. Select the policy you configured and verify that 'Defender for Endpoint client configuration package type' is set to 'Auto from connector' (or 'Onboarding blob' for disconnected environments). 2. Confirm that 'Sample Sharing' is set to 'All' or 'None' as intended. 3. Under Assignments, verify the policy is assigned to the correct device groups. 4. On a target Windows device, open Windows Security > Device security > Core isolation details and confirm that 'Microsoft Defender for Endpoint' shows as 'On'. Alternatively, run 'Get-MpComputerStatus | Select-Object AMRunningMode' in PowerShell and verify the output is 'Normal' or 'Passive' depending on your configuration.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Endpoint detection and response. Select the policy you configured and either delete it or change the settings back to the previous values. 2. If you used an onboarding blob, remove the blob content from the 'Onboard' field and set the package type to 'Auto from connector' (or revert to the previous setting). 3. Change 'Sample Sharing' back to the previous setting. 4. Remove the policy assignment from any device groups by editing the assignment and removing the groups. 5. On affected devices, run 'Get-MpComputerStatus | Select-Object AMRunningMode' to confirm the Defender for Endpoint state reverts to the previous mode. If needed, manually offboard the device using the offboarding script from the Microsoft Defender portal.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
