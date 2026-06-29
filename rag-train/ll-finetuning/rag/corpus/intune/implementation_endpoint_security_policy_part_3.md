# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How do I duplicate an endpoint security policy in Intune for different deployment scenarios?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint Security Policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Locate the source policy in the policy list.
2. Select the ellipsis (â€¦) > Duplicate.
3. Provide a new descriptive name and save.
4. Edit the duplicated policy to customize settings for your specific use case.
5. Configure new group assignments for the target scenario.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Manage > Policies. 2. Confirm the duplicated policy appears in the list with the new name. 3. Select the duplicated policy and verify its settings match the source policy except for any intended customizations. 4. Under Assignments, confirm the new group assignments are correctly configured. 5. Use the 'Check status' option for the policy to ensure it is applied to the intended devices without errors.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Manage > Policies. 2. Locate the duplicated policy. 3. Select the ellipsis (…) next to the policy and choose 'Delete'. 4. Confirm the deletion when prompted. 5. If the original source policy was modified, restore it from a backup or recreate it using the original settings.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
