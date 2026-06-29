# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How does location selection affect content definition methods in a DLP policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with multiple locations

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
1. When multiple locations are selected, a 'no' value for a content definition category takes precedence over 'yes' value.

## Remediation Steps
1. When selecting SharePoint sites only, the policy supports detecting sensitive items by one or more of SIT, by sensitivity label or by retention label.
2. When selecting SharePoint sites and Teams chat and channel messages locations, the policy will only support detecting sensitive items by SIT.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Open the DLP policy in question. 3. Under 'Locations', confirm that only 'SharePoint sites' is selected. 4. Under 'Content definitions', verify that the policy allows detection by SIT, sensitivity label, or retention label. 5. Edit the policy to add 'Teams chat and channel messages' location. 6. Under 'Content definitions', confirm that only SIT is available for detection. 7. Remove the Teams location and revert to SharePoint only. 8. Confirm that detection by sensitivity label and retention label are again available.

## Rollback
1. If the policy fails to detect content after adding Teams location, remove the Teams location from the policy. 2. If the policy fails to detect content after removing Teams location, re-add the Teams location. 3. If the policy becomes non-functional, restore the previous policy configuration from backup or recreate the policy with the original settings.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
