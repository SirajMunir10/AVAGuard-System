# Incident Response: Data Classification and Incident Response

**Domain:** Purview
**Subdomain:** Data Classification and Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A sensitive data spill is detected in Microsoft Purview. How do I use Content Explorer and Activity Explorer to identify the scope of exposure and initiate a response?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Purview Information Protection and Data Loss Prevention configured
- **Configuration:** Sensitivity labels applied to documents; DLP policies in audit-only mode

## Symptoms
- Alert from Microsoft 365 Defender indicating sensitive data (e.g., credit card numbers) was shared externally
- Data Classification dashboard shows unexpected spike in high-sensitivity items
- Activity Explorer logs show external sharing of labeled documents

## Error Codes
N/A

## Root Causes
1. User accidentally attached a sensitive document to an external email
2. DLP policy was in audit-only mode and did not block the action

## Remediation Steps
1. Use Content Explorer in Microsoft Purview compliance portal to locate all copies of the sensitive file across SharePoint, OneDrive, and Exchange
2. Use Activity Explorer to review the exact user, timestamp, and destination of the external share
3. Apply a DLP policy in block mode to prevent further sharing of that sensitivity label
4. Revoke access to the shared file using SharePoint Online or OneDrive sharing management
5. Notify the data owner and initiate a formal incident response process per your organization's policy

## Validation
Confirm that the DLP policy now blocks external sharing of the affected sensitivity label by attempting to share a test file with the same label to an external domain.

## Rollback
If the block policy causes business disruption, revert the DLP policy to audit-only mode and implement user training instead.

## References
- <https://learn.microsoft.com/en-us/purview/data-classification-incident-response>
