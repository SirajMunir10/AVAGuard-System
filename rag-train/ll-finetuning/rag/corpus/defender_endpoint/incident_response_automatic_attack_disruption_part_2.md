# Incident Response: Automatic attack disruption

**Domain:** Defender for Endpoint
**Subdomain:** Automatic attack disruption
**Incident Type:** Incident Response

## Scenario / Query
How to handle automatic device isolation for business-critical devices in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When an isolation exclusion rule is defined, automatic attack disruption uses selective isolation by default and isolates the device according to the configured isolation exclusion rules.
2. If an automatically isolated device is business-critical, prioritize rapid validation and stakeholder coordination.
3. Release isolation only after you confirm appropriate containment and remediation steps are in place.
4. Consider using automatic attack disruption exclusions to reduce the likelihood of isolating devices that can't tolerate interruption.

## Validation
1. Confirm the device is no longer isolated: Run 'Get-MpPreference | Select-Object -Property DisableRealtimeMonitoring, DisableBehaviorMonitoring, DisableBlockAtFirstSeen, DisableIOAVProtection, DisablePrivacyMode, DisableScriptScanning, DisableArchiveScanning, DisableAutoExclusions, DisableCatchupFullScan, DisableCatchupQuickScan, DisableCpuThrottleOnIdle, DisableDatagramProcessing, DisableDnsOverTcpParsing, DisableEmailScanning, DisableFileScanning, DisableFtpParsing, DisableGradualRelease, DisableHttpParsing, DisableInboundConnectionFiltering, DisableNetworkProtection, DisableRdpParsing, DisableRealtimeMonitoring, DisableScriptScanning, DisableSmtpParsing, DisableSshParsing, DisableTlsParsing, DisableUdpParsing, DisableWmiScanning, IsolationState' on the device. Verify IsolationState is 0 (not isolated).
2. In Microsoft Defender XDR, navigate to Assets > Devices, search for the device, and confirm its status shows 'Active' and not 'Isolated'.
3. Review the incident timeline in Microsoft Defender XDR to ensure no new alerts or isolation actions have been triggered for the device.
4. Validate that the automatic attack disruption exclusion rule is applied: Run 'Get-MpPreference | Select-Object -Property ExclusionPath, ExclusionExtension, ExclusionProcess' on the device to confirm the exclusion is present.
5. Confirm business-critical applications are running as expected by checking application logs or performing a connectivity test to dependent services.

## Rollback
1. If the device is still isolated and needs to be re-isolated due to ongoing threat, run 'Start-MpWDOScan -ScanType QuickScan' to ensure the device is clean, then manually isolate the device via Microsoft Defender XDR: Go to Assets > Devices, select the device, and choose 'Isolate device'.
2. If the exclusion rule was removed or not applied, re-add the exclusion: Run 'Add-MpPreference -ExclusionPath "C:\Path\To\BusinessCriticalApp"' or use the appropriate exclusion type (Path, Extension, Process).
3. If the device was released from isolation prematurely and a threat is detected, immediately re-isolate the device using the Microsoft Defender XDR portal: Assets > Devices > select device > Isolate device.
4. If the automatic attack disruption exclusion rule is not working as expected, temporarily disable automatic attack disruption for the device by adding the device to the exclusion list in Microsoft Defender XDR: Settings > Endpoints > Advanced features > Automatic attack disruption > Manage exclusions.
5. If the device experiences performance issues after isolation release, run a full scan with 'Start-MpWDOScan -ScanType FullScan' and review Microsoft Defender Antivirus protection history for any missed threats.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
