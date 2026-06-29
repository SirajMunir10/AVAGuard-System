# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot high CPU utilization caused by Microsoft Defender Antivirus when binaries are not digitally signed?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender Antivirus real-time protection, scheduled scans, on-demand scans

## Symptoms
- Higher CPU utilization by Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
1. Binaries (such as .exe, .dll) are not digitally signed, triggering real-time protection scans, scheduled scans, or on-demand scans

## Remediation Steps
1. Consider signing the binaries using an internal PKI
2. Reach out to the vendor so they could sign the binary
3. Add the certificate to the Indicators – Certificate - allow
4. As a work-around: (Preferred) For .exe's and dll's use Indicators – File hash - allow
5. As a work-around: (Alternative) Add Antivirus exclusions (process+path)

## Validation
1. Verify that the binaries are now digitally signed: run `Get-AuthenticodeSignature -FilePath <path_to_binary>` for each previously unsigned binary. Confirm that Status shows 'Valid' and SignerCertificate matches the internal PKI or vendor certificate.
2. If using certificate indicator: In Microsoft 365 Defender portal, go to Settings > Endpoints > Indicators > Certificate, confirm the certificate hash is listed with action 'Allow' and scope set appropriately.
3. If using file hash indicator: In Microsoft 365 Defender portal, go to Settings > Endpoints > Indicators > File hash, confirm the file hash is listed with action 'Allow'.
4. If using exclusions: In Windows Security app or via Group Policy, confirm the exclusion paths/processes are listed under Virus & threat protection settings > Exclusions.
5. Monitor CPU usage: Run `Get-CimInstance -ClassName Win32_PerfFormattedData_PerfOS_Processor | Select-Object Name, PercentProcessorTime` or use Performance Monitor to confirm CPU utilization has returned to baseline.
6. Check Microsoft Defender Antivirus scan logs: Run `Get-MpThreatDetection` and `Get-MpComputerStatus` to confirm no recent detections on the signed binaries or excluded items.

## Rollback
1. Remove the allowed certificate indicator: In Microsoft 365 Defender portal, go to Settings > Endpoints > Indicators > Certificate, select the added indicator and click 'Remove'.
2. Remove the allowed file hash indicator: In Microsoft 365 Defender portal, go to Settings > Endpoints > Indicators > File hash, select the added indicator and click 'Remove'.
3. Remove antivirus exclusions: In Windows Security app or via Group Policy, delete the exclusion paths/processes added as a workaround.
4. If binaries were signed with an internal PKI, revoke the signing certificate if necessary, or revert to the original unsigned binaries.
5. Re-enable real-time protection if it was temporarily disabled: Run `Set-MpPreference -DisableRealtimeMonitoring $false`.
6. Monitor CPU usage again to confirm that high CPU utilization returns (indicating rollback is effective) and then proceed with alternative remediation.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-performance-issues>
