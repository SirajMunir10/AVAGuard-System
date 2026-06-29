# Implementation: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How do I configure the 'Apply restrictions to only unsupported file extensions' option in a DLP policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with 'Audit or restrict activities on devices' action selected

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the 'Audit or restrict activities on devices' action in the DLP policy.
2. The 'Apply restrictions to only unsupported file extensions' configuration option will appear.
3. Note: This configuration option does NOT support scoping by Device and device groups in the policy location setting.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Open the DLP policy that was configured. 3. Under 'Actions', confirm that 'Audit or restrict activities on devices' is selected. 4. Verify that the 'Apply restrictions to only unsupported file extensions' option is visible and set to the desired state (e.g., On or Off). 5. Use the Get-DlpCompliancePolicy cmdlet in Exchange Online PowerShell to confirm the policy settings: Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List Name, Mode, ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation, EndpointDlpLocation, RestrictUnsupportedFileExtensions. 6. Check that the policy is applied to the intended locations (e.g., devices) and that no unintended scope restrictions exist.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, edit the DLP policy. 2. Under 'Actions', deselect 'Audit or restrict activities on devices' to remove the option entirely, or set 'Apply restrictions to only unsupported file extensions' to its previous state (e.g., Off). 3. Save the policy and wait for replication (up to 1 hour). 4. Use Set-DlpCompliancePolicy in Exchange Online PowerShell to revert the setting: Set-DlpCompliancePolicy -Identity "PolicyName" -RestrictUnsupportedFileExtensions $false. 5. Confirm the change with Get-DlpCompliancePolicy as in validation step 5. 6. If the policy was causing issues, consider disabling it temporarily: Set-DlpCompliancePolicy -Identity "PolicyName" -Mode Disable.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
