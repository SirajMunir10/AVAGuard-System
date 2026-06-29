# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve authorization errors when accessing Microsoft Defender Antivirus configuration documentation?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Access to this page requires authorization.
- You can try signing in or changing directories.

## Error Codes
N/A

## Root Causes
1. User may not be signed in with appropriate credentials.
2. User may be in an incorrect directory or tenant.

## Remediation Steps
1. Sign in with appropriate credentials.
2. Change directories to the correct tenant.

## Validation
1. Open a new InPrivate/Incognito browser session. 2. Navigate to https://learn.microsoft.com/en-us/defender-endpoint/configure-microsoft-defender-antivirus-features. 3. Sign in with the appropriate credentials (e.g., a user account with the required permissions, such as Security Administrator or Global Reader). 4. Confirm the page loads without any authorization errors. 5. Verify the directory/tenant shown in the top-right corner matches the correct tenant for your organization.

## Rollback
1. Sign out of the current session. 2. Clear browser cache and cookies. 3. Sign in with the original credentials that were experiencing the authorization error. 4. If the issue persists, switch to the original directory/tenant by clicking the user icon in the top-right corner and selecting the appropriate directory. 5. Document the error and contact your tenant administrator if access is still denied.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-microsoft-defender-antivirus-features>
