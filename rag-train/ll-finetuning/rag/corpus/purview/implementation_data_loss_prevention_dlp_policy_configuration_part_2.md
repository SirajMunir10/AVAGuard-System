# Implementation: Data Loss Prevention (DLP) Policy Configuration

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP) Policy Configuration
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy conditions using file extension detection?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy rules with file extension condition

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the 'File extension is' condition to detect sensitive information in files with any file extension.
2. Add the necessary file extensions, separated by commas, to a rule in your policy.
3. Note: 'File extension is' is supported only for Windows versions that support the 'File type is' condition.
4. Warning: Including .dll, .exe, .mui, .ost, .pf, .pst extensions might significantly increase CPU load.
5. Note: 'File extension is' does not support archive file types.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Open the DLP policy that was configured. 3. Select the rule containing the 'File extension is' condition. 4. Verify that the condition is set to 'File extension is' and the list of extensions (e.g., .docx, .xlsx) matches the intended configuration. 5. Create a test file with one of the specified extensions containing sensitive data (e.g., credit card number). 6. Attempt to share or copy the test file to an unauthorized location (e.g., external email, USB drive). 7. Confirm that the DLP policy blocks or alerts on the action as expected. 8. Review DLP activity reports in the compliance portal to ensure the test event is logged.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Open the DLP policy that was modified. 3. Select the rule containing the 'File extension is' condition. 4. Remove the condition entirely or replace it with the previous condition (e.g., 'File type is' if originally used). 5. If the policy was newly created, delete the policy. 6. Save the policy changes. 7. Re-test with the same test file to confirm the DLP action no longer triggers for the file extension condition. 8. Monitor DLP activity reports for any unexpected blocks or alerts.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
