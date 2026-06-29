# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy action to add the sender's manager as recipient?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with action 'Add the sender's manager as recipient'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the manager attribute is defined in Active Directory (AD).
2. Configure the DLP policy action: 'Add the sender's manager as recipient'.

## Validation
1. Verify that the manager attribute is populated for the sender in Active Directory (AD) or Azure AD by running: Get-ADUser -Identity <senderUPN> -Properties Manager | Select-Object Manager. 2. Confirm the DLP policy is configured with the action 'Add the sender's manager as recipient' by running: Get-DlpCompliancePolicy -Identity <PolicyName> | Format-List. 3. Send a test email containing sensitive data that triggers the DLP policy and verify that the sender's manager receives the notification or incident report.

## Rollback
1. Remove the 'Add the sender's manager as recipient' action from the DLP policy by running: Set-DlpCompliancePolicy -Identity <PolicyName> -RemoveAction 'Add the sender's manager as recipient'. 2. If the policy was newly created, delete it with: Remove-DlpCompliancePolicy -Identity <PolicyName>. 3. Revert any changes made to the sender's manager attribute in AD if it was modified for testing.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
