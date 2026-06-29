# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure device scoping for a Microsoft Purview DLP policy to target specific users on specific devices?

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
1. For 'All users on all onboarded devices': Set 'All users and groups' and 'All devices and device groups'.
2. For 'All users on specific devices': Set 'All users and groups' with either 'Exclude devices and device groups' (adding devices to exclude) or 'Specific devices and device groups' (adding devices to include).
3. For 'Specific users on all onboarded devices': Set either 'All users and groups' with 'Exclude users and groups' (adding users to exclude) or 'Specific users and groups' (adding users to include), and set 'All devices and device groups'.
4. For 'Specific users on specific devices': Set 'Specific users and groups' and 'Specific devices and device groups'.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy you configured. 3. Under 'Locations', confirm that 'Devices' is toggled on. 4. Under 'Device groups', verify the scoping settings match your intended target (e.g., 'All users and groups' with 'Specific devices and device groups' for specific devices). 5. Use the 'Test' feature in the policy wizard to simulate a DLP rule on a targeted device and user. 6. On a targeted device, trigger a DLP rule (e.g., copy sensitive data to USB) and confirm the policy action (e.g., block) is enforced. 7. On a non-targeted device, trigger the same action and confirm the policy does not apply.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy you modified. 3. Under 'Locations' > 'Devices', revert the device scoping to the previous configuration (e.g., change from 'Specific devices and device groups' to 'All devices and device groups' or remove exclusions). 4. If the policy was newly created, delete the policy entirely. 5. If the policy was edited, restore the previous version using the 'Version history' option in the policy details pane. 6. Verify the rollback by repeating validation steps to ensure the policy no longer applies to unintended users or devices.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
