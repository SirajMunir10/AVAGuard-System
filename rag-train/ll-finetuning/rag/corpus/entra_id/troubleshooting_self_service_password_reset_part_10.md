# Troubleshooting: Self-Service Password Reset

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
The user never receives the password reset email.

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Email delivery and spam filtering

## Symptoms
- User does not receive password reset email

## Error Codes
N/A

## Root Causes
1. The message is rejected by a spam filter

## Remediation Steps
1. Check your spam, junk, or deleted items folder for the email
2. Make sure the user checks the correct email account as registered with SSPR

## Validation
1. Ask the user to check their spam, junk, or deleted items folder for the password reset email. 2. Confirm with the user that the email address they are checking matches the one registered for SSPR in Microsoft Entra ID (e.g., via the user's profile in the Entra admin center). 3. If the email is still not found, ask the user to initiate another password reset and monitor the email account in real time, including spam and junk folders.

## Rollback
1. If the user still does not receive the email after checking spam/junk folders and verifying the registered email address, escalate to the email administrator to check mail flow logs for rejection by spam filters. 2. As a temporary workaround, enable alternate authentication methods (e.g., phone call or SMS) for the user in SSPR settings. 3. If the issue persists, consider adding the Microsoft password reset email domain or sender address to the user's email allow list.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
