# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I access and use out-of-the-box hunting queries in Microsoft Sentinel after installing a solution from the Content hub?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Content hub solutions installed

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Install a solution that includes hunting queries from the Content hub.
2. Navigate to the hunting Queries tab to view the out-of-the-box queries for that solution.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Threat management', select 'Hunting'. 3. On the 'Queries' tab, verify that queries from the installed solution appear in the list. 4. Optionally, run a query to confirm it executes without errors.

## Rollback
1. In the Azure portal, go to your Microsoft Sentinel workspace. 2. Under 'Content management', select 'Content hub'. 3. Find the solution you installed and select 'Manage'. 4. Choose 'Uninstall' to remove the solution and its associated hunting queries.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
