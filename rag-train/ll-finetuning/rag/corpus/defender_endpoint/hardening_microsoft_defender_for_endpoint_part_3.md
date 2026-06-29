# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
What are the recommended configuration settings for next generation protection in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Next generation protection

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set Scan removable storage devices such as USB drives to Yes.
2. Enable Real-time Protection: Enable Behavioral Monitoring.
3. Enable protection against Potentially Unwanted Applications at download and prior to installation.
4. Set Cloud Protection Service membership type to Advanced membership.
5. Configure all available attack surface reduction rules to Audit.

## Validation
1. Verify that 'Scan removable storage devices such as USB drives' is enabled: Run PowerShell command 'Get-MpPreference | Select-Object -Property DisableRemovableDriveScanning' and confirm the value is 'False'.
2. Confirm Real-time Protection and Behavioral Monitoring are active: Run 'Get-MpPreference | Select-Object -Property DisableRealtimeMonitoring, DisableBehaviorMonitoring' and ensure both are 'False'.
3. Check PUA protection is set to block at download and prior to installation: Run 'Get-MpPreference | Select-Object -Property PUAProtection' and verify the value is '1' (Enabled).
4. Validate Cloud Protection Service membership is Advanced: Run 'Get-MpPreference | Select-Object -Property MAPSReporting' and confirm it is '2' (Advanced membership).
5. Confirm attack surface reduction rules are configured to Audit: Run 'Get-MpPreference | Select-Object -Property AttackSurfaceReductionRules_Actions' and verify each rule's action is '1' (Audit).

## Rollback
1. To revert removable drive scanning: Run 'Set-MpPreference -DisableRemovableDriveScanning $true'.
2. To disable Real-time Protection: Run 'Set-MpPreference -DisableRealtimeMonitoring $true'.
3. To disable Behavioral Monitoring: Run 'Set-MpPreference -DisableBehaviorMonitoring $true'.
4. To disable PUA protection: Run 'Set-MpPreference -PUAProtection 0'.
5. To set Cloud Protection Service to Basic or off: Run 'Set-MpPreference -MAPSReporting 0' (off) or '1' (Basic).
6. To disable attack surface reduction rules: Run 'Remove-MpPreference -AttackSurfaceReductionRules_Ids' for each rule, or set actions to '0' (Disabled).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
