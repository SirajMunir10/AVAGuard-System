# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I detect content that does not have a sensitivity label applied using a DLP policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with 'Content is not labeled' condition

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the 'Content is not labeled' condition to detect content that doesn't have a sensitivity label applied.
2. To help ensure only supported file types are detected, use this condition with the 'File extension is' or 'File type is' conditions.
3. Supported file types include Word processing (Word, PDF) with extensions .doc, .docx, .docm, .dot, .dotx, .dotm, .docb, .pdf; Spreadsheet (Excel, CSV, TSV) with extensions .xls, .xlsx, .xlt, .xlm, .xlsm, .xltx, .xltm, .xlsb, .xlw, .csv, .tsv; Presentation (PowerPoint) with extensions .ppt, .pptx, .pos, .pps, .pptm, .potx, .potm, .ppam, .ppsx.

## Validation
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the DLP policy that includes the 'Content is not labeled' condition. 2. Confirm that the condition 'Content is not labeled' is present in the policy rule. 3. Verify that the policy also includes a 'File extension is' or 'File type is' condition with supported file types (e.g., .docx, .pdf, .xlsx, .pptx). 4. Use the DLP policy test functionality (if available) to simulate a document without a sensitivity label and confirm it triggers the policy. 5. Check the DLP activity explorer for recent events matching the policy to ensure detection is occurring.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the DLP policy that was modified. 2. Remove the 'Content is not labeled' condition from the policy rule. 3. If the 'File extension is' or 'File type is' condition was added, remove it as well. 4. Save the policy changes. 5. Monitor the DLP activity explorer to confirm that the policy no longer triggers on unlabeled content.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
