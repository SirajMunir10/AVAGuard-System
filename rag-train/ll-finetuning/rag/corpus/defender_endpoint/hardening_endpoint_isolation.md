# Hardening: Endpoint isolation

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint isolation
**Incident Type:** Hardening

## Scenario / Query
How to configure isolation exclusions to preserve critical communications during automatic device isolation in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Devices running Windows 11, Windows 10 version 1703 or later, Windows Server 2012 R2 and later, Azure Stack HCI OS version 23H2 and later, macOS

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define selective isolation exclusions to specify which processes and network destinations remain accessible on an isolated device.
2. Define automatic attack disruption exclusions to exclude specific devices or entities from automatic disruption actions entirely.

## Validation
1. Confirm the isolation exclusion policy is applied: Run 'Get-MpPreference | Select-Object -ExpandProperty ExclusionPath' on a test device to verify the exclusion paths are present. 2. Verify network connectivity: From an isolated device, attempt to connect to an excluded destination (e.g., 'Test-NetConnection -ComputerName <excluded_FQDN> -Port 443') and confirm success. 3. Check automatic attack disruption exclusions: In the Microsoft 365 Defender portal, navigate to Settings > Endpoints > Advanced features > Automatic attack disruption and verify the excluded devices or entities are listed. 4. Simulate isolation: Use 'Start-MpWDOScan -ScanType QuickScan' or trigger a test alert to confirm the device isolates but retains access to excluded processes and destinations.

## Rollback
1. Remove isolation exclusions: Run 'Remove-MpPreference -ExclusionPath <path>' for each added exclusion path. 2. Remove automatic attack disruption exclusions: In the Microsoft 365 Defender portal, go to Settings > Endpoints > Advanced features > Automatic attack disruption and delete the excluded devices or entities. 3. If isolation was applied manually, release isolation: Use 'Stop-MpWDOScan' or in the portal, go to Device inventory > select the device > Actions > Release from isolation. 4. Verify rollback: Confirm the device is fully isolated again (no exclusions) by running 'Get-MpPreference' and checking that exclusion lists are empty.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
