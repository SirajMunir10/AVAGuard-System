# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure authentication contexts for sensitivity labels on sites and groups?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Entra Conditional Access configuration

## Symptoms
- Authentication context not available in drop-down list for selection
- Users with unsupported apps see access denied or are prompted to authenticate but rejected

## Error Codes
N/A

## Root Causes
1. Authentication contexts not created, configured, and published as part of Microsoft Entra Conditional Access configuration

## Remediation Steps
1. Create, configure, and publish authentication contexts as part of Microsoft Entra Conditional Access configuration
2. Refer to the Configure authentication contexts section from the Microsoft Entra Conditional Access documentation

## Validation
Authentication context appears in drop-down list for selection

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
