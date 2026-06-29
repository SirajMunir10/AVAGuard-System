# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to configure network share coverage and exclusions for endpoint DLP policies?

## Environment Context
- **Tenant Type:** Purview
- **Configuration:** Endpoint DLP policies scoped to Devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. To exclude a specific network path for all monitored devices, add the path value in Exclude these network share paths.
2. Ensure devices have the required updates: Windows 10 - March 21, 2023â€”KB5023773 (OS Builds 19042.2788, 19044.2788, and 19045.2788) Preview, March 28, 2023â€”KB5023774 (OS Build 22000.1761) Preview; Windows 11 - March 28, 2023â€”KB5023778 (OS Build 22621.1485) Preview; Microsoft Defender April-2023 (Platform: 4.18.2304.8 | Engine: 1.1.20300.3); macOS Last 3 OS versions supported; Minimum Defender app version supported - 101.24122.0005.

## Validation
1. Confirm that the network share exclusion path is listed in the 'Exclude these network share paths' setting under Endpoint DLP policy configuration. 2. On a test device, verify that DLP policy does not apply to files in the excluded network share path by attempting a restricted action (e.g., copy to USB) and confirming no policy block or notification occurs. 3. Check device compliance: run 'winver' on Windows 10/11 to confirm OS build matches KB5023773 (19042.2788, 19044.2788, 19045.2788) or KB5023774 (22000.1761) or KB5023778 (22621.1485). 4. On Windows, run 'Get-MpComputerStatus | Select-Object AMProductVersion,AMEngineVersion' to verify Defender platform >= 4.18.2304.8 and engine >= 1.1.20300.3. 5. On macOS, run 'mdatp health --field product_version' to confirm version >= 101.24122.0005.

## Rollback
1. Navigate to the Endpoint DLP policy settings and remove the network share path from 'Exclude these network share paths'. 2. If device updates caused issues, uninstall the problematic update via Control Panel > Programs > Installed Updates (e.g., KB5023773, KB5023774, KB5023778) or use 'wusa /uninstall /kb:5023773' (adjust KB number). 3. Roll back Defender platform by reinstalling a previous version from Microsoft Update Catalog or using 'MpCmdRun -RemoveDefinitions -All' and then reinstall the earlier platform version. 4. For macOS, uninstall the current Defender version and reinstall a supported earlier version from the Microsoft 365 admin center.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
