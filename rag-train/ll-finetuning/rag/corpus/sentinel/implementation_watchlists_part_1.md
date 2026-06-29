# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How do I create a watchlist in Microsoft Sentinel from a CSV file?

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
1. Navigate to the Microsoft Sentinel workspace in the Azure portal.
2. Under Configuration, select Watchlists.
3. Click Add new.
4. Provide a name, description, and alias for the watchlist.
5. Upload a CSV file containing the data.
6. Map the columns from the CSV to the watchlist fields.
7. Review and create the watchlist.

## Validation
Verify the watchlist appears in the Watchlists list and data is queryable.

## Rollback
Delete the watchlist from the Watchlists blade.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
