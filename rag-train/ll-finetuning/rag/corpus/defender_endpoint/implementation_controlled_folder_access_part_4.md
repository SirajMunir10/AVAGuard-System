# Implementation: Controlled Folder Access

**Domain:** Defender for Endpoint
**Subdomain:** Controlled Folder Access
**Incident Type:** Implementation

## Scenario / Query
How to enable Controlled Folder Access in audit mode using PowerShell?

## Environment Context
- **Tenant Type:** Windows
- **Configuration:** Microsoft Defender Antivirus

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Type powershell in the Start menu, right-click Windows PowerShell and select Run as administrator.
2. Run the following command: Set-MpPreference -EnableControlledFolderAccess AuditMode

## Validation
Run the following PowerShell command as administrator: Get-MpPreference | Select-Object -Property EnableControlledFolderAccess. Verify that the output shows 'AuditMode'.

## Rollback
Run the following PowerShell command as administrator: Set-MpPreference -EnableControlledFolderAccess Disabled. Then confirm by running: Get-MpPreference | Select-Object -Property EnableControlledFolderAccess. The output should show 'Disabled'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
