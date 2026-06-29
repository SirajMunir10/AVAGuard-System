# Troubleshooting: Windows Enrollment

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Enrollment Status Page (ESP) timeout before sign-in screen loads during Windows enrollment?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) tenant with Intune
- **Configuration:** ESP tracking Microsoft Store for Business apps; Conditional Access policy with 'Require device to be marked as compliant' control applied to All Cloud apps and Windows

## Symptoms
- Enrollment Status Page (ESP) times out before the sign in screen can load

## Error Codes
N/A

## Root Causes
1. All the following conditions are true: ESP is used to track Microsoft Store for Business apps; a Microsoft Entra Conditional Access policy uses the 'Require device to be marked as compliant' control; the policy applies to All Cloud apps and Windows

## Remediation Steps
1. Target your Intune compliance policies to devices
2. Make sure that compliance can be determined before the user logs on
3. Use offline licensing for store apps so the Windows client does not have to check with the Microsoft Store before determining device compliance

## Validation
1. Verify that Intune compliance policies are assigned to the affected device group: Sign in to Microsoft Intune admin center > Devices > Compliance policies > select the policy > Properties > Assignments > confirm the device group is included.
2. Confirm compliance evaluation can occur before user logon: In the same compliance policy, under 'Settings' > 'Device Health', ensure 'Require BitLocker' or other pre-logon checks are not set to 'Not configured' if they block compliance. Check that the device has a valid compliance status in Intune > Devices > All devices > select device > Device compliance.
3. Verify Microsoft Store for Business apps use offline licensing: In Microsoft Store for Business portal > Manage > Apps & software > select the app > License type > confirm 'Offline' is selected. In Intune > Apps > All apps > select the app > Properties > App information > ensure 'Offline' is selected under 'License type'.
4. Test enrollment: Perform a new Windows enrollment on a test device and observe the Enrollment Status Page (ESP). Confirm the ESP completes without timeout and the sign-in screen loads within the expected time.

## Rollback
1. Revert compliance policy targeting: In Intune admin center > Devices > Compliance policies > select the policy > Properties > Assignments > remove the device group from 'Included groups' or add to 'Excluded groups'.
2. Restore pre-logon compliance checks: In the same compliance policy > Settings > Device Health > set 'Require BitLocker' or other settings back to 'Not configured' if they were changed.
3. Switch Microsoft Store for Business apps back to online licensing: In Microsoft Store for Business portal > Manage > Apps & software > select the app > License type > change to 'Online'. In Intune > Apps > All apps > select the app > Properties > App information > change 'License type' to 'Online'.
4. If issues persist, remove the Conditional Access policy requiring compliant device: Sign in to Microsoft Entra admin center > Protection > Conditional Access > select the policy > Properties > set 'Enable policy' to 'Off' or delete the policy.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
