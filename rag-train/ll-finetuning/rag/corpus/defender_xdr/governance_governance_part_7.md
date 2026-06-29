# Governance: Governance

**Domain:** Defender XDR
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
A security operations team notices that Microsoft Defender for Office 365 Safe Attachments and Safe Links policies are not being applied to all users in the tenant. Some users are receiving malicious attachments that should have been blocked. How can the team audit and enforce consistent policy application across the organization?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Safe Attachments and Safe Links policies are created but not assigned to all users; some users are in groups not covered by any policy.

## Symptoms
- Users report receiving phishing emails with malicious attachments that were not blocked
- Security team observes that Safe Attachments and Safe Links policies are not applied to all mailboxes
- Policy reports show gaps in coverage for certain distribution groups or users

## Error Codes
N/A

## Root Causes
1. Safe Attachments and Safe Links policies are scoped to specific users, groups, or domains, leaving some users unprotected
2. No default policy exists that covers all users; administrators must explicitly assign policies to all recipients

## Remediation Steps
1. Review existing Safe Attachments and Safe Links policies in the Microsoft 365 Defender portal (Policies & rules > Threat policies > Safe Attachments / Safe Links)
2. Ensure that at least one policy is scoped to 'All users' or create a new policy with the condition 'Recipient domain is *' to cover all mailboxes
3. Use the 'Get-SafeAttachmentPolicy' and 'Get-SafeLinksPolicy' PowerShell cmdlets (Exchange Online PowerShell) to list policies and their assigned scopes
4. Use 'Set-SafeAttachmentPolicy' or 'New-SafeAttachmentPolicy' to modify or create a policy with the parameter '-Enable $true' and scope to all users
5. Validate policy application by checking the 'Threat Protection Status' report in the Defender portal for coverage gaps

## Validation
Run the PowerShell command: Get-SafeAttachmentPolicy | Format-List Name,Enabled,Identity and verify that at least one policy has no scope restrictions or covers all users. Also check the 'Threat Protection Status' report for any users with 'No policy' status.

## Rollback
If the new policy causes false positives, remove the policy using Remove-SafeAttachmentPolicy -Identity 'PolicyName' or adjust the scope to exclude specific users/groups.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-about>
- <https://learn.microsoft.com/en-us/powershell/module/exchange/get-safeattachmentpolicy>
