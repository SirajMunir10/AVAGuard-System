# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure 'Require approved client app' grant in Conditional Access policies for iOS and Android devices?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Conditional Access
- **Configuration:** Device platform condition set to iOS and Android

## Symptoms
- User is redirected to app store to install broker app if not present

## Error Codes
N/A

## Root Causes
1. Device must be registered in Microsoft Entra ID using a broker app
2. Broker app required: Microsoft Authenticator for iOS, or Microsoft Authenticator or Microsoft Company Portal for Android

## Remediation Steps
1. Ensure device platform condition is set to iOS and Android only
2. Ensure broker app (Microsoft Authenticator for iOS, or Microsoft Authenticator or Microsoft Company Portal for Android) is installed on the device
3. If broker app is not installed, user is redirected to appropriate app store to install it

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that includes the 'Require approved client app' grant. 4. Under Assignments > Conditions > Device platforms, confirm that 'iOS' and 'Android' are selected and no other platforms are included. 5. Under Access controls > Grant, confirm that 'Require approved client app' is selected. 6. Use the What If tool to simulate a sign-in from an iOS or Android device and verify that the policy is applied and the grant control is required. 7. On a test iOS device, ensure the Microsoft Authenticator app is installed and the device is registered in Microsoft Entra ID. 8. Attempt to access a protected resource (e.g., Exchange Online) from the device and confirm that access is granted without being redirected to the app store. 9. On a test Android device, ensure either Microsoft Authenticator or Microsoft Company Portal is installed and the device is registered. 10. Repeat the access attempt and confirm successful access without app store redirection.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was modified. 4. Under Access controls > Grant, uncheck 'Require approved client app' and save the policy. 5. Alternatively, if the policy was newly created, delete the policy entirely. 6. If the device platform condition was changed, revert it to the original settings (e.g., remove iOS and Android if they were added). 7. Use the What If tool to confirm that the policy no longer requires an approved client app. 8. On test devices, verify that access to protected resources is granted without the broker app requirement.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
