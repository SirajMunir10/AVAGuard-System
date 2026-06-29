# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the Collect file button disabled when trying to collect a file in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** RBAC permissions for file collection

## Symptoms
- Collect file button is grayed out or disabled during an active collection attempt

## Error Codes
N/A

## Root Causes
1. Insufficient RBAC permissions to collect files
2. File has not been seen in the organization in the past 30 days
3. File was quarantined as a potential network threat and may not be recoverable

## Remediation Steps
1. Ensure appropriate RBAC permissions are assigned: For Portable Executable files (.exe, .sys, .dll, and others), Security Administrator or Advanced live response or Alerts permissions are required. For Non-Portable Executable files (.txt, .docx, and others), Security Administrator or Advanced live response permissions are required.
2. If the file hasn't been seen in the organization in the past 30 days, the Collect file button is disabled by design.
3. If the file was quarantined as a potential network threat, it might not be recoverable due to expired network credentials.

## Validation
1. Confirm that the user account has the required RBAC role: In Microsoft 365 Defender, go to Settings > Endpoints > Roles. Verify the user is assigned a role with 'Security Administrator', 'Advanced live response', or 'Alerts' permissions. 2. For a Portable Executable file, ensure the role includes 'Advanced live response' or 'Alerts' permission. For a Non-Portable Executable file, ensure the role includes 'Advanced live response' permission. 3. Check the file's last seen date: In the file's details page, look for 'First seen' and 'Last seen' timestamps. If 'Last seen' is more than 30 days ago, the button is disabled by design. 4. If the file was quarantined as a potential network threat, verify the quarantine status and note that network credentials may have expired, making the file unrecoverable.

## Rollback
1. If RBAC permissions were changed, revert the user's role assignment to the previous role. 2. No rollback is needed for the 30-day rule as it is a design limitation. 3. If the file was quarantined and network credentials expired, no rollback is possible; the file cannot be recovered.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
