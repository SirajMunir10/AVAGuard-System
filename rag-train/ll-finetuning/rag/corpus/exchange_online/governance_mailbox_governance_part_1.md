# Governance: Mailbox Governance

**Domain:** Exchange Online
**Subdomain:** Mailbox Governance
**Incident Type:** Governance

## Scenario / Query
An administrator notices that a user's mailbox is approaching the storage quota limit, but the user is no longer with the organization. The mailbox must be preserved for compliance purposes but should not consume active quota. What is the correct governance action?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Mailbox quotas and retention policies are configured per the organization's compliance requirements.

## Symptoms
- User mailbox is near or over the storage quota limit
- Mailbox belongs to a former employee
- Mailbox is still active and consuming licensed storage

## Error Codes
N/A

## Root Causes
1. Mailbox was not converted to a shared mailbox or placed on litigation hold/in-place hold after the user left
2. No retention policy was applied to preserve the mailbox without consuming a license

## Remediation Steps
1. Convert the user mailbox to a shared mailbox using the Exchange admin center or PowerShell (Set-Mailbox -Type Shared). This preserves the mailbox without requiring an Exchange Online license.
2. Place the shared mailbox on litigation hold or apply a retention policy to ensure compliance data is preserved.
3. Remove the Exchange Online license from the user after conversion to reduce costs.

## Validation
Verify that the mailbox appears as a shared mailbox in the Exchange admin center and that the original user can no longer sign in. Confirm that litigation hold or retention policy is active on the mailbox.

## Rollback
To revert, assign an Exchange Online license to the shared mailbox and convert it back to a user mailbox using Set-Mailbox -Type Regular.

## References
- <https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/convert-a-mailbox-to-a-shared-mailbox>
