# Governance: Mailbox Governance

**Domain:** Exchange Online
**Subdomain:** Mailbox Governance
**Incident Type:** Governance

## Scenario / Query
How can I identify and remediate Exchange Online mailboxes that have no retention policy applied, potentially leading to data loss or non-compliance?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Mailbox retention policies are not assigned to all users; default MRM policy may be missing or removed.

## Symptoms
- Mailboxes are not subject to any retention or archive policy
- Users can delete emails without any retention hold
- Litigation hold or eDiscovery searches may miss data due to premature deletion

## Error Codes
N/A

## Root Causes
1. New mailboxes created without a retention policy assignment
2. Retention policy removed from a mailbox without replacement
3. Default MRM policy not applied at tenant level

## Remediation Steps
1. Run Get-Mailbox -ResultSize unlimited | Where-Object {$_.RetentionPolicy -eq $null} to list mailboxes without a retention policy
2. Assign a retention policy using Set-Mailbox -Identity <MailboxIdParameter> -RetentionPolicy <PolicyName>
3. Ensure the default MRM policy is set via Set-OrganizationConfig -DefaultMrMPolicy <PolicyName>

## Validation
Run Get-Mailbox -ResultSize unlimited | Where-Object {$_.RetentionPolicy -eq $null} again and confirm the count is zero.

## Rollback
Re-run Set-Mailbox -Identity <MailboxIdParameter> -RetentionPolicy $null to remove the policy assignment if needed.

## References
- <https://learn.microsoft.com/en-us/powershell/module/exchange/get-mailbox>
- <https://learn.microsoft.com/en-us/powershell/module/exchange/set-mailbox>
- <https://www.cisecurity.org/benchmark/microsoft_365>
