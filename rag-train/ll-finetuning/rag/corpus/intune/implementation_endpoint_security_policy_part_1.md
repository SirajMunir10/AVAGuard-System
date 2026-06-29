# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
What RBAC permissions are required to configure endpoint security policies in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint security policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use granular permissions for specific workloads: Application control for Business - Application control policies and reports; Attack surface reduction - Most Attack surface reduction policies; Endpoint detection and response - EDR policies and reports.
2. Use Security baselines permission (unified access) for: Antivirus policies (all profiles), Account protection policies, Disk encryption policies, Firewall policies, and some Attack surface reduction profiles: App and browser isolation, Web protection, Exploit protection, Controlled folder access.
3. For Attack surface reduction policies, check the specific profile requirements as some profiles use the granular Attack surface reduction permission while others require Security baselines permission.
4. For detailed profile-specific requirements, see Custom role considerations.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com) with a user assigned a custom Intune role that includes the granular permissions (e.g., 'Application control for Business' > 'Application control policies and reports', 'Attack surface reduction' > 'Most Attack surface reduction policies', 'Endpoint detection and response' > 'EDR policies and reports') or the 'Security baselines' permission. 2. Navigate to 'Endpoint security' > 'Antivirus' and verify that you can create, edit, and assign an antivirus policy (e.g., Windows 10/11 antivirus policy). 3. Navigate to 'Endpoint security' > 'Attack surface reduction' and verify that you can create, edit, and assign an attack surface reduction policy (e.g., App and browser isolation profile). 4. Navigate to 'Endpoint security' > 'Endpoint detection and response' and verify that you can create, edit, and assign an EDR policy. 5. Navigate to 'Endpoint security' > 'Account protection' and verify that you can create, edit, and assign an account protection policy. 6. Navigate to 'Endpoint security' > 'Disk encryption' and verify that you can create, edit, and assign a disk encryption policy. 7. Navigate to 'Endpoint security' > 'Firewall' and verify that you can create, edit, and assign a firewall policy. 8. Confirm that no 'Access denied' or 'Insufficient permissions' errors appear during these operations.

## Rollback
1. If the granular permissions cause unintended access, remove the specific granular permissions from the custom role: a. In Intune admin center, go to 'Tenant administration' > 'Roles' > 'All roles'. b. Select the custom role used for endpoint security. c. Click 'Properties' > 'Permissions' > 'Edit'. d. Under 'Endpoint Security', uncheck the granular permissions that were added (e.g., 'Application control for Business', 'Attack surface reduction', 'Endpoint detection and response'). e. Click 'Review + save' to apply changes. 2. If the 'Security baselines' permission causes unintended access, remove it from the custom role: a. Follow steps a-c above. b. Under 'Endpoint Security', uncheck 'Security baselines'. c. Click 'Review + save'. 3. If the custom role itself is problematic, delete it: a. In Intune admin center, go to 'Tenant administration' > 'Roles' > 'All roles'. b. Select the custom role. c. Click 'Delete' and confirm. 4. To restore previous permissions, reassign the original built-in roles (e.g., 'Endpoint Security Manager') to the affected users via 'Tenant administration' > 'Roles' > 'All roles' > select role > 'Assignments' > 'Assign'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
