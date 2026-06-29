# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I define network share groups for endpoint DLP policies to assign different policy actions to specific network share paths?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policies scoped to Devices; Windows 10 and later (21H1, 21H2) with KB 5018482, Windows 11 21H2/22H2 with KB 5018483, Windows 10 RS5 (KB 5006744), Windows Server 2022

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define groups of network share paths using prefixes that all shares start with, e.g., '\Library' matches the Library folder and all its subfolders.
2. Use wildcards, e.g., '\Users*\Desktop' matches '\Users\user1\Desktop' and '\Users\user1\user2\Desktop'.
3. Use environmental variables, e.g., '%AppData%\app123'.
4. Wildcard values are supported; a path definition can contain an asterisk (*) in the middle or at the end of the path, e.g., '\\Lib*' covers '\\Library'.
5. Assign policy actions to the group: Allow (audit with no user notifications or alerts), Audit only (with notifications and alerts), Block with override (blocks action but user can override), Block (blocks no matter what).
6. After defining a network share group, use it in all DLP policies scoped to Devices.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Network share groups. 2. Confirm the network share group is listed with the correct path prefixes and wildcards. 3. Create a test DLP policy scoped to Devices that uses the network share group. 4. On a test Windows device (Windows 10 21H1+ with required KB), copy a sensitive file to a network share path matching the defined group. 5. Verify the expected policy action (e.g., Block with override) is enforced and an audit event appears in Activity explorer.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Network share groups, delete the network share group. 2. Remove the network share group from any DLP policies that reference it. 3. If the policy was created solely for testing, delete the test DLP policy. 4. On the test device, confirm that the previous policy action no longer applies to the network share path.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
