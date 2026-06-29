# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How do I create a shared access signature (SAS) URL for Microsoft Sentinel to retrieve watchlist data?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with watchlist feature enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a shared access signature URL for Microsoft Sentinel to retrieve the watchlist data.
2. Only public Blob SAS URI is supported.
3. Follow the steps in Create SAS tokens for blobs in the Azure portal.
4. Set the shared access signature token expiry time to at least six hours.
5. Keep the default value for Allowed IP addresses as blank.
6. Copy the value for Blob SAS URL.

## Validation
1. In the Azure portal, navigate to the Microsoft Sentinel workspace. 2. Under 'Configuration', select 'Watchlist'. 3. Click '+ Add' and select 'Create new watchlist'. 4. In the 'Source Type' dropdown, choose 'Azure Storage'. 5. In the 'SAS URI' field, paste the Blob SAS URL you copied. 6. Complete the remaining fields (e.g., Name, Description) and click 'Next: Review + create'. 7. On the 'Review + create' tab, verify that the watchlist preview loads correctly and shows the expected data. 8. Click 'Create'. 9. After creation, confirm the watchlist appears in the list with a status of 'Succeeded'.

## Rollback
1. In the Azure portal, navigate to the Microsoft Sentinel workspace. 2. Under 'Configuration', select 'Watchlist'. 3. Locate the watchlist that was created using the SAS URL. 4. Select the watchlist and click 'Delete' to remove it. 5. In the confirmation dialog, click 'Yes' to confirm deletion. 6. If the SAS token is no longer needed, revoke it by regenerating the storage account key or deleting the stored access policy associated with the SAS token in the Azure Storage account.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
