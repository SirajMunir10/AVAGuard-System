# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How does DLP proactively block documents in SharePoint and OneDrive for guests?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** SharePoint and OneDrive locations in DLP policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For SharePoint and OneDrive locations, documents will be proactively blocked right after detection of sensitive information (regardless of whether the document is shared or not) for all guests.
2. Internal users continue to have access to the document.

## Validation
1. Confirm that the DLP policy includes SharePoint and OneDrive locations and is configured to block access for guests. Run: Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List ExchangeLocation, SharePointLocation, OneDriveLocation, Mode. 2. Verify the policy action is set to 'Block' for external users. Run: Get-DlpComplianceRule -Policy "PolicyName" | Where-Object {$_.AccessScope -eq 'ExternalUser'} | Format-List Actions. 3. Upload a test document containing sensitive info (e.g., credit card number) to a SharePoint site shared with a guest account. 4. As the guest, attempt to open the document; confirm access is denied and a policy tip is shown. 5. As an internal user, verify the document remains accessible.

## Rollback
1. Disable the DLP policy that blocks guests: Set-DlpCompliancePolicy -Identity "PolicyName" -State Disabled. 2. Remove the test document from SharePoint. 3. Confirm guest access is restored by having the guest open a previously blocked document. 4. Re-enable the policy if needed after investigation: Set-DlpCompliancePolicy -Identity "PolicyName" -State Enabled.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
