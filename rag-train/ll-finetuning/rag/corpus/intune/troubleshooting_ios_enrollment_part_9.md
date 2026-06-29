# Troubleshooting: iOS Enrollment

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
ADE enrollment stuck at user login when multifactor authentication is enabled

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** ADE enrollment profile with authentication method set to Setup Assistant (legacy)

## Symptoms
- Initial setup sticks after entering credentials on an ADE-managed device

## Error Codes
N/A

## Root Causes
1. Multifactor authentication (MFA) is enabled and does not work during enrollment on ADE devices when the authentication method is set to Setup Assistant (legacy)

## Remediation Steps
1. Disable MFA, then re-enroll the device
2. Alternatively, change the authentication method to Setup Assistant with modern authentication

## Validation
1. Verify that MFA is disabled for the affected user or group in Azure AD (e.g., via Conditional Access policy).
2. Confirm the enrollment profile's authentication method is set to 'Setup Assistant with modern authentication' (not 'Setup Assistant (legacy)').
3. On the ADE-managed iOS device, perform a factory reset and re-initiate enrollment.
4. Observe that the device completes the Setup Assistant without being prompted for MFA credentials and reaches the Managed Home Screen or company portal.
5. Check Intune console: navigate to Devices > iOS/iPadOS > Enrollment status and confirm the device shows 'Enrolled' and is compliant.

## Rollback
1. Re-enable MFA for the affected user or group in Azure AD (e.g., reapply the Conditional Access policy requiring MFA).
2. Change the enrollment profile's authentication method back to 'Setup Assistant (legacy)'.
3. On the device, perform a factory reset and re-initiate enrollment.
4. Confirm the device again gets stuck at the user login step due to MFA, reproducing the original issue.
5. If the device is already enrolled and functional, no further rollback is needed; document the change for future reference.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
