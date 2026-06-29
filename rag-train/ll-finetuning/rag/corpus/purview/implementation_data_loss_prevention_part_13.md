# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to design a DLP policy by creating a policy intent statement and mapping it to a specific policy configuration?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Purview DLP policy design

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a policy intent statement
2. Map the policy intent statement to a specific policy configuration

## Validation
1. Confirm the policy intent statement is documented and aligns with business requirements. 2. Verify the DLP policy configuration matches the intent by running: Get-DlpCompliancePolicy | Format-List Name, Mode, ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation. 3. Check that the policy is enabled and applied to the correct locations. 4. Use Get-DlpComplianceRule -Policy <PolicyName> to confirm rules reflect the intent. 5. Test the policy with a sensitive info type using the DLP test tool or by sending a test email with sample data.

## Rollback
1. Disable the DLP policy by running: Set-DlpCompliancePolicy -Identity <PolicyName> -Mode Disable. 2. Remove the policy if needed: Remove-DlpCompliancePolicy -Identity <PolicyName>. 3. Revert any location changes by updating the policy with original locations: Set-DlpCompliancePolicy -Identity <PolicyName> -ExchangeLocation $null -SharePointLocation $null -OneDriveLocation $null -TeamsLocation $null. 4. If rules were modified, restore from backup or recreate original rules using New-DlpComplianceRule. 5. Document the rollback and notify stakeholders.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
