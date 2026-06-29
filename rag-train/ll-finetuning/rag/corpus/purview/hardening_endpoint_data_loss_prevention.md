# Hardening: Endpoint Data Loss Prevention

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention
**Incident Type:** Hardening

## Scenario / Query
How do I configure DLP policies to restrict activities involving files with unsupported extensions while excluding specific extensions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy with 'Document could not be scanned' condition and 'Apply restrictions to only unsupported file extensions' option

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the 'Document could not be scanned' condition together with 'Apply restrictions to only unsupported file extensions' in your DLP policies.
2. Refine detection by adding unsupported extensions to exclude.
3. Do not add a '.' when you add an extension.
4. Use the latest anti-malware client version.

## Validation
1. Verify that the DLP policy includes the condition 'Document could not be scanned' and the option 'Apply restrictions to only unsupported file extensions' is enabled. 2. Confirm that the list of excluded extensions does not contain leading dots (e.g., 'txt' not '.txt'). 3. Ensure the anti-malware client version is up to date by running 'Get-MpComputerStatus | Select-Object AMProductVersion' on an endpoint. 4. Test the policy by attempting to copy an unsupported file type (e.g., .xyz) to a restricted location and confirm the action is blocked. 5. Test an excluded extension (e.g., .txt) and confirm the action is allowed.

## Rollback
1. Remove the 'Document could not be scanned' condition from the DLP policy. 2. Disable the 'Apply restrictions to only unsupported file extensions' option. 3. Clear any custom excluded extensions from the policy. 4. If the anti-malware client was updated, roll back to the previous version using 'Uninstall-WindowsFeature -Name Windows-Defender' (or reinstall the earlier version via Microsoft Update Catalog). 5. Re-test the policy to ensure unrestricted behavior is restored.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
