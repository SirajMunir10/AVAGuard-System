# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to find more hunting queries and data sources in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to the Content hub in Microsoft Sentinel.
2. Refer to community resources like the Microsoft Sentinel GitHub repository.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Content management', select 'Content hub'. 3. Verify that the 'Content hub' page loads and displays available solutions, including hunting queries and data connectors. 4. Open a browser and go to https://github.com/Azure/Azure-Sentinel. 5. Confirm that the repository is accessible and contains hunting queries and sample data sources.

## Rollback
1. If the Content hub fails to load, ensure the Microsoft Sentinel workspace is deployed and has the necessary permissions (e.g., Contributor role). 2. If the GitHub repository is inaccessible, check network connectivity or firewall rules that may block github.com. 3. No further rollback is required as the remediation steps are informational and do not alter the environment.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
- <https://github.com/Azure/Azure-Sentinel>
