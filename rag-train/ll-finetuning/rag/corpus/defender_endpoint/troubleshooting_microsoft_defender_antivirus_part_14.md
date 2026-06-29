# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot issues with Microsoft Defender Antivirus when encountering access authorization problems?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** Microsoft Defender Antivirus

## Symptoms
- Access to this page requires authorization
- You can try signing in or changing directories

## Error Codes
N/A

## Root Causes
1. Authorization issue accessing troubleshooting documentation

## Remediation Steps
1. Try signing in
2. Try changing directories

## Validation
1. Open a browser and navigate to https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus. 2. Confirm the page loads without displaying 'Access to this page requires authorization' or 'You can try signing in or changing directories'. 3. If prompted, sign in with an account that has appropriate permissions (e.g., Global Admin or Security Admin) and verify the full troubleshooting content is accessible.

## Rollback
1. If the page still shows authorization errors, sign out of any current Microsoft account. 2. Clear browser cache and cookies. 3. Attempt to access the URL again in an InPrivate/Incognito session. 4. If the issue persists, contact your tenant administrator to verify your account has the required role (e.g., Security Reader, Security Administrator) and that the tenant is properly licensed for Defender for Endpoint Plan 1 or Plan 2.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
