# Incident Response: Incident Response

**Domain:** Governance
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security administrator suspects that an attacker has compromised a user account and is using it to perform reconnaissance in Microsoft 365. How can the administrator use Microsoft Purview Audit (Standard) to search for suspicious sign-in activity and then initiate an automated investigation and response (AIR) playbook in Microsoft 365 Defender?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 (or E3 with add-on licenses for Audit Standard and Defender for Office 365 Plan 2)
- **Configuration:** Audit logging enabled (default for Standard); Microsoft 365 Defender portal configured with automated investigation and response enabled for Office 365.

## Symptoms
- Unusual sign-in attempts from unfamiliar IP addresses or locations
- Multiple failed sign-in attempts followed by a successful sign-in
- User reports receiving phishing emails that appear to come from internal accounts

## Error Codes
N/A

## Root Causes
1. Compromised user credentials due to phishing or password reuse
2. Lack of conditional access policies to block high-risk sign-ins
3. Insufficient monitoring of audit logs for anomalous activity

## Remediation Steps
1. 1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a user with the Security Administrator role.
2. 2. Go to 'Audit' under 'Search & investigation' to search the unified audit log for the affected user's sign-in events (Workload: AzureActiveDirectory, Activity: UserLoggedIn).
3. 3. Review the audit records for suspicious IP addresses, user agents, and timestamps.
4. 4. From the audit results, select a suspicious event and choose 'Initiate investigation' to trigger an automated investigation in Microsoft 365 Defender.
5. 5. In the Microsoft 365 Defender portal, navigate to 'Incidents & alerts' > 'Incidents' to monitor the automated investigation and review recommended actions (e.g., disable user account, remove suspicious inbox rules).
6. 6. Apply the recommended remediation actions (e.g., reset user password, revoke sessions, block IP) as approved by the security team.

## Validation
After remediation, run a new audit log search for the affected user to confirm no further suspicious sign-ins. Verify that the user account is no longer flagged in the Microsoft 365 Defender incidents queue.

## Rollback
If a remediation action (e.g., disabling the user) was taken in error, re-enable the user account via the Microsoft 365 admin center and restore any removed inbox rules from the deleted items folder.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/audit-log-search?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/m365d-autoir?view=o365-worldwide>
