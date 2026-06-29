# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
What to do when access to the Microsoft Purview audit log search page requires authorization?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** N/A

## Symptoms
- Access to this page requires authorization.
- You can try signing in or changing directories.

## Error Codes
N/A

## Root Causes
1. User may not have appropriate permissions or may be in the wrong directory.

## Remediation Steps
1. Try signing in with appropriate credentials.
2. Try changing directories to the correct tenant.

## Validation
1. Confirm the user is signed in with an account that has the 'Audit Log' role or equivalent (e.g., Global Admin, Compliance Admin, Audit Logs admin).
2. Navigate to the Microsoft Purview compliance portal (https://compliance.microsoft.com) and select 'Audit' under 'Solutions'.
3. Verify that the audit log search page loads without the 'Access to this page requires authorization' error.
4. Run a test audit log search (e.g., search for activities from the last 24 hours) and confirm results are returned.
5. If the user is in the wrong directory, use the directory picker (top-right corner) to switch to the correct tenant and repeat steps 2-4.

## Rollback
1. If the user cannot access the audit log search page after signing in with appropriate credentials, sign out and sign in with the original account that had the issue.
2. If the user changed directories and the audit log search page still shows the authorization error, switch back to the original directory using the directory picker.
3. If the issue persists, verify the user's role assignments in the Microsoft 365 admin center (https://admin.microsoft.com) under 'Roles' -> 'Role assignments' and ensure the 'Audit Logs' role is assigned.
4. If the user still cannot access, contact your Microsoft 365 tenant administrator to confirm the tenant's audit log configuration and licensing (e.g., E5 or A5 subscription).

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
