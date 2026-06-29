# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Information Barriers policy application failure due to Exchange address book policies?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange address book policies

## Symptoms
- Information Barriers policies are not being applied

## Error Codes
N/A

## Root Causes
1. Exchange address book policies are in place and preventing Information Barriers policies from being applied

## Remediation Steps
1. Connect to Exchange Online PowerShell
2. Run the Get-AddressBookPolicy cmdlet and review the results
3. If Exchange address book policies are listed, remove the address book policies
4. If no address book policies exist, review audit logs to determine why the policy application failed

## Validation
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline. 2. Run Get-AddressBookPolicy to confirm no address book policies exist. 3. Run Get-InformationBarrierPolicy and Get-InformationBarrierRecipientStatus to verify that Information Barriers policies are applied and active. 4. Check audit logs for any remaining policy application failures.

## Rollback
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline. 2. If address book policies were removed, reapply them using Set-Mailbox -AddressBookPolicy <PolicyName> for each affected mailbox. 3. Verify address book policies are restored with Get-AddressBookPolicy and Get-Mailbox | Format-List AddressBookPolicy. 4. Monitor Information Barriers policy application status to ensure no conflicts.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
