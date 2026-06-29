# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure Antivirus policy for cross-platform management in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows devices use built-in Microsoft Defender Antivirus; macOS devices use Microsoft Defender for Endpoint

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Windows devices, use the built-in Microsoft Defender Antivirus.
2. For macOS devices, use Microsoft Defender for Endpoint.
3. Ensure Tamper protection is available on Windows and macOS with Defender for Endpoint P1 or greater licenses.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Antivirus. Verify that a policy exists for Windows devices using the 'Microsoft Defender Antivirus' profile and for macOS devices using the 'Microsoft Defender for Endpoint' profile. 2. For each policy, confirm the assignment is correctly targeting the intended device groups. 3. On a Windows test device, run 'Get-MpComputerStatus' in PowerShell to confirm that Microsoft Defender Antivirus is active and tamper protection is enabled. 4. On a macOS test device, run 'mdatp health' in Terminal to verify that Microsoft Defender for Endpoint is running and tamper protection is on.

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint security > Antivirus. Select the newly created antivirus policy and choose 'Delete' to remove it. 2. If the policy was assigned to groups, remove the assignments before deletion to avoid conflicts. 3. On Windows devices, if tamper protection was enabled via the policy, it will revert to the previous state after policy removal; verify with 'Get-MpComputerStatus'. 4. On macOS devices, if the policy configured Defender for Endpoint settings, removal will revert to default settings; verify with 'mdatp health'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
