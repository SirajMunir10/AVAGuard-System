# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve '$(build.sense.productDisplayName) service failed to request to stop itself after offboarding process'?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- $(build.sense.productDisplayName) service failed to request to stop itself after offboarding process
- Failure code: %1

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Verify that the service start type is manual
2. Reboot the device

## Validation
1. Open an elevated Command Prompt and run: sc query sense
2. Confirm that the 'START_TYPE' field shows 'DEMAND_START' (manual).
3. Check the latest Sense event in the System log: Get-WinEvent -LogName System | Where-Object { $_.ProviderName -eq 'Sense' -and $_.Id -eq 1 } | Format-List TimeCreated, Message
4. Verify no recent 'service failed to request to stop' errors appear in the Sense operational log: Get-WinEvent -LogName 'Microsoft-Windows-Sense/Operational' -MaxEvents 10 | Where-Object { $_.LevelDisplayName -eq 'Error' }

## Rollback
1. If the service start type was changed incorrectly, revert to its original value using: sc config sense start= <original_start_type>
2. If a reboot caused other issues, perform a system restore to a point before the change: rstrui.exe
3. If the device fails to boot after reboot, boot into Safe Mode and reset the service start type to its previous state via Services.msc or sc config sense start= auto
4. Re-enable any startup items or services that were disabled during troubleshooting.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
