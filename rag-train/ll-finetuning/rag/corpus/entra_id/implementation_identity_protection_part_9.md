# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
How to enable self-service password reset in Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Identity Protection

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Self-service password reset.
2. In Active Directory, only select the option User must change password at next logon after you enable everything in the previous bullets.

## Validation
1. Sign in to the Entra admin center as a Global Administrator. 2. Browse to Protection > Password reset. 3. Confirm that 'Self-service password reset enabled' is set to 'Selected' or 'All' and the appropriate groups are selected. 4. In an InPrivate/Incognito session, navigate to https://passwordreset.microsoftonline.com and verify that a test user can complete the password reset flow. 5. In Active Directory Users and Computers, confirm that the 'User must change password at next logon' checkbox is selected for the relevant user accounts.

## Rollback
1. Sign in to the Entra admin center as a Global Administrator. 2. Browse to Protection > Password reset. 3. Set 'Self-service password reset enabled' to 'None' to disable SSPR. 4. In Active Directory Users and Computers, clear the 'User must change password at next logon' checkbox for any users where it was set. 5. Verify that users can no longer access the password reset portal by navigating to https://passwordreset.microsoftonline.com in an InPrivate/Incognito session.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
