# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
What are the default settings for network share coverage and exclusions in endpoint DLP?

## Environment Context
- **Tenant Type:** Purview
- **Configuration:** Default settings for network share coverage and exclusions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. DLP policies scoped to Devices are applied to all network shares and mapped drives that the device connects to. Supported actions: Devices.
2. Just-in-time protection is applied only to the files on storage devices that are local to the endpoint.
3. DLP policies scoped to Devices are applied to all network shares and mapped drives that the device connects to. Supported actions: Devices.
4. Just-in-time protection is applied to all network shares and mapped drives that the device connects to.

## Validation
1. Confirm that endpoint DLP settings are configured to apply to all network shares and mapped drives by reviewing the 'Network share coverage' setting in the Microsoft Purview compliance portal under Endpoint DLP settings. 2. Verify that just-in-time protection is enabled for network shares and mapped drives by checking the 'Just-in-time protection' configuration. 3. Run a test DLP policy on a device connected to a network share and confirm that policy actions (e.g., audit, block) are enforced on files accessed via that share. 4. Use the Get-DlpConfiguration PowerShell cmdlet (if available) to export and review the current network share coverage and exclusion settings.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Endpoint DLP settings and disable 'Network share coverage' to revert to default behavior where DLP policies are not applied to network shares. 2. Disable 'Just-in-time protection' for network shares and mapped drives if it was enabled. 3. If exclusions were added, remove any custom exclusion paths for network shares. 4. Re-run the test DLP policy to confirm that network shares are no longer covered by DLP enforcement.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
