# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure the Document property is condition in a DLP policy to detect documents with custom properties?

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
1. Use the Document property is condition to detect documents with custom properties matching specified values.
2. For example: Department = 'Marketing', Project = 'Secret'.
3. To specify multiple values for a custom property, use double quotes. For example, 'Department: Marketing, Sales'.
4. Supported file types are Office and PDF: Word processing (.doc, .docx, .docm, .dot, dotx, .dotm, .docb, .pdf), Spreadsheet (.xls, .xlsx, .xlt, .xlm, .xlsm, xltx, xltm, xlsb, .xlw, .csv, .tsv), Presentation (.ppt, .pptx, .pos, .pps, .pptm, .potx, .potm, .ppam, .ppsx).

## Validation
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the DLP policy that was configured with the 'Document property is' condition.
2. Click 'Edit policy' and review the rule containing the condition. Confirm that the condition is set to 'Document property is' and that the custom property name and value(s) are correctly specified (e.g., Department = 'Marketing' or Department: 'Marketing, Sales').
3. Create a test file (e.g., a Word document) that includes the custom property with the specified value(s). Save the file in a location monitored by the DLP policy.
4. Attempt to share or copy the test file in a way that would trigger the DLP policy (e.g., email, OneDrive sharing).
5. Verify that the DLP policy detects the document and generates an alert or blocks the action as configured. Check the DLP alerts page for matching incidents.
6. Optionally, use the DLP test mode (if available) to simulate the policy and confirm detection without enforcement.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the DLP policy that was modified.
2. Click 'Edit policy' and locate the rule containing the 'Document property is' condition.
3. Remove or disable the 'Document property is' condition from the rule. Alternatively, delete the entire rule if it was newly added.
4. Save the policy changes and confirm that the policy is updated.
5. Repeat the test steps from validation to ensure that the custom property detection no longer triggers the policy.
6. If the policy was previously in test mode, revert to the original enforcement mode (e.g., turn off test mode).

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
