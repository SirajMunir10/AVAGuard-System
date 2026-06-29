# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I scope a DLP policy to specific user accounts on specific devices for payroll check printing?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Device scoping for DLP policies requires build 101.25072 or higher for macOS support. Does not support Microsoft Entra registered devices.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set 'Specific users and groups'.
2. Set 'Specific devices and device groups'.

## Validation
1. Verify that the DLP policy is assigned to the correct user accounts: Run `Get-DlpCompliancePolicy -Identity "Payroll Check Printing Policy" | Format-List AssignedTo` in Exchange Online PowerShell. Confirm the output lists the intended user accounts. 2. Verify that the policy is scoped to the correct devices: Run `Get-DlpCompliancePolicy -Identity "Payroll Check Printing Policy" | Format-List DeviceGroups` and confirm the output includes the intended device group names. 3. Confirm that the devices meet the minimum build requirement: On each macOS device, go to Apple menu > About This Mac and verify the build number is 101.25072 or higher. 4. Ensure devices are not Microsoft Entra registered: Run `dsregcmd /status` on each Windows device and confirm the output does not show "AzureAdJoined : YES" with "DomainJoined : NO". For macOS, verify the device is joined to Microsoft Entra ID via the Company Portal app or by checking the device's management profile.

## Rollback
1. Remove the user scoping: Run `Set-DlpCompliancePolicy -Identity "Payroll Check Printing Policy" -AssignedTo @()` in Exchange Online PowerShell to clear the specific user assignments. 2. Remove the device scoping: Run `Set-DlpCompliancePolicy -Identity "Payroll Check Printing Policy" -DeviceGroups @()` to clear the specific device group assignments. 3. If the policy was newly created, delete it entirely: Run `Remove-DlpCompliancePolicy -Identity "Payroll Check Printing Policy"`. 4. If the policy was modified, revert to the previous configuration by restoring from a backup or re-applying the original settings using the same cmdlets with the original values.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
