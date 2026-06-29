# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy actions for applying HTML disclaimer, prepending subject, or applying message encryption?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with actions 'Apply HTML disclaimer', 'Prepend subject', 'Apply message encryption', 'Remove message encryption (preview)'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure the DLP policy action: 'Apply HTML disclaimer'.
2. Configure the DLP policy action: 'Prepend subject'.
3. Configure the DLP policy action: 'Apply message encryption'.
4. Configure the DLP policy action: 'Remove message encryption (preview)'.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. Select the DLP policy you configured. Under 'Actions', verify that 'Apply HTML disclaimer' is listed with the correct disclaimer text and fallback action. 2. Confirm 'Prepend subject' is listed with the specified subject text. 3. Confirm 'Apply message encryption' is listed with the selected encryption template (e.g., 'Do Not Forward'). 4. If configured, confirm 'Remove message encryption (preview)' is listed. 5. Send a test email that triggers the policy and verify the received message includes the HTML disclaimer, the subject line is prepended, and the message is encrypted (or encryption removed as configured).

## Rollback
1. In the same DLP policy, edit the 'Actions' section. 2. Remove or disable the 'Apply HTML disclaimer' action. 3. Remove or disable the 'Prepend subject' action. 4. Remove or disable the 'Apply message encryption' action. 5. If present, remove or disable the 'Remove message encryption (preview)' action. 6. Save the policy and confirm the changes are applied. 7. Send a test email to verify the previous actions are no longer enforced.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
