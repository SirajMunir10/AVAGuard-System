# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure the 'Disable classification' setting in Endpoint DLP to exclude specific file extensions from classification?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Add a file extension to the 'Disable classification' setting without a leading dot (e.g., 'txt' not '.txt').
2. Files with the added extension will not be scanned by Endpoint DLP for content classification.
3. Policy evaluation based on content of those files will not occur.
4. Content information for investigations will not be visible for those files.

## Validation
1. Confirm the 'Disable classification' setting is configured: Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > 'Disable classification' section. Verify that the file extension (e.g., 'txt') appears in the list without a leading dot.
2. Test that files with the added extension are not classified: On an onboarded Windows 10/11 device, create a file with the excluded extension (e.g., 'test.txt') containing sensitive content (e.g., credit card number). Copy the file to a USB drive or cloud storage. Confirm that no DLP policy match or audit event is generated for that file.
3. Verify that other file extensions are still classified: Repeat step 2 with a file of a different extension (e.g., 'test.docx') containing the same sensitive content. Confirm that a DLP policy match and audit event are generated.
4. Check investigation content: In Microsoft 365 Defender > Incidents & alerts, open an incident related to a DLP policy for a non-excluded file. Verify that the 'Content' tab shows the actual sensitive content. For the excluded file type, confirm that no content details are available.

## Rollback
1. Remove the file extension from the 'Disable classification' list: In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > 'Disable classification' section, delete the added extension (e.g., 'txt') from the list.
2. Confirm removal: Verify that the extension no longer appears in the list.
3. Test that files with the previously excluded extension are now classified: Repeat validation step 2 using a file with the previously excluded extension (e.g., 'test.txt') containing sensitive content. Confirm that a DLP policy match and audit event are generated.
4. Verify that content investigation is restored: Repeat validation step 4 for the previously excluded file type and confirm that content details are now visible.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
