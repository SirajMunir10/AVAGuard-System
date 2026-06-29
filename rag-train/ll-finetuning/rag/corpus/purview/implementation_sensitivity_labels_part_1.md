# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to publish a sensitivity label for sites and groups and ensure it takes effect?

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
1. Publish the sensitivity label by adding it to a sensitivity label policy
2. Configure the dependent conditional access policy for SharePoint as documented in Use app-enforced restrictions
3. Ensure the label setting is the same or more restrictive than the tenant-level setting for unmanaged devices
4. Create, configure, and publish authentication contexts as part of Microsoft Entra Conditional Access configuration

## Validation
Label setting takes effect after the user next authenticates

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
