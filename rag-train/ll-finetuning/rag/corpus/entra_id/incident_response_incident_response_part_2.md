# Incident Response: Incident Response

**Domain:** Entra ID
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst suspects that a compromised user account in Entra ID is being used to perform unauthorized privileged role activation. How can the analyst use the Entra ID audit logs to identify the suspicious activity and what immediate steps should be taken to contain the incident?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) P2 licensed tenant with Privileged Identity Management (PIM) enabled
- **Configuration:** PIM role activation requires Azure AD Multi-Factor Authentication (MFA); audit logging is enabled by default for all directory operations

## Symptoms
- Unexpected activation of a privileged role (e.g., Global Administrator) by a user who does not normally require that role
- Multiple role activations from an unusual IP address or geographic location
- Role activation occurring outside of normal business hours

## Error Codes
N/A

## Root Causes
1. User account credentials were compromised (e.g., through phishing or password reuse)
2. Attacker used the compromised account to activate a privileged role via PIM

## Remediation Steps
1. Immediately revoke all active role assignments for the compromised user by using the Entra ID admin center or the `Remove-AzureADMSPrivilegedRoleAssignment` PowerShell cmdlet (documented in Microsoft Learn: 'Remove-AzureADMSPrivilegedRoleAssignment')
2. Reset the user's password and require MFA re-registration
3. Sign out the user from all sessions using the 'Revoke sessions' option in the Entra ID admin center
4. Review and disable any suspicious applications or service principals that may have been granted consent by the compromised user
5. Enable and review the Entra ID audit logs for any other suspicious activity, focusing on the 'Add member to role' activity

## Validation
Confirm that the suspicious role activation no longer appears in the audit logs and that the userâ€™s account has been secured. Verify that no new privileged role activations occur from the same IP address.

## Rollback
If the account was incorrectly disabled, re-enable it and restore the userâ€™s original role assignments using the PIM activation history. Ensure that any password reset is communicated securely to the user.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
- CIS Microsoft 365 Foundation Benchmark v2.0.0, Control 1.1.1
