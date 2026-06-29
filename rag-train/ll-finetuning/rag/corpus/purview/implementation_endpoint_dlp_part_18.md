# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to configure auto-quarantine for cloud sync apps like OneDrive to prevent sensitive items from syncing to the cloud?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy with blocking action

## Symptoms
- Repeated DLP notifications for users and admins
- Sensitive items syncing to cloud via cloud sync apps such as onedrive.exe

## Error Codes
N/A

## Root Causes
1. Unallowed cloud-sync app attempting to access a DLP-protected sensitive item
2. Endless chain of DLP notifications due to repeated access attempts

## Remediation Steps
1. Add the cloud sync app (e.g., onedrive.exe) to the Restricted apps list with Auto-quarantine
2. Configure auto-quarantine to move the sensitive item to an admin-configured folder
3. Optionally configure a placeholder (.txt) file to inform users of the new location and other pertinent information

## Validation
1. Verify that the cloud sync app (e.g., onedrive.exe) is listed in the Restricted apps list under Endpoint DLP settings: navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Restricted apps and confirm the app is present with 'Auto-quarantine' enabled.
2. Attempt to sync a sensitive item (e.g., a file containing a credit card number) via the restricted app from a test device. Confirm that the file is automatically moved to the admin-configured quarantine folder (e.g., %userprofile%\Documents\Quarantine) and that a placeholder .txt file is created in the original location with the configured notification message.
3. Check the DLP activity explorer for the test event: verify that the action is 'Blocked' and the secondary action is 'Auto-quarantined' for the restricted app.
4. Confirm that no new DLP notifications are generated for the user or admin for the quarantined item.

## Rollback
1. Remove the cloud sync app from the Restricted apps list: navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Restricted apps, select the app (e.g., onedrive.exe), and click 'Remove'.
2. If auto-quarantine was configured with a custom quarantine folder, revert to the default quarantine folder or delete the custom folder path in the settings.
3. If a placeholder .txt file was configured, disable the placeholder option in the auto-quarantine settings.
4. To restore any previously quarantined items, manually move them from the quarantine folder back to their original locations using File Explorer or a script.
5. Verify that the app can now sync files without triggering DLP blocking or auto-quarantine by performing a test sync of a non-sensitive file.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
