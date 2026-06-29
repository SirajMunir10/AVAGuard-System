# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy actions for forwarding messages to sender's manager for approval?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with action 'Forward the message for approval to sender's manager'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the sender's manager is defined in Active Directory (AD).
2. Configure the DLP policy action: 'Forward the message for approval to sender's manager'.

## Validation
1. Verify that the sender's manager is defined in Active Directory: run Get-ADUser -Identity <sender> -Properties Manager and confirm the Manager attribute is populated.
2. Confirm the DLP policy is configured with the action 'Forward the message for approval to sender's manager': run Get-DlpCompliancePolicy -Identity <policy name> | Format-List and check that the action is present.
3. Send a test email that triggers the DLP rule and verify that the message is forwarded to the sender's manager for approval.

## Rollback
1. Remove the 'Forward the message for approval to sender's manager' action from the DLP policy: run Set-DlpCompliancePolicy -Identity <policy name> -RemoveAction 'ForwardToSenderManagerForApproval'.
2. If needed, restore the previous DLP policy configuration from a backup or reapply the original actions.
3. Clear the Manager attribute in Active Directory if it was incorrectly set: run Set-ADUser -Identity <sender> -Manager $null.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
