# Incident Response: Incident Response

**Domain:** Intune
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I respond to a detected malicious device enrollment in Intune where a non-compliant device is granted access to corporate resources?

## Environment Context
- **Tenant Type:** Microsoft Intune standalone or co-managed with Configuration Manager
- **Configuration:** Conditional Access policies rely on Intune compliance status; device enrollment is open to all users

## Symptoms
- A device that does not meet compliance policies is able to access corporate email and data
- Intune reports the device as non-compliant, but Conditional Access does not block access
- Security alerts indicate anomalous enrollment from an unknown device

## Error Codes
N/A

## Root Causes
1. Conditional Access policy is not configured to require compliant devices
2. Device compliance policy is not assigned to the affected user or device group
3. The device was enrolled using a user account that bypasses Conditional Access due to policy exclusion

## Remediation Steps
1. Immediately block the non-compliant device from accessing resources by using Intune remote actions: select the device in Intune console, choose 'Retire' or 'Wipe' as appropriate
2. Review and update Conditional Access policies to require 'Require device to be marked as compliant' for all cloud apps
3. Ensure the device compliance policy is assigned to the correct user/device groups and that it evaluates the necessary settings (e.g., OS version, encryption, jailbreak detection)
4. Audit enrollment logs in Azure AD to identify the user and device, and revoke user sessions if necessary
5. Consider enabling 'Device enrollment restrictions' in Intune to block enrollment from untrusted platforms or unapproved device models

## Validation
Verify that the device no longer appears in Intune's list of compliant devices and that Conditional Access blocks access for that device. Use the 'What If' tool in Azure AD Conditional Access to test the policy against the affected user and device.

## Rollback
If the device was incorrectly blocked, re-enroll the device after ensuring compliance policies are correctly assigned and the device meets requirements. Use Intune 'Retire' action to remove the device and allow re-enrollment.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/respond-to-compromised-device>
- <https://learn.microsoft.com/en-us/mem/intune/protect/conditional-access-intune-common-ways-use>
