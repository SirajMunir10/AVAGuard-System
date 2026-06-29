# Troubleshooting: Microsoft Defender Antivirus (0x80508027)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x80508027 indicating removal of low and medium threats is disabled in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508027
- Message: ERR_MP_REMOVE_LOW_MEDIUM_DISABLED ERR_MP_REMOVE_LOW_MEDIUM_DISABLED

## Error Codes
- `0x80508027`

## Root Causes
1. Removal of low and medium threats might be disabled

## Remediation Steps
1. Check the detected threats and resolve them as required

## Validation
1. Open Windows Security app and navigate to Virus & threat protection > Protection history. Verify that low and medium threats are now listed and can be acted upon. 2. Run the PowerShell command: Get-MpThreat | Where-Object {$_.Resources -ne $null} | Format-Table -AutoSize. Confirm that threats with severity 'Low' or 'Medium' are present and their 'RemediationStatus' is not 'Disabled'. 3. Attempt to manually remove a low or medium threat using: Remove-MpThreat -ThreatID <ThreatID>. Verify no error 0x80508027 is returned.

## Rollback
1. If the remediation fails or causes issues, re-enable the removal of low and medium threats by setting the following registry key: Set-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender' -Name 'DisableRemovalOfLowMediumThreats' -Value 1 -Type DWord. 2. Restart the Microsoft Defender Antivirus service: Restart-Service -Name WinDefend. 3. Confirm the error 0x80508027 reappears by attempting to remove a low or medium threat via PowerShell: Remove-MpThreat -ThreatID <ThreatID>.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
