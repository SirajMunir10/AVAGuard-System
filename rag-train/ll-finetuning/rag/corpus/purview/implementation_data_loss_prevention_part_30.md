# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How does DLP policy scoping work when mixing users and groups in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy scoping for Exchange, OneDrive, and other locations

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When scoping a policy to only users, DLP takes the union of the specified users.
2. When scoping a policy to only groups, DLP takes the union of the specified groups.
3. When users and groups are mixed, DLP evaluates the union of group membership, then the union of users, then the intersection of group members and users, and applies the policy scope to that intersection.
4. To include more than 100 users, put those users in distribution groups or security groups and scope the policy to up to 50 groups.
5. To include a few individual users not in groups, put those individuals into a group of their own to ensure the policy is scoped to all intended users.

## Validation
1. Verify that the DLP policy is scoped to the intended users by running: Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List ExchangeLocation, OneDriveLocation, SharePointLocation, TeamsLocation. 2. Confirm that the policy applies only to the intersection of group members and individually specified users by checking the effective scope using: Get-DlpComplianceRule -Policy "PolicyName" | Select-Object Name, Location, UserScope. 3. For policies with mixed scoping, ensure that users not in any group are excluded by reviewing group membership with: Get-DistributionGroupMember -Identity "GroupName" | Format-Table DisplayName. 4. Validate that the policy is enforced on the correct locations by testing with a sample user in the intersection using: Test-DlpPolicy -PolicyName "PolicyName" -UserPrincipalName "user@domain.com".

## Rollback
1. Remove the mixed scoping by setting the policy to scope only to groups: Set-DlpCompliancePolicy -Identity "PolicyName" -ExchangeLocation $null -ExchangeLocationException $null -OneDriveLocation $null -OneDriveLocationException $null -SharePointLocation $null -SharePointLocationException $null -TeamsLocation $null -TeamsLocationException $null -AddExchangeLocation "All" -AddOneDriveLocation "All" -AddSharePointLocation "All" -AddTeamsLocation "All". 2. If the policy was scoped to specific users, revert to a group-only scope by removing individual user entries: Set-DlpCompliancePolicy -Identity "PolicyName" -RemoveExchangeLocation "user@domain.com" -RemoveOneDriveLocation "user@domain.com". 3. Recreate the policy with only group scoping if needed: New-DlpCompliancePolicy -Name "PolicyName" -ExchangeLocation "Group1","Group2" -OneDriveLocation "Group1","Group2" -SharePointLocation "Group1","Group2" -TeamsLocation "Group1","Group2". 4. If the policy caused unintended exclusions, disable the policy temporarily: Set-DlpCompliancePolicy -Identity "PolicyName" -Enabled $false.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
