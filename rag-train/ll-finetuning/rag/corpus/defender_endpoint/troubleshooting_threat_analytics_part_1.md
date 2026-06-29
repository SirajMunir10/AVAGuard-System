# Troubleshooting: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Troubleshooting

## Scenario / Query
What roles and permissions are required to access Threat analytics in the Defender portal?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Licensing for at least one Microsoft Defender XDR product (except Microsoft Defender for Endpoint P1); Microsoft Sentinel SIEM customers have limited access.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure you have a license for at least one Microsoft Defender XDR product (Microsoft Defender for Endpoint P1 license is an exception and doesn't grant Threat analytics access).
2. Assign the Security data basics (read) role to view threat analytics report, related incidents and alerts, and impacted assets.
3. Assign the Vulnerability management (read) and Exposure Management (read) roles to see related exposure data and recommended actions.
4. If not using Microsoft Defender unified RBAC, create custom roles for each service using Microsoft Entra global roles.

## Validation
1. Confirm the user has a valid license for at least one Microsoft Defender XDR product (excluding Microsoft Defender for Endpoint P1) by checking the Microsoft 365 admin center > Billing > Licenses. 2. Verify the user is assigned the 'Security data basics (read)' role in Microsoft Defender unified RBAC by navigating to Microsoft Defender XDR > Permissions > Roles > select the role and review assignments. 3. If exposure data access is needed, confirm the user also has 'Vulnerability management (read)' and 'Exposure Management (read)' roles assigned. 4. If not using unified RBAC, verify the user has a Microsoft Entra global role that grants equivalent permissions (e.g., Security Reader). 5. Sign in to Microsoft Defender XDR (https://security.microsoft.com) as the user and navigate to Threat analytics to confirm the page loads and shows reports, incidents, alerts, and impacted assets.

## Rollback
1. Remove the 'Security data basics (read)' role assignment from the user in Microsoft Defender XDR > Permissions > Roles. 2. If assigned, remove the 'Vulnerability management (read)' and 'Exposure Management (read)' roles. 3. If using Microsoft Entra global roles, remove the user from the assigned role (e.g., Security Reader) via Microsoft Entra admin center > Roles and administrators. 4. If the user was granted a custom role, delete or modify the custom role to remove permissions. 5. Verify the user can no longer access Threat analytics by signing in and confirming the page is blocked or shows insufficient permissions.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
