# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
Why is a device not being marked as compliant for Conditional Access even though it is enrolled in Intune?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with Intune
- **Configuration:** Conditional Access policy with 'Require device to be marked as compliant'

## Symptoms
- Device is not marked as compliant in Conditional Access policies.
- User is blocked from accessing resources despite device being enrolled in Intune.

## Error Codes
N/A

## Root Causes
1. Device is not registered in Microsoft Entra ID before being marked as compliant.
2. Device operating system is not supported (only Windows 10+, iOS, Android, macOS, and Linux Ubuntu are supported).
3. Microsoft Edge in InPrivate mode on Windows is considered as a noncompliant device.
4. For agent user scenarios, device compliance signals might not be available if the session runs directly in cloud infrastructure.
5. On iOS and macOS, some browsers require additional configuration to present the client certificate due to transition of device identity key storage to Apple Secure Enclave.

## Remediation Steps
1. Verify the device is registered in Microsoft Entra ID.
2. Check that the device operating system is Windows 10+, iOS, Android, macOS, or Linux Ubuntu.
3. Ensure the user is not using Microsoft Edge in InPrivate mode on Windows.
4. For agent user scenarios, combine the control with scoping conditions so the policy applies only to endpoint-based sessions.
5. On iOS and macOS, configure browsers to present the client certificate as per browser-specific requirements.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Identity > Devices > All devices. 3. Locate the device in question and confirm its 'Registered' status is 'Yes'. 4. Verify the device's operating system is one of: Windows 10+, iOS, Android, macOS, or Linux Ubuntu. 5. Check the Conditional Access policy that requires device compliance and ensure the 'Require device to be marked as compliant' grant control is selected. 6. For Windows devices, confirm the user is not using Microsoft Edge in InPrivate mode by reviewing browser logs or testing with a standard session. 7. For iOS/macOS, verify the browser is configured to present the client certificate (e.g., Safari requires manual certificate selection). 8. For agent user scenarios, review the policy's conditions to ensure it is scoped to endpoint-based sessions (e.g., filter for device platforms).

## Rollback
1. If the device is not registered in Microsoft Entra ID, initiate device registration via Settings > Accounts > Access work or school > Connect. 2. If the operating system is unsupported, upgrade the device to a supported OS or replace it. 3. If InPrivate mode is causing noncompliance, instruct the user to use a standard Microsoft Edge session. 4. For agent user scenarios, modify the Conditional Access policy to remove or adjust scoping conditions that restrict to endpoint-based sessions. 5. For iOS/macOS certificate issues, revert browser configuration to default settings and re-enroll the device in Intune to regenerate certificates.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
