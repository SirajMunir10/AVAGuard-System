# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure DLP actions for on-premises repositories?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with on-premises repository actions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Block people from accessing files stored in on-premises repositories.
2. Set permissions on the file (permissions inherited from the parent folder).
3. Move file from where it's stored to a quarantine folder.

## Validation
1. Verify the DLP policy is applied to the on-premises repository by running: Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List ExchangeLocation, SharePointLocation, OneDriveLocation, OnPremisesScannerLocation. 2. Confirm the action 'Block people from accessing files stored in on-premises repositories' is enabled by checking the policy's rule actions: Get-DlpComplianceRule -Policy "PolicyName" | Select-Object -ExpandProperty Actions. 3. Test the policy by placing a sensitive file in the on-premises repository and triggering a scan; verify the file is blocked and an incident is reported in the DLP alerts dashboard. 4. For the 'Set permissions' action, check that the file's effective permissions are inherited from the parent folder after the policy enforcement. 5. For the 'Move to quarantine' action, confirm the file is moved to the specified quarantine folder path and is no longer accessible in the original location.

## Rollback
1. Remove the DLP policy actions by editing the policy: Set-DlpComplianceRule -Identity "RuleName" -RemoveAction "BlockAccess" -RemoveAction "SetPermissions" -RemoveAction "MoveToQuarantine". 2. If files were moved to quarantine, restore them to their original location using: Move-Item -Path "QuarantineFolderPath\*" -Destination "OriginalRepositoryPath". 3. Reset file permissions to inherit from parent folder: Remove-ItemPermission -Path "FilePath" -InheritanceType None; Set-ItemPermission -Path "FilePath" -InheritanceType ContainerInherit. 4. Re-enable access to the repository by ensuring the DLP policy is no longer blocking access: Set-DlpCompliancePolicy -Identity "PolicyName" -OnPremisesScannerLocation $null. 5. Monitor the DLP alerts to ensure no further false positives are generated.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
