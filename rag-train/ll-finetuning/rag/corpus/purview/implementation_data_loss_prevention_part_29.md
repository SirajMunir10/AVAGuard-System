# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to scope DLP policies using distribution groups and security groups for Exchange location?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange location scope calculation

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you choose to include specific distribution groups in Exchange, the DLP policy is scoped to the emails sent by members of that group or sent to members of that group.
2. Similarly, excluding a distribution group excludes all the emails sent by the members of that distribution group or from policy evaluation.
3. Non-Mail Enabled Security Groups are enabled for specific customers only.
4. Use Non-Mail Enabled Security Groups, Mail-Enabled Security Groups, Distribution Groups, Microsoft 365 Groups, or Adaptive Scopes to define inclusion and exclusion scopes.
5. Policy is applied to included scopes; out of scope means policy isn't applied.

## Validation
1. Verify that the DLP policy is applied to the intended distribution group by sending a test email from a member of the included group to an external recipient containing sensitive data (e.g., credit card number). Confirm the email is blocked or flagged in the DLP reports. 2. Verify exclusion by sending a similar email from a member of the excluded distribution group and confirm the email is delivered without DLP action. 3. For non-mail-enabled security groups, confirm the policy scope includes/excludes members by checking the DLP policy match results in the Microsoft 365 Defender portal under Data Loss Prevention > Policies > [Policy Name] > Policy matches. 4. Use the Exchange admin center or PowerShell to confirm the distribution group membership matches the intended scope.

## Rollback
1. Remove the distribution group or security group from the DLP policy scope by editing the policy in the Microsoft 365 Defender portal: Data Loss Prevention > Policies > [Policy Name] > Edit policy > Locations > Exchange > Edit included/excluded groups. 2. If the policy was newly created, delete the policy entirely. 3. For PowerShell, use Remove-DlpCompliancePolicy -Identity "PolicyName" to delete the policy, or Set-DlpCompliancePolicy -Identity "PolicyName" -ExchangeLocation @() to clear all Exchange locations. 4. Monitor for any unintended data exfiltration or policy gaps after rollback.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
