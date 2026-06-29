# Implementation: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Implementation

## Scenario / Query
How to configure a retention policy or retention label for Exchange in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange Online

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you're new to configuring retention in Microsoft 365, see Get started with data lifecycle management.
2. If you're ready to configure a retention policy or retention label for Exchange, see the following instructions: Create and configure retention policies, Publish retention labels and apply them in apps, Apply a retention label to content automatically.

## Validation
1. Connect to Exchange Online PowerShell: Connect-ExchangeOnline -UserPrincipalName admin@contoso.com
2. Verify the retention policy exists: Get-RetentionCompliancePolicy | Where-Object {$_.Name -eq 'Exchange Retention Policy'}
3. Check the policy is applied to Exchange mailboxes: Get-RetentionCompliancePolicy -Identity 'Exchange Retention Policy' | Format-List ExchangeLocation
4. Confirm retention rules are active: Get-RetentionComplianceRule -Policy 'Exchange Retention Policy' | Format-List Name, Mode, RetentionDuration, RetentionAction
5. For retention labels, verify label publishing: Get-ComplianceTag | Where-Object {$_.Name -eq 'Exchange Label'} | Format-List Name, Priority, RetentionAction, RetentionDuration
6. Test label application on a sample mailbox: Get-ExoMailbox -Identity user@contoso.com | Select-Object RetentionPolicy, RetentionHoldEnabled

## Rollback
1. Remove the retention policy from Exchange locations: Set-RetentionCompliancePolicy -Identity 'Exchange Retention Policy' -ExchangeLocation $null
2. Delete the retention policy: Remove-RetentionCompliancePolicy -Identity 'Exchange Retention Policy' -Confirm:$false
3. Delete associated retention rules: Get-RetentionComplianceRule -Policy 'Exchange Retention Policy' | Remove-RetentionComplianceRule -Confirm:$false
4. For retention labels, remove the label from published policies: Remove-ComplianceTag -Name 'Exchange Label' -Confirm:$false
5. Disable retention hold on mailboxes if enabled: Set-Mailbox -Identity user@contoso.com -RetentionHoldEnabled $false
6. Verify removal: Get-RetentionCompliancePolicy | Where-Object {$_.Name -eq 'Exchange Retention Policy'}

## References
- <https://learn.microsoft.com/en-us/purview/retention-policies-exchange>
