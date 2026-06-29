# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How to calculate Exchange location scope when using distribution groups for inclusion and exclusion?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange location scope calculation example

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Consider an example with four users in your org and two distribution groups used for defining Exchange location inclusion and exclusion scopes.
2. The policy is applied to included scopes; out of scope means policy isn't applied.

## Validation
1. Confirm the membership of the two distribution groups used for inclusion and exclusion scopes. Run: Get-DistributionGroupMember -Identity "InclusionGroup" | Select-Object Name, RecipientTypeDetails. 2. Run: Get-DistributionGroupMember -Identity "ExclusionGroup" | Select-Object Name, RecipientTypeDetails. 3. Verify the four users in the org: Get-Mailbox | Where-Object { $_.RecipientTypeDetails -eq 'UserMailbox' } | Select-Object Name, PrimarySmtpAddress. 4. Determine which users are in the inclusion group but not in the exclusion group. For example, if UserA and UserB are in InclusionGroup, and UserB is also in ExclusionGroup, then UserA is in scope. 5. Confirm the DLP policy is applied to the calculated scope by checking the policy's Exchange location: Get-DlpCompliancePolicy -Identity "PolicyName" | Select-Object ExchangeLocation, ExchangeSenderLocation, ExchangeLocationException.

## Rollback
1. Remove the inclusion scope from the DLP policy: Set-DlpCompliancePolicy -Identity "PolicyName" -ExchangeLocation @(). 2. Remove the exclusion scope: Set-DlpCompliancePolicy -Identity "PolicyName" -ExchangeLocationException @(). 3. Re-add the original Exchange location scope if needed: Set-DlpCompliancePolicy -Identity "PolicyName" -ExchangeLocation "All". 4. Verify the policy scope is restored: Get-DlpCompliancePolicy -Identity "PolicyName" | Select-Object ExchangeLocation, ExchangeLocationException.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
