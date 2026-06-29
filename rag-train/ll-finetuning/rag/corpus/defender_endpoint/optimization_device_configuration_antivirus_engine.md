# Optimization: Device Configuration â€“ Antivirus Engine

**Domain:** Defender for Endpoint
**Subdomain:** Device Configuration â€“ Antivirus Engine
**Incident Type:** Optimization

## Scenario / Query
How do I optimize Microsoft Defender Antivirus performance by excluding specific file paths and processes from real-time scanning without reducing security coverage?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5 / Defender for Endpoint Plan 2)
- **Configuration:** Microsoft Defender Antivirus managed via Intune or Group Policy; real-time protection enabled

## Symptoms
- High CPU usage by MsMpEng.exe during normal business operations
- End-user complaints about system slowness when opening trusted line-of-business applications
- Antivirus engine repeatedly scanning large database or log files that are known to be safe

## Error Codes
N/A

## Root Causes
1. No exclusions configured for trusted, frequently accessed file types or locations
2. Default real-time scanning behavior includes high-volume, low-risk paths such as SQL database folders or build output directories

## Remediation Steps
1. Identify the specific file extensions, folder paths, or processes that are causing performance issues using the Microsoft Defender Antivirus performance analyzer (Get-MpPerformanceReport).
2. Add exclusions via Group Policy (Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Exclusions) or via Intune (Devices > Configuration profiles > Endpoint protection > Microsoft Defender Antivirus > Exclusions).
3. Use the Add-MpPreference -ExclusionPath, -ExclusionExtension, or -ExclusionProcess PowerShell cmdlets to set exclusions on individual devices for testing.
4. Ensure exclusions are as narrow as possible (e.g., specific file paths rather than entire drives) and review the Microsoft recommended exclusion list for Windows Server roles to avoid over-excluding.
5. Monitor performance after applying exclusions using the same performance analyzer to confirm improvement without triggering alerts.

## Validation
Run Get-MpPreference to verify that the exclusions are applied. Use the Microsoft Defender Antivirus performance analyzer (Get-MpPerformanceReport) to confirm that the previously high CPU usage has dropped below acceptable thresholds.

## Rollback
Remove the added exclusions using Remove-MpPreference -ExclusionPath, -ExclusionExtension, or -ExclusionProcess, or revert the Group Policy/Intune configuration change.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-exclusions-microsoft-defender-antivirus>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-performance-issues>
