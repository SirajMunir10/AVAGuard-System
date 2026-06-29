# Implementation: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Implementation

## Scenario / Query
How to enable Controlled folder access using Group Policy?

## Environment Context
- **Tenant Type:** on-premises
- **Configuration:** Group Policy management device with GPMC

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open the Group Policy Management Console (GPMC) on your Group Policy management device.
2. Right-click the Group Policy Object you want to configure and select Edit.
3. In the Group Policy Management Editor, go to Computer configuration and select Administrative templates.
4. Expand the tree to Windows components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Controlled folder access.
5. Double-click the Configure Controlled folder access setting and set the option to Enabled.
6. In the options section, specify one of the following options: Enable, Disable (Default), Audit Mode, Block disk modification only, or Audit disk modification only.

## Validation
1. On a target machine in the scope of the GPO, run 'gpupdate /force' from an elevated command prompt. 2. Open an elevated PowerShell and run 'Get-MpPreference | Select-Object -Property EnableControlledFolderAccess, ControlledFolderAccessProtectedFolders, ControlledFolderAccessAllowedApplications'. 3. Confirm that EnableControlledFolderAccess is set to the expected value (e.g., 1 for Enable, 2 for Audit Mode). 4. Verify that the policy is applied by running 'gpresult /h gpresult.html' and checking the 'Microsoft Defender Antivirus - Controlled Folder Access' section for the configured setting.

## Rollback
1. Open the Group Policy Management Console (GPMC) on the management device. 2. Right-click the same Group Policy Object and select Edit. 3. Navigate to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Controlled folder access. 4. Double-click 'Configure Controlled folder access' and set it to 'Not Configured' or 'Disabled'. 5. Click OK and close the Group Policy Management Editor. 6. On affected machines, run 'gpupdate /force' from an elevated command prompt to revert the policy.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
