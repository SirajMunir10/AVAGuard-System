# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to define removable USB device groups in Microsoft Purview Endpoint DLP to assign different policy actions for specific storage devices?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Windows 10 and later (21H1, 21H2) with KB 5018482, Windows 11 21H2, 22H2 with KB 5018483, Windows 10 RS5 (KB 5006744), Windows Server 2022

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create up to 20 groups of removable storage devices, with up to 50 devices per group.
2. Define groups using parameters: Storage device friendly name (supports wildcards), USB product ID, USB vendor ID, Serial number ID (supports wildcards), Device ID (supports wildcards), Instance path ID (supports wildcards), Hardware ID (supports wildcards).
3. Get the Friendly name value from the storage device property details in device manager.
4. Get the Device Instance path value from the USB device property details in device manager and convert it to Product ID and Vendor ID format (see Standard USB identifiers).
5. Get the serial number ID value from the storage device property details in device manager.
6. Get the device ID value from the storage device property details in device manager.
7. Get the hardware ID value from the storage device property details in device manager.

## Validation
1. In Microsoft Purview compliance portal, navigate to Endpoint DLP settings and confirm the device group is listed under 'Removable storage device groups'. 2. Verify the group contains the correct devices by checking the parameters (friendly name, product ID, vendor ID, serial number, device ID, instance path ID, hardware ID) against the actual device properties in Device Manager. 3. Run a test by connecting a USB device that matches the group criteria and confirm the expected DLP policy action is applied (e.g., block or audit). 4. Use Get-DlpRemovableStorageDeviceGroup PowerShell cmdlet (if available) to programmatically verify group membership.

## Rollback
1. In Microsoft Purview compliance portal, navigate to Endpoint DLP settings and delete the newly created removable storage device group. 2. If the group was edited, restore the previous configuration by re-adding the original devices or reverting to a backup of the DLP policy. 3. Verify that the DLP policy actions revert to the default behavior for the affected devices. 4. If the issue persists, restore the entire Endpoint DLP policy from a backup or reconfigure the policy to exclude the problematic group.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
