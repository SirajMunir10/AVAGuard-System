# Implementation: Data Loss Prevention (DLP) Policy Configuration

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP) Policy Configuration
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy conditions for file size and file type detection?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy rules

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set the condition to detect items that are larger than 10KB.
2. Use 'Document size equals or is greater than' to detect documents with file sizes equal to or greater than the specified value.
3. Note: DLP only supports content inspection for files less than 64 MB.
4. Use 'File type is' to detect specific file types such as Word, PDF, Excel, CSV, TSV, PowerPoint, and Outlook .msg.
5. Ensure that 'File type is' and 'File extension is' conditions are not used in the same rule; they must be in separate rules.
6. For 'File type is', the following Windows versions are required: Windows 10 (21H2, 22H2) for X64, Windows 11 (21H2, 22H2) for ARM64.
7. For 'File extension is', add necessary file extensions separated by commas.
8. Avoid including .dll, .exe, .mui, .ost, .pf, .pst extensions as they may significantly increase CPU load.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. Select the DLP policy you configured. Under 'Rules', verify that a condition 'Document size equals or is greater than' is set to 10 KB. 2. Confirm that the rule includes a condition 'File type is' with the desired file types (e.g., Word, PDF, Excel). 3. Ensure that 'File type is' and 'File extension is' are not present in the same rule; if both are needed, they must be in separate rules. 4. Run a test by uploading a file larger than 10 KB and of a specified type (e.g., a 15 KB PDF) to a monitored location (e.g., SharePoint). Verify that the DLP policy triggers an incident or action as expected. 5. Upload a file smaller than 10 KB (e.g., 5 KB) of the same type and confirm no policy match occurs. 6. Upload a file larger than 64 MB (e.g., 70 MB) and verify that content inspection is not performed (DLP does not support content inspection for files >= 64 MB).

## Rollback
1. In the same DLP policy, edit the rule that contains the 'Document size equals or is greater than' condition and remove or adjust the size threshold (e.g., set to 0 or delete the condition). 2. If 'File type is' condition was added, remove it from the rule. 3. If 'File extension is' was used in a separate rule, delete that rule or remove the extensions. 4. Save the policy changes and wait for replication (up to 1 hour). 5. Re-test by uploading files of various sizes and types to confirm that the policy no longer matches as before.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
