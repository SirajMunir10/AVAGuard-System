# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to export or download message details from Communication Compliance for archiving outside of Microsoft 365?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy with policy matches

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select one or more policy matches and then select Download in the bar over the list to automatically add the selected messages to a .zip file that you can save in storage outside of Microsoft 365.
2. To download messages that cumulatively exceed 3 MB in size, use Export files (displayed in the upper-right corner of the Policies page).
3. Select the policy matches you want to export, select Export files, and then select the list of documents or users you want to export, or select Export files and then select the documents, users, and date ranges that you want to export.
4. After you select Export, it takes a few minutes for the job to complete. You receive an email notification with a link to the Exports tab when the export is ready to download.
5. To download a file that has a Ready to download status, select the files batch in the Name list, then select Download export(s) over the list.
6. To include attachments in exported files, you must select them manually in the list of policy matches. They are not automatically included with their parent message file.
7. You can also create and download a Message details report.

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy that had matches. 3. In the list of policy matches, select one or more messages. 4. Verify that the 'Download' button in the bar above the list is enabled and click it. 5. Confirm that a .zip file is downloaded containing the selected messages. 6. For messages cumulatively exceeding 3 MB, click 'Export files' in the upper-right corner of the Policies page. 7. Select the policy matches, choose 'Export files', and specify the documents, users, or date ranges. 8. After export, check for an email notification with a link to the Exports tab. 9. In the Exports tab, verify the file batch has a 'Ready to download' status. 10. Select the batch and click 'Download export(s)' to confirm the file downloads. 11. Optionally, create and download a Message details report to verify the report includes the expected message details.

## Rollback
1. If the downloaded .zip file contains incorrect or incomplete messages, delete the file from the external storage location. 2. Re-download the correct messages by repeating the selection and download steps. 3. If an export job fails or produces errors, cancel the export job from the Exports tab (if supported) or wait for it to complete and delete the resulting file. 4. Re-initiate the export with corrected parameters (e.g., different date range or user selection). 5. If the Message details report is incorrect, delete the report and generate a new one with the correct filters. 6. Ensure no sensitive data remains in temporary locations (e.g., browser downloads folder) after deletion.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
