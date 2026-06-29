# Troubleshooting: Android Enrollment

**Domain:** Intune
**Subdomain:** Android Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle Microsoft Edge sign-in prompt during Android enrollment when an unenrolled user tries to access corporate data protected by conditional access?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Conditional access policy protecting corporate data

## Symptoms
- Microsoft Edge app prompts user to sign in during enrollment flow
- User is diverted from the enrollment flow

## Error Codes
N/A

## Root Causes
1. User tries to access corporate data before enrolling their device
2. Microsoft Edge app is launched to open Company Portal website during enrollment

## Remediation Steps
1. Tell users to enroll in the Company Portal before trying to access their organization's data
2. If user is prompted by Microsoft Edge to sign in, they should skip the Microsoft Edge sign-in step to proceed with enrollment flow
3. Users can initiate enrollment in the preinstalled Company Portal app

## Validation
1. Confirm the user's device is now enrolled in Intune by checking the device status in the Microsoft Intune admin center: Devices > All devices > search for the user's device and verify the 'Managed by' column shows 'Intune' and 'Enrollment state' is 'Success'.
2. Verify the user can access corporate data (e.g., Microsoft Edge or Outlook) without being prompted to sign in again by having the user open the corporate app and confirming no sign-in prompt appears.
3. Check the conditional access policy logs in Azure AD: Sign-in logs > filter by user and application (e.g., Microsoft Edge) to confirm the sign-in was successful and not blocked by conditional access.

## Rollback
1. If the user cannot complete enrollment, instruct them to skip the Microsoft Edge sign-in prompt during the Company Portal enrollment flow, as documented in the troubleshooting guide.
2. If the user is already enrolled but still sees the sign-in prompt, have them sign out of Microsoft Edge and the Company Portal app, then re-initiate enrollment from the preinstalled Company Portal app.
3. As a last resort, remove the device from Intune: In the Microsoft Intune admin center, go to Devices > All devices, select the device, and choose 'Delete'. Then have the user re-enroll the device by opening the Company Portal app and following the enrollment steps.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-android-enrollment>
