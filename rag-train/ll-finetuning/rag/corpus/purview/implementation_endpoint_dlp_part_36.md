# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I create a removable storage device group in Microsoft Purview DLP using hardware IDs and aliases?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Endpoint DLP configured with device management

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Get the hardware ID value from the storage device property details in device manager.
2. Create a removable storage device group named Backup.
3. Add individual devices by their friendly name as aliases (e.g., backup_drive_001, backup_drive_002).
4. Multiselect the parameters to include all devices that satisfy those parameters.
5. Assign policy actions to the group in a DLP policy: Allow (audit with no user notifications or alerts), Audit only (you can add notifications and alerts), Block with override (blocks the action, but the user can override), or Block (blocks no matter what).

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Device groups. 2. Confirm the 'Backup' removable storage device group exists. 3. Verify the group includes the hardware IDs and aliases (e.g., backup_drive_001, backup_drive_002) as configured. 4. In a DLP policy, assign the 'Backup' group to a rule and set an action (e.g., 'Allow' or 'Block'). 5. On an endpoint device, connect a removable storage device matching the hardware ID and alias. 6. Attempt a DLP-restricted action (e.g., copy sensitive file to the device). 7. Verify the expected DLP action occurs (e.g., file copy allowed with audit event, or blocked). 8. Check DLP activity explorer for the corresponding audit event.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Device groups, select the 'Backup' group. 2. Remove any hardware IDs or aliases that were added. 3. Delete the 'Backup' device group entirely. 4. In any DLP policy that references the 'Backup' group, remove the rule or change the action to 'Block' to prevent unintended access. 5. On test endpoints, disconnect the removable storage device and verify no DLP restrictions remain for that device. 6. Monitor DLP activity explorer for any unexpected audit events and adjust as needed.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
