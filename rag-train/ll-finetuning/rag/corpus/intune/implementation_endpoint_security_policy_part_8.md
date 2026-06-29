# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure Application Control policy in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Integration with Defender's application tagging and trust mechanisms

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use managed installers with integration of Defender's application tagging and trust mechanisms.
2. Enforce policy using Defender infrastructure for application control decisions.

## Validation
1. Confirm that the Application Control policy is assigned to the target device group by navigating to Endpoint Security > Application Control in the Microsoft Intune admin center and verifying the policy assignment status. 2. On a managed Windows device, run the command 'Get-MpComputerStatus | Select-Object -Property AppControl*' in PowerShell to verify that the Application Control policy is active and that the 'AppControlPolicies' property shows the expected policy name. 3. Check the Microsoft Defender for Endpoint portal for the device to confirm that the application control policy is enforced and that trusted applications are tagged correctly based on the managed installer and trust mechanisms.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Application Control, select the policy that was implemented, and choose 'Delete' to remove the policy assignment. 2. Alternatively, modify the policy assignment to exclude the affected device group by editing the policy's 'Assignments' tab and removing the group. 3. On a managed Windows device, run the command 'Get-MpComputerStatus | Select-Object -Property AppControl*' to confirm that the Application Control policy is no longer active. 4. If the policy was enforced via Defender infrastructure, verify in the Microsoft Defender for Endpoint portal that the device's application control state has reverted to the previous baseline.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
