# Implementation: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I get access to run advanced hunting queries in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Unified role based access control (URBAC)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign the Advanced Hunting access (Email & Collaboration tables) permission: Membership assigned with the Security operations > Raw data > Email & collaboration metadata (read) URBAC permission.
2. Assign the Advanced Hunting access (Alerts & behaviors tables) permission: Membership assigned with the Security operations > Security data > Security data basics (read) URBAC permission.

## Validation
1. Sign in to the Microsoft Defender portal (https://security.microsoft.com) as a user with the assigned permissions. 2. Navigate to Hunting > Advanced hunting. 3. Run a sample query against the Email & collaboration tables, e.g., EmailEvents | take 10. Verify results are returned. 4. Run a sample query against the Alerts & behaviors tables, e.g., AlertInfo | take 10. Verify results are returned. 5. If either query returns an error or no data, confirm the user’s role assignments in Microsoft Entra ID > Roles & admins > Unified RBAC (Preview) > Assignments.

## Rollback
1. Sign in to the Microsoft Defender portal as a global administrator or a user with the Unified RBAC management permission. 2. Navigate to Permissions > Roles under Microsoft Defender XDR. 3. Select the role(s) that include the Advanced Hunting access permissions (e.g., Security operations > Raw data > Email & collaboration metadata (read) and Security operations > Security data > Security data basics (read)). 4. Remove the user or group from the role assignment. 5. Confirm the user no longer has access by repeating the validation steps and verifying that queries return an access denied error.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
