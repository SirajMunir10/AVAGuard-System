# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I scope a DLP policy to apply only to kiosk devices used by multiple users?

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
1. Set 'All users and groups'.
2. Set either 'All devices and device groups' with 'Exclude devices and device groups' and add the devices to be excluded, or 'Specific devices and device groups' and add the devices to be included.

## Validation
1. Confirm that the DLP policy is applied to the intended kiosk devices by running the following PowerShell command: Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List Name, Mode, ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation, EndpointDlpLocation, EndpointDlpDeviceGroups. 2. Verify that the policy's device scope includes only the kiosk devices by checking the EndpointDlpDeviceGroups property. 3. Test the policy by signing into a kiosk device and attempting a restricted action (e.g., copying sensitive data to USB) to ensure the policy blocks it. 4. Confirm that non-kiosk devices are not affected by performing the same test on a standard device and verifying the action is allowed.

## Rollback
1. Remove the device scoping by editing the DLP policy: Set-DlpCompliancePolicy -Identity "PolicyName" -EndpointDlpDeviceGroups @{Remove="KioskDeviceGroup1","KioskDeviceGroup2"}. 2. Alternatively, set the policy to apply to all devices: Set-DlpCompliancePolicy -Identity "PolicyName" -EndpointDlpDeviceGroups @{Add="All"}. 3. If the policy was newly created, delete it: Remove-DlpCompliancePolicy -Identity "PolicyName". 4. Monitor for any residual effects by checking audit logs for policy violations.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
