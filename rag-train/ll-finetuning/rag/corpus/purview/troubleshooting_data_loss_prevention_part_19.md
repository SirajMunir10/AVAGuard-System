# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How to programmatically access business justification values from email X-header after a DLP override?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with user overrides enabled for email

## Symptoms
- User overrides a block with override action on an email
- Override option and text are stored in email X-header

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the msip_justification values in the email X-header data
2. Values are stored in the following order: False Positive; Recipient Entitled; Manager Approved; I Acknowledge; JustificationText_[free text]
3. Values are separated by semicolons
4. Maximum free text allowed is 500 characters

## Validation
Send a test email that triggers a DLP policy with user override enabled. Override the block and provide a justification. Retrieve the email headers using Get-MessageTrace or by inspecting the message in Exchange Online. Confirm the X-header 'msip_justification' contains the expected values in the format: False Positive; Recipient Entitled; Manager Approved; I Acknowledge; JustificationText_[free text]. Verify the free text does not exceed 500 characters.

## Rollback
If the justification values are not appearing or are incorrect, review the DLP policy configuration to ensure user overrides are enabled and the policy is applied to the correct scope. Check that the email client supports the X-header injection. If necessary, disable the override option temporarily and re-enable after troubleshooting. Use Set-DlpCompliancePolicy to adjust the policy settings.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
