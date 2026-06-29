# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure the File extension is condition in a DLP policy to monitor specific file extensions?

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
1. Add the necessary file extensions, separated by commas to a rule in your policy.
2. Note: File extension is condition is supported only for those versions of Windows that support the File type is condition.
3. Note: File extension is doesn't support archive file types.
4. Note: Including any of the following file extensions in your policy rules might significantly increase the CPU load: .dll, .exe, .mui, .ost, .pf, .pst.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the policy that was modified. 3. In the policy rule, confirm that the 'File extension is' condition is present and lists the expected file extensions (e.g., .docx, .pdf) separated by commas. 4. Use the DLP test functionality or simulate a file transfer with one of the specified extensions to verify the policy triggers an alert or blocks the action as configured. 5. Check the DLP activity explorer for matching events.

## Rollback
1. In the same DLP policy rule, remove the 'File extension is' condition or edit the list of file extensions to revert to the previous configuration. 2. If the condition was added as part of a new rule, delete that rule entirely. 3. Save the policy and confirm the change is applied. 4. Verify that the previous behavior (e.g., no alerts for those extensions) is restored by testing with a file of the previously monitored extension.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
