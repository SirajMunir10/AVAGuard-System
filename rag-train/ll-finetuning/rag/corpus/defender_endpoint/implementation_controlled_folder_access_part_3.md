# Implementation: Controlled Folder Access

**Domain:** Defender for Endpoint
**Subdomain:** Controlled Folder Access
**Incident Type:** Implementation

## Scenario / Query
How to enable Controlled Folder Access using PowerShell?

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
2. Run the following command: Set-MpPreference -EnableControlledFolderAccess Enabled

## Validation
Run the following PowerShell command as administrator to verify that Controlled Folder Access is enabled: Get-MpPreference | Select-Object -Property EnableControlledFolderAccess. Confirm the output shows 'True'.

## Rollback
Run the following PowerShell command as administrator to disable Controlled Folder Access: Set-MpPreference -EnableControlledFolderAccess Disabled. Then verify the change by running: Get-MpPreference | Select-Object -Property EnableControlledFolderAccess, ensuring the output shows 'False'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
