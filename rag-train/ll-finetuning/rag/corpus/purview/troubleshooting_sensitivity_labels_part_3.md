# Troubleshooting: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle a detected document sensitivity mismatch when a higher priority labeled document is uploaded to a site with a lower priority sensitivity label?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels with Groups & sites scope; label priority order configured

## Symptoms
- User uploads a document with a higher priority sensitivity label (e.g., Confidential) to a SharePoint site with a lower priority label (e.g., General)
- Action is not blocked but generates an automatic email with subject 'Incompatible sensitivity label detected'
- Email sent to the uploader, site owners, and site admins (maximum of 100 recipients)
- Audit log event 'Detected document sensitivity mismatch' from the File and page activities category

## Error Codes
N/A

## Root Causes
1. Document has a higher priority sensitivity label than the sensitivity label applied to the site
2. Label separation with Groups & sites scope for labels that protect containers

## Remediation Steps
1. Identify the uploaded document via the email link or audit log
2. Delete or move the uploaded document from the site as needed
3. Configure the hyperlink for the troubleshooting guide using the Set-SPOTenant cmdlet with the LabelMismatchEmailHelpLink parameter

## Validation
Search the audit log for 'Detected document sensitivity mismatch' from the File and page activities category

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
