# Troubleshooting: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Troubleshooting

## Scenario / Query
Why does a sensitivity label setting for sites and groups have no effect even after publishing?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity label policy, SharePoint conditional access policy, tenant-level settings for unmanaged devices

## Symptoms
- Sensitivity label option for sites and groups has no effect
- Label setting is less restrictive than tenant-level configuration

## Error Codes
N/A

## Root Causes
1. Dependent conditional access policy for SharePoint not configured as documented in Use app-enforced restrictions
2. Label setting is less restrictive than a configured setting at the tenant level
3. Authentication contexts not created, configured, and published as part of Microsoft Entra Conditional Access configuration

## Remediation Steps
1. Configure the dependent conditional access policy for SharePoint as documented in Use app-enforced restrictions
2. Choose a label setting that is the same or more restrictive than the tenant-level setting for unmanaged devices
3. Create, configure, and publish authentication contexts as part of Microsoft Entra Conditional Access configuration

## Validation
Label setting takes effect after the user next authenticates

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
