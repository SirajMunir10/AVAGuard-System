# Hardening: Conditional Access (53003 â€“ Conditional Access policy not satisfied (if policy is misconfigured to allow legacy auth))

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How can I detect and remediate a tenant where legacy authentication protocols (POP3, IMAP, SMTP, ActiveSync) are not blocked by a Conditional Access policy, leaving the tenant vulnerable to password spray and replay attacks?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) P1 or P2
- **Configuration:** Conditional Access policies that should include the 'Other clients' condition to block legacy authentication

## Symptoms
- Sign-in logs show successful authentications from legacy protocols (POP3, IMAP, SMTP, ActiveSync) that do not support modern authentication
- Conditional Access policies are configured but do not apply to 'Other clients'
- Security alerts for password spray or brute force attacks originating from legacy protocol clients

## Error Codes
- `53003 â€“ Conditional Access policy not satisfied (if policy is misconfigured to allow legacy auth)`
- `50053 â€“ Account locked due to repeated failed sign-in attempts (common with legacy protocol attacks)`

## Root Causes
1. Conditional Access policy does not include the 'Client apps' condition with 'Other clients' selected
2. Legacy authentication protocols are not explicitly blocked by a Conditional Access policy or tenant-wide setting

## Remediation Steps
1. 1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator.
2. 2. Navigate to Protection > Conditional Access > Policies.
3. 3. Create a new policy or modify an existing one: Assign the target users/groups, and under 'Cloud apps or actions' select 'All cloud apps'.
4. 4. Under 'Conditions' > 'Client apps', select 'Other clients' (this covers legacy authentication protocols).
5. 5. Under 'Access controls' > 'Grant', select 'Block access'.
6. 6. Enable the policy and set it to 'On'.
7. 7. Optionally, use the legacy authentication blocking feature in the 'Authentication methods' > 'Settings' blade to block legacy auth at the tenant level.

## Validation
After the policy is enabled, verify that sign-in logs for legacy protocol attempts show 'Blocked by Conditional Access' with error code 53003. Use the 'Sign-in logs' report filtered by 'Client app' containing 'Other clients' to confirm no successful legacy authentications.

## Rollback
Set the Conditional Access policy to 'Off' or delete the policy. If tenant-level legacy auth blocking was enabled, disable it in Authentication methods > Settings.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-block-legacy-authentication>
- CIS Microsoft 365 Foundations Benchmark v2.0.0 â€“ Control 1.1.3: 'Block legacy authentication'
