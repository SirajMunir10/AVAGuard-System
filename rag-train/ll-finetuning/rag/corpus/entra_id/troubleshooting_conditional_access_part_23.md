# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
Why does a Conditional Access policy requiring a compliant device fail when using a supported browser in private mode or with cookies disabled?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Device-based Conditional Access policy requiring compliant device

## Symptoms
- Device check fails when using a supported browser in private mode
- Device check fails when cookies are disabled

## Error Codes
N/A

## Root Causes
1. Browser is running in private mode
2. Cookies are disabled in the browser

## Remediation Steps
1. Ensure the browser is not running in private mode
2. Enable cookies in the browser settings

## Validation
1. Open a supported browser (e.g., Microsoft Edge, Chrome) in normal (non-private) mode. 2. Ensure cookies are enabled in browser settings. 3. Navigate to a resource protected by the Conditional Access policy requiring a compliant device. 4. Sign in with a test user account that has a compliant device. 5. Confirm that the device check passes and access is granted. 6. Repeat the test with the same browser in private/incognito mode and verify that the device check now fails. 7. Repeat the test with cookies disabled and verify that the device check fails.

## Rollback
1. If the remediation causes unexpected access issues, re-enable private browsing or disable cookies in the browser settings for the affected users. 2. Temporarily modify the Conditional Access policy to exclude the affected users or devices until the browser configuration is corrected. 3. Monitor sign-in logs for device compliance failures and adjust policy assignments as needed. 4. Communicate to users that private browsing or disabled cookies may cause access failures and advise them to use normal browsing mode with cookies enabled.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
