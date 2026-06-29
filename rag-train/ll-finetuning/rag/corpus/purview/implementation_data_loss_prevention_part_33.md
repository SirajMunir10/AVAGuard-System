# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I scope a DLP policy to control data leakage by specific users on all devices?

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
1. Set either 'All users and groups' with 'Exclude users and groups' and add the users to be excluded, or 'Specific users and groups' and add the users to be included.
2. Set 'All devices and device groups'.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was scoped. 3. Under 'Locations', confirm that 'Devices' is toggled on. 4. Under 'Users and groups', verify that either 'All users and groups' with the correct excluded users, or 'Specific users and groups' with the correct included users is selected. 5. Under 'Devices and device groups', confirm that 'All devices and device groups' is selected. 6. Use the DLP policy test feature (if available) to simulate a data leakage event from a user in the scope on a supported device (Windows 10/11, macOS with build 101.25072 or higher, excluding Microsoft Entra registered devices) and confirm the policy action is triggered.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was scoped. 3. Under 'Users and groups', revert to the original user scope (e.g., change from 'Specific users and groups' to 'All users and groups' with no exclusions, or remove the exclusions). 4. Under 'Devices and device groups', change from 'All devices and device groups' to the original device scope (e.g., specific device groups or individual devices). 5. Save the policy and confirm the change is applied. 6. If the policy was newly created, delete the policy entirely.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
