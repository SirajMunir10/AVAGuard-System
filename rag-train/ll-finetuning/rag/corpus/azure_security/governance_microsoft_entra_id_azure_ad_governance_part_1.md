# Governance: Microsoft Entra ID (Azure AD) Governance (53000 â€“ DeviceNotCompliant (documented in Microsoft Entra ID sign-in error codes))

**Domain:** Azure
**Subdomain:** Microsoft Entra ID (Azure AD) Governance
**Incident Type:** Governance

## Scenario / Query
A user reports that they cannot access the Azure portal because their account is blocked. The tenant administrator discovers that the user's sign-in was blocked by a Conditional Access policy that requires multi-factor authentication (MFA) and device compliance, but the user's device is not enrolled in Microsoft Intune. How should the administrator resolve this governance gap?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft Entra ID P2)
- **Configuration:** Conditional Access policy requiring MFA and compliant device for all cloud app access; device compliance policy configured in Microsoft Intune

## Symptoms
- User receives sign-in block message: 'Your sign-in was successful but your admin requires the device to be managed by Microsoft Intune.'
- User cannot access Azure portal or any cloud app protected by the Conditional Access policy

## Error Codes
- `53000 â€“ DeviceNotCompliant (documented in Microsoft Entra ID sign-in error codes)`

## Root Causes
1. User's device is not enrolled in Microsoft Intune or does not meet compliance policy requirements
2. Conditional Access policy requires device compliance but no exception or grace period is configured for unmanaged devices

## Remediation Steps
1. Enroll the user's device in Microsoft Intune by following the steps in 'Enroll your device in Intune' documentation.
2. Ensure the device meets the compliance policy (e.g., OS version, encryption, antivirus).
3. If the device cannot be enrolled, create a Conditional Access policy exception for the user using a 'Filter for devices' or exclude the user from the policy temporarily, as documented in 'Conditional Access: Require compliant or hybrid Azure AD joined device'.
4. Alternatively, require the user to use Microsoft Authenticator app for MFA and access via a compliant device.

## Validation
After device enrollment and compliance check, the user should be able to sign in without the block. Verify by checking the user's sign-in logs in Microsoft Entra ID for 'Success' with DeviceCompliant = true.

## Rollback
Remove the user from any exclusion group or delete the temporary exception policy. If the device was enrolled, unenroll it via Intune console.

## References
- Microsoft Entra ID sign-in error codes: https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if
- Device compliance policy: https://learn.microsoft.com/en-us/mem/intune/protect/device-compliance-get-started
