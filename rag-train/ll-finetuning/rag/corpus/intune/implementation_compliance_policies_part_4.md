# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How to configure Valid operating system builds in Intune compliance policy to enforce specific patch levels across multiple Windows releases?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** Compliance policy with Valid operating system builds setting

## Symptoms
- Device with OS build outside specified ranges is reported as noncompliant
- Compliance remediation message only shows the first OS version range specified in the policy

## Error Codes
N/A

## Root Causes
1. Device OS build does not fall within any of the defined minimum and maximum OS build ranges
2. Technical limitation: only the first OS version range is shown in the compliance remediation message

## Remediation Steps
1. Specify a list of minimum and maximum OS build ranges using major.minor.build.revision format
2. Each entry requires a description, minimum OS version, and maximum OS version
3. Largest supported value for each field is 65535 (e.g., 65535.65535.65535.65535)
4. Export the list as a CSV file after defining entries
5. Document acceptable OS version ranges for managed devices in your organization

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies and select the policy with Valid operating system builds configured. 2. Under Compliance settings > Windows Health, confirm that the Valid operating system builds list contains the expected ranges with correct major.minor.build.revision values. 3. Use Graph API to retrieve the policy: GET https://graph.microsoft.com/beta/deviceManagement/deviceCompliancePolicies/{policyId} and verify the 'validOperatingSystemBuildRanges' property includes all intended entries. 4. On a test device with an OS build within one of the defined ranges, run 'dsregcmd /status' and confirm the device shows as compliant in the Intune console. 5. On a test device with an OS build outside all defined ranges, confirm it is reported as noncompliant and that the remediation message displays only the first range (expected behavior).

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies and select the policy with Valid operating system builds configured. 2. Under Compliance settings > Windows Health, clear the Valid operating system builds list by removing all entries. 3. Alternatively, replace the list with the previous known-good set of ranges (if backed up) or set the policy to not use Valid operating system builds. 4. Use Graph API to update the policy: PATCH https://graph.microsoft.com/beta/deviceManagement/deviceCompliancePolicies/{policyId} with an empty 'validOperatingSystemBuildRanges' array or the previous values. 5. Force a sync on affected devices by running 'SyncML' via 'Start-DeviceSync' or from the Intune console. 6. Verify that devices previously noncompliant due to the build ranges become compliant again.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
