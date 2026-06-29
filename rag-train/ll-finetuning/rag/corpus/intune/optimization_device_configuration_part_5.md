# Optimization: Device Configuration

**Domain:** Intune
**Subdomain:** Device Configuration
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Intune device configuration by reducing the number of duplicate or conflicting policies assigned to the same user or device groups?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Multiple Configuration Profiles and Compliance Policies assigned to overlapping Azure AD groups

## Symptoms
- Devices show 'Conflict' status for one or more configuration profiles
- Users report unexpected settings changes or inability to change settings
- Intune reporting shows high number of policy evaluation errors

## Error Codes
N/A

## Root Causes
1. Multiple policies targeting the same setting with different values
2. Overlapping group assignments without exclusion rules
3. Lack of policy prioritization review

## Remediation Steps
1. Review assigned policies in the Microsoft Intune admin center under 'Devices' > 'Configuration profiles' and 'Compliance policies'
2. Use the 'Conflicts' tab in the device policy report to identify conflicting assignments
3. Consolidate policies by merging duplicate settings into a single profile
4. Apply exclusion groups to remove overlapping assignments
5. Assign policies to the smallest possible group to reduce conflicts

## Validation
Verify that the number of devices in 'Conflict' status drops to zero and that all target devices report 'Succeeded' for the consolidated policies.

## Rollback
If consolidation causes unintended settings, revert to the previous policy assignments by reassigning the original profiles and removing the consolidated profile.

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
