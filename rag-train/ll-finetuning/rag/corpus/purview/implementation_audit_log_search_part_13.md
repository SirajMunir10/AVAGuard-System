# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to search for activities related to enabling and disabling information barriers for a SharePoint site using audit log search?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search in Microsoft Purview

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the audit activities article to find the exact operation name for the information barriers activities you want to search for
2. Enter SPOIBIsEnabled,SPOIBIsDisabled in the operation search field
3. Copy and paste the operation names directly from the article to the operation search field to ensure they're entered correctly and without typos

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search. 2. In the 'Activities' filter, select 'SharePoint site activities' and then choose 'Enabled information barriers for site' and 'Disabled information barriers for site' from the list. Alternatively, in the 'Activities' filter, type or paste the operation names: SPOIBIsEnabled, SPOIBIsDisabled. 3. Set the date range to cover the expected time of the remediation. 4. Click 'Search'. 5. Confirm that the search results include audit records for the target SharePoint site showing the expected 'Enabled information barriers for site' or 'Disabled information barriers for site' events with the correct site URL.

## Rollback
1. If the remediation introduced unintended changes, navigate to the affected SharePoint site. 2. Go to Site settings > Site permissions > Site collection administration > Information barriers. 3. Toggle the information barriers setting back to its original state (enable if disabled, disable if enabled). 4. Alternatively, use SharePoint Online Management Shell: Connect-SPOService -Url https://[tenant]-admin.sharepoint.com; then run Set-SPOSite -Identity <SiteURL> -InformationBarrierMode <OriginalMode> (e.g., 'Open' or 'Explicit'). 5. Verify the change by running Get-SPOSite -Identity <SiteURL> | Select-Object InformationBarrierMode. 6. Re-run the audit log search to confirm the rollback action is recorded.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
