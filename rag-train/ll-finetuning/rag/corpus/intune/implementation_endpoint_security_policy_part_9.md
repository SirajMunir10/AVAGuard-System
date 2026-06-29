# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How to implement Defender integration for unified security posture across endpoint security policies and threat detection?

## Environment Context
- **Tenant Type:** Microsoft Intune with Microsoft Defender for Endpoint
- **Configuration:** Endpoint security policies, Defender agent

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Centralized visibility across endpoint security policies and threat detection
2. Combined device compliance and threat intelligence data
3. Consistent security policy deployment across Windows, macOS, and Linux through Defender agent
4. Manage select endpoint security policies (Antivirus, Attack Surface Reduction, EDR) on non-enrolled devices through the Defender portal

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Overview and verify that the 'Microsoft Defender for Endpoint' connector status shows 'Enabled' and 'Connected'. 2. Go to Endpoint security > Antivirus, Attack surface reduction, and Endpoint detection and response; confirm that policies are assigned to the correct device groups and that the policy status for Windows, macOS, and Linux devices shows 'Succeeded'. 3. In the Microsoft 365 Defender portal (security.microsoft.com), go to Assets > Devices and verify that devices managed by Intune appear with a 'Managed by' value of 'Microsoft Intune' and that their Defender sensor health is 'Active'. 4. From a test device, run 'Get-MpComputerStatus' in PowerShell and confirm that 'AMServiceEnabled', 'AntivirusEnabled', and 'DefenderSignaturesOutOfDate' are correctly reflecting the policy settings. 5. In the Defender portal, go to Endpoints > Vulnerability management and confirm that threat and vulnerability data from the devices is populated and consistent with Intune compliance policies.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Microsoft Defender for Endpoint and set the connector to 'Disabled' to disconnect the integration. 2. Delete or disable any endpoint security policies (Antivirus, Attack Surface Reduction, EDR) that were created specifically for non-enrolled devices via the Defender portal by going to Endpoints > Configuration management > Endpoint security policies and removing the assignments. 3. Revert any changes made to device compliance policies that reference Defender for Endpoint threat levels by editing the policy in Intune > Devices > Compliance policies and removing the 'Require the device to be at or under the machine risk score' setting. 4. On affected devices, reset the Defender agent configuration by running 'Set-MpPreference -DisableRealtimeMonitoring $false' and 'Update-MpSignature' in PowerShell to restore default protection settings. 5. Verify that devices return to their previous security posture by checking the Defender portal and Intune console for any remaining policy conflicts or errors.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
