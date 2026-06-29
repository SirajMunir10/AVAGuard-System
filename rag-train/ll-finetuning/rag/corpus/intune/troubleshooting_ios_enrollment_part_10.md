# Troubleshooting: iOS Enrollment

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve authentication not redirecting to the government cloud for iOS enrollment?

## Environment Context
- **Tenant Type:** Government
- **Configuration:** iOS Company Portal Cloud setting

## Symptoms
- Government users signing in from another device are redirected to the public cloud for authentication rather than the government cloud

## Error Codes
N/A

## Root Causes
1. Microsoft Entra ID doesn't yet support redirecting to the government cloud when signing in from another device

## Remediation Steps
1. Open the Settings app and select Company Portal
2. In the Company Portal settings, select Cloud
3. Set the Cloud to Government

## Validation
1. On the iOS device, open the Settings app and tap Company Portal. 2. Tap Cloud and verify the setting shows 'Government'. 3. Close and reopen the Company Portal app, then attempt to sign in. 4. Confirm the authentication redirects to the government cloud (e.g., login.microsoftonline.us) instead of the public cloud. 5. Check that enrollment proceeds without the previous redirection error.

## Rollback
1. On the iOS device, open the Settings app and tap Company Portal. 2. Tap Cloud and change the setting back to 'Automatic' or 'Public' (the previous value). 3. Close and reopen the Company Portal app. 4. Verify that authentication redirects to the public cloud as before. 5. If the issue persists, reinstall the Company Portal app and re-enroll the device.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
