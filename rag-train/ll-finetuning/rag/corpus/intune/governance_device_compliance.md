# Governance: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Governance

## Scenario / Query
An Intune administrator reports that some devices are marked as non-compliant even though they meet all compliance policy settings. The administrator suspects that the compliance policy assignment is not being applied correctly due to a governance gap in policy scope or exclusion groups.

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Compliance policies assigned to 'All Devices' group, but some devices belong to an exclusion group that was not properly configured.

## Symptoms
- Devices show status 'Not evaluated' or 'Non-compliant' despite meeting policy requirements
- Compliance policy report shows devices in 'Not applicable' state
- Administrator sees inconsistent compliance results across similar devices

## Error Codes
N/A

## Root Causes
1. Exclusion groups are incorrectly configured or contain unintended device objects
2. Compliance policy assignment scope is too broad or too narrow
3. Policy deployment priority or conflict resolution not properly governed

## Remediation Steps
1. Review compliance policy assignments in Microsoft Intune admin center under 'Devices' > 'Compliance policies' > 'Properties' > 'Assignments'
2. Verify that exclusion groups contain only intended devices and that no overlapping assignments cause conflicts
3. Use the 'Device compliance' report to identify devices with 'Not applicable' status and cross-reference with group membership
4. Adjust group membership or policy assignments to ensure correct scope

## Validation
After remediation, run the compliance policy report and confirm that all targeted devices show 'Compliant' status when they meet policy requirements.

## Rollback
If changes cause unintended compliance results, revert to previous assignment configuration by restoring group membership or policy assignments from backup or change log.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/create-compliance-policy>
