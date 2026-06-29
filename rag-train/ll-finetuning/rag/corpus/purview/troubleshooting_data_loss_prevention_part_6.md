# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How to view user override justifications for DLP policy blocks in Exchange, SharePoint, OneDrive, or Teams?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with user overrides enabled and 'Notify users in Office 365 services with a policy tip' enabled

## Symptoms
- Users override DLP block actions with a justification
- Need to audit override justifications for compliance or tuning

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search the audit log for ExceptionInfo value for the details of the override
2. Check the email X-header for msip_justification values in the following order: False Positive; Recipient Entitled; Manager Approved; I Acknowledge; JustificationText_[free text]
3. Note that msip_justification values are separated by semicolons and maximum free text is 500 characters

## Validation
Verify that the audit log contains ExceptionInfo with fields: FalsePositive, Justification, Reason, and Rules

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
