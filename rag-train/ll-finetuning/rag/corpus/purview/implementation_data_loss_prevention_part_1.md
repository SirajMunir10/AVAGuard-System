# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to design a DLP policy that groups rules for a specific regulation like HIPAA?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy for HIPAA compliance across SharePoint and OneDrive

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a DLP policy that helps detect the presence of information subject to HIPAA
2. Define the 'what' by configuring sensitive information types for HIPAA data
3. Define the 'where' by targeting all SharePoint sites and all OneDrive sites
4. Set conditions to find documents containing HIPAA sensitive information shared with people outside your organization
5. Configure actions to block access to the document and send a notification
6. Store these requirements as individual rules grouped together as a DLP policy to simplify management and reporting

## Validation
Verify that the policy detects HIPAA data and applies the configured actions when conditions are met

## Rollback
Disable or delete the DLP policy if it does not meet compliance requirements

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
