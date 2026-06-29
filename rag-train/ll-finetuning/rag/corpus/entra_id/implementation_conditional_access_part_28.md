# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure Conditional Access policy to require an Intune app protection policy on client apps before granting access?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Intune integrated
- **Configuration:** Conditional Access policy with grant control set to 'Require app protection policy'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the device is registered in Microsoft Entra ID, which requires using a broker app (Microsoft Authenticator for iOS or Microsoft Company Portal for Android).
2. If a broker app isn't installed on the device when the user attempts to authenticate, the user is redirected to the app store to install the broker app.
3. Note: The Microsoft Authenticator app can be used as the broker app but does not support being targeted as an approved client app.
4. For Windows devices, note that no more than three Microsoft Entra user accounts are supported in the same session.
5. For Windows devices, refer to the article 'Require an app protection policy on Windows devices (preview)' for more information.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies and select the policy that was configured with 'Require app protection policy' grant control. 3. Verify that under 'Grant', the control 'Require app protection policy' is selected and no other grant controls are conflicting. 4. On a test device that is registered in Microsoft Entra ID (using Microsoft Authenticator on iOS or Company Portal on Android), attempt to access a protected resource (e.g., Exchange Online). 5. Confirm that access is blocked if the device does not have an Intune app protection policy applied. 6. Apply an Intune app protection policy to the test device, then reattempt access and verify that access is granted. 7. For Windows devices, ensure no more than three Microsoft Entra user accounts are in the same session and refer to the preview documentation for additional validation steps.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies and select the policy that was configured with 'Require app protection policy'. 3. Under 'Grant', change the control from 'Require app protection policy' to 'Require all the selected controls' or remove the app protection policy requirement, then save the policy. 4. Alternatively, set the policy state to 'Off' to disable it entirely. 5. Verify that users can access resources without the app protection policy requirement. 6. If the issue was caused by a broker app not being installed, ensure users install Microsoft Authenticator (iOS) or Company Portal (Android) and re-register the device in Microsoft Entra ID.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
