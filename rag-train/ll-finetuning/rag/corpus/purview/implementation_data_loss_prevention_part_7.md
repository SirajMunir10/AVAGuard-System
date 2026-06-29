# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I create a removable USB device group in Microsoft Purview DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open the Microsoft Purview portal and go to Data Loss Prevention > Overview > settings gear icon in the upper right corner > Data Loss Prevention > Endpoint DLP settings > Removable USB device groups.
2. Select + Create removable storage device group.
3. Enter a Group name.
4. Select Add removable storage device.
5. Enter an Alias.
6. Select the parameters and enter the values to clearly identify the specific device.
7. Select Add.
8. Add other devices to the group as needed.
9. Select Save and then Close.

## Validation
1. Navigate to Microsoft Purview portal > Data Loss Prevention > Settings (gear icon) > Data Loss Prevention > Endpoint DLP settings > Removable USB device groups.
2. Confirm the newly created group appears in the list with the expected name.
3. Select the group and verify that the alias, parameters, and values match the intended configuration.
4. Optionally, run a test by connecting a USB device that matches the defined parameters and confirm that the DLP policy applies as expected (e.g., via audit logs or policy simulation).

## Rollback
1. Navigate to Microsoft Purview portal > Data Loss Prevention > Settings (gear icon) > Data Loss Prevention > Endpoint DLP settings > Removable USB device groups.
2. Select the group you created.
3. Click 'Delete' or the delete icon to remove the group.
4. Confirm the deletion when prompted.
5. Verify the group no longer appears in the list.
6. If the group was already in use by a DLP policy, edit that policy to remove the reference to the deleted group.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
