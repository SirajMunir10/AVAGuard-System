# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure a Conditional Access policy that requires compliant devices using Microsoft Intune compliance policies?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with Intune
- **Configuration:** Devices must be enrolled in Intune and have compliance policies assigned

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the information returned from devices to identify devices that meet compliance requirements such as: Requiring a PIN to unlock, Requiring device encryption, Requiring a minimum or maximum operating system version, Requiring a device isn't jailbroken or rooted.
2. Policy compliance information is sent to Microsoft Entra ID where Conditional Access decides to grant or block access to resources.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies and select the policy you created. 3. Under Assignments > Users and groups, confirm the correct users/groups are included. 4. Under Cloud apps or actions, confirm the target apps are selected. 5. Under Conditions > Device platforms, verify the platform configuration. 6. Under Access controls > Grant, confirm 'Require device to be marked as compliant' is selected and 'Require all the selected controls' is chosen. 7. Use the 'What If' tool to simulate a sign-in for a test user: a. Select the user, cloud app, and device platform. b. Confirm the policy applies and the grant control shows 'Require compliant device'. 8. On a test device enrolled in Intune, verify it shows as compliant in the Microsoft Intune admin center under Devices > All devices. 9. Attempt to access the target cloud app from the compliant device and confirm access is granted. 10. Attempt access from a non-compliant device and confirm access is blocked with a message indicating the device is not compliant.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy you created and select it. 4. Set the policy state to 'Off' to disable it immediately. 5. Alternatively, delete the policy by selecting 'Delete' from the policy's context menu. 6. If you need to restore a previous policy configuration, use the 'Audit logs' to find the original policy settings and recreate them manually. 7. Verify that users can access resources without the compliant device requirement by testing access from a non-compliant device.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
- <https://learn.microsoft.com/en-us/mem/intune/protect/create-compliance-policy>
- <https://learn.microsoft.com/en-us/entra/identity/devices/hybrid-join-plan>
