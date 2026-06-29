# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure a Conditional Access policy requiring compliant devices without blocking Intune enrollment?

## Environment Context
- **Tenant Type:** Entra ID tenant with Intune
- **Configuration:** Conditional Access policy with 'Require device to be marked as compliant' control

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enroll new devices to Intune even if you select 'Require device to be marked as compliant' for 'All users' and 'All resources' (formerly 'All cloud apps') using the previous steps.
2. Note: 'Require device to be marked as compliant' control doesn't block Intune enrollment and the access to the Microsoft Intune Web Company Portal application.

## Validation
1. Sign in as a test user who does not have a compliant device. 2. Attempt to access the Microsoft Intune Web Company Portal (https://portal.manage.microsoft.com). 3. Verify that the user is allowed to enroll the device (i.e., the enrollment process proceeds). 4. Attempt to access any other cloud app (e.g., Exchange Online, SharePoint Online) from the non-compliant device. 5. Verify that access is blocked with a message indicating the device is not compliant. 6. Use the Conditional Access 'What If' tool in the Entra admin center: select the test user, target app (e.g., Microsoft Intune Web Company Portal), and device state (non-compliant). Confirm the policy evaluates to 'Grant: Require compliant device' but does not block the Company Portal app.

## Rollback
1. In the Entra admin center, navigate to Protection > Conditional Access > Policies. 2. Locate the policy that includes 'Require device to be marked as compliant'. 3. Set the policy state to 'Off' to disable it. 4. Alternatively, remove the 'Require device to be marked as compliant' grant control from the policy. 5. If the policy was scoped to 'All users' and 'All resources', change the scope to a test group of users or a specific app to limit impact. 6. Wait 5–10 minutes for the changes to propagate, then verify that non-compliant devices can access all cloud apps without restriction.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
