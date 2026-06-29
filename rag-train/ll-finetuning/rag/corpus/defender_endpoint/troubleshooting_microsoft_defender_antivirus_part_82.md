# Troubleshooting: Microsoft Defender Antivirus (0x80501107)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80501107 with message MP_ERROR_TEST_INDUCED_ERROR in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80501107 displayed
- Message displayed: MP_ERROR_TEST_INDUCED_ERROR

## Error Codes
- `0x80501107`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that no new event with ID 1006, 1007, or 1008 related to error 0x80501107 appears after remediation.
4. Run the following PowerShell command to check the current status of Microsoft Defender Antivirus:
   Get-MpComputerStatus | Select-Object AMProductVersion, AMServiceEnabled, AntivirusEnabled
5. Confirm that AMServiceEnabled and AntivirusEnabled are both True.
6. Perform a quick scan using: Start-MpScan -ScanType QuickScan
7. Verify the scan completes without error 0x80501107.

## Rollback
1. If the remediation involved any configuration changes, revert them using Group Policy or PowerShell:
   - For example, if registry keys were modified, restore the original values from backup.
2. Restart the Microsoft Defender Antivirus service:
   - Open Services.msc, locate 'Microsoft Defender Antivirus Service', right-click and select Restart.
3. If the issue persists, run the Microsoft Support and Recovery Assistant (SaRA) for Defender.
4. As a last resort, reset Microsoft Defender Antivirus to default settings using:
   Set-MpPreference -Force
5. Reboot the device and re-verify the error is no longer present.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
