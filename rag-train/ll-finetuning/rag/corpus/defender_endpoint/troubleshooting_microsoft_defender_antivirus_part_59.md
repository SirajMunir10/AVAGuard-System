# Troubleshooting: Microsoft Defender Antivirus (5013)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 5013 indicating Tamper protection blocked a change to Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Tamper protection enabled

## Symptoms
- Event ID 5013 is generated
- Tamper protection blocked a change to Microsoft Defender Antivirus

## Error Codes
- `5013`

## Root Causes
1. Tamper protection is enabled and an attempt to change any of Defender's settings is blocked

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. 2. Verify that no new Event ID 5013 entries appear after the remediation. 3. Confirm that Tamper protection is still enabled by running Get-MpComputerStatus | Select-Object -Property IsTamperProtected from an elevated PowerShell prompt. 4. Attempt a benign change to Defender settings (e.g., Set-MpPreference -DisableRealtimeMonitoring $false) and confirm it is blocked with a new Event ID 5013.

## Rollback
1. If the remediation fails or causes issues, re-enable Tamper protection by running Set-MpPreference -DisableTamperProtection $false from an elevated PowerShell prompt. 2. Restart the Microsoft Defender Antivirus service with Restart-Service -Name WinDefend. 3. Verify Tamper protection is active by running Get-MpComputerStatus | Select-Object -Property IsTamperProtected. 4. Confirm Event ID 5013 is generated again when a change is attempted.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
