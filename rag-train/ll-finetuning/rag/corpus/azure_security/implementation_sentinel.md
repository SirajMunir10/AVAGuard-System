# Implementation: Sentinel

**Domain:** Azure
**Subdomain:** Sentinel
**Incident Type:** Implementation

## Scenario / Query
How do I configure CORS for Azure Storage to use a SAS URI with Azure Sentinel watchlists?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure Storage account with Blob service

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to the storage account settings, Resource sharing page.
2. Select the Blob service tab.
3. Add https://*.portal.azure.net to the allowed origins table.
4. Select the appropriate Allowed methods of GET and OPTIONS.
5. Save the configuration.

## Validation
1. In the Azure portal, navigate to the storage account > 'Resource sharing (CORS)' > 'Blob service' tab. 2. Confirm that 'https://*.portal.azure.net' appears in the 'Allowed origins' list. 3. Verify that 'GET' and 'OPTIONS' are selected under 'Allowed methods'. 4. Save the configuration. 5. In Azure Sentinel, go to 'Watchlists' and attempt to create or update a watchlist using a SAS URI from that storage account. 6. Confirm the watchlist is created or updated without CORS-related errors.

## Rollback
1. In the Azure portal, navigate to the storage account > 'Resource sharing (CORS)' > 'Blob service' tab. 2. Delete the entry 'https://*.portal.azure.net' from the 'Allowed origins' list. 3. Uncheck 'GET' and 'OPTIONS' under 'Allowed methods' if they were not previously selected. 4. Save the configuration. 5. In Azure Sentinel, verify that watchlist operations using SAS URIs from that storage account now fail with a CORS error, confirming the rollback.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
