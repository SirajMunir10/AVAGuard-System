# Hardening: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Hardening

## Scenario / Query
How to prompt users to set up the Microsoft Authenticator app during sign-in to increase security for MFA registered users?

## Environment Context
- **Tenant Type:** Entra ID tenant with MFA registered users using SMS or voice calls
- **Configuration:** Public preview functionality to prompt users to set up Microsoft Authenticator app during sign-in

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Identify users registered for MFA using SMS or voice calls.
2. Use the public preview functionality to prompt users to set up the Microsoft Authenticator app during sign-in.
3. Set these prompts by group to control who is prompted.
4. Enable targeted campaigns to move users to the more secure method.

## Validation
1. Sign in to the Entra ID admin center as an Authentication Policy Administrator. 2. Navigate to Protection > Authentication methods > Policies > Microsoft Authenticator. 3. Confirm the 'Enable' toggle is set to 'Yes' and the 'Target' includes the intended user group. 4. As a test user in the targeted group, sign in at https://aka.ms/mfasetup and verify that a prompt appears to set up the Microsoft Authenticator app. 5. Check the sign-in logs for the test user: look for an event with Activity 'User registered for security info' and Method 'Microsoft Authenticator'.

## Rollback
1. Sign in to the Entra ID admin center as an Authentication Policy Administrator. 2. Navigate to Protection > Authentication methods > Policies > Microsoft Authenticator. 3. Set the 'Enable' toggle to 'No' or remove the targeted group from the 'Target' field. 4. If a targeted campaign was created, navigate to Protection > Authentication methods > Campaigns, select the campaign, and click 'Delete campaign'. 5. Confirm that test users no longer see the Authenticator setup prompt during sign-in by having a test user sign in at https://aka.ms/mfasetup.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
