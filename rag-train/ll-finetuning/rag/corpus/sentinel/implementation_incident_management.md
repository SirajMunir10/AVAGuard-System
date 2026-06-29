# Implementation: Incident Management

**Domain:** Sentinel
**Subdomain:** Incident Management
**Incident Type:** Implementation

## Scenario / Query
How to add comments to incidents in Microsoft Sentinel with supported formats and limitations?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel incident comments

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Comments support text inputs in plain text, basic HTML, and Markdown.
2. You can paste copied text, HTML, and Markdown into the comment window.
3. Insert links to images in comments; images must be hosted in a publicly accessible location such as Dropbox, OneDrive, Google Drive. Images cannot be uploaded directly.
4. A single comment can contain up to 30,000 characters.
5. A single incident can contain up to 100 comments.
6. Only the author of a comment has permission to edit it.
7. Only users with the Microsoft Sentinel Contributor role have permission to delete comments. Even the comment's author must have this role to delete it.

## Validation
1. Open the Microsoft Sentinel incident in the Azure portal. 2. In the incident details pane, scroll to the 'Comments' section. 3. Add a new comment containing plain text, basic HTML (e.g., <b>bold</b>), and Markdown (e.g., **bold**). 4. Verify the comment displays correctly with formatting applied. 5. Paste a link to an image hosted in a publicly accessible location (e.g., Dropbox, OneDrive, Google Drive) into the comment and confirm the image renders. 6. Attempt to upload an image directly and confirm the upload option is not available. 7. Create a comment with exactly 30,000 characters and verify it is accepted. 8. Attempt to create a comment with 30,001 characters and confirm it is rejected. 9. Add comments until the incident has 100 comments, then attempt to add a 101st comment and confirm it is rejected. 10. As a user without the Microsoft Sentinel Contributor role, attempt to delete a comment you authored and confirm the delete option is not available. 11. As a user with the Microsoft Sentinel Contributor role, delete a comment authored by another user and confirm the deletion succeeds.

## Rollback
1. If a comment contains incorrect or sensitive information, the author can edit the comment by clicking the edit icon next to the comment. 2. If a comment needs to be removed entirely, a user with the Microsoft Sentinel Contributor role can delete the comment by clicking the delete icon. 3. If an image link is broken or points to an unauthorized location, edit the comment to remove or replace the link. 4. If too many comments have been added, delete unnecessary comments (requires Microsoft Sentinel Contributor role) to reduce the count below 100. 5. If a comment exceeds the 30,000-character limit, edit the comment to shorten it. 6. If formatting is incorrect, edit the comment to correct the HTML or Markdown syntax.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
