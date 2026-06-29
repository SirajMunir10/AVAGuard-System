# Implementation: Controlled Folder Access

**Domain:** Defender for Endpoint
**Subdomain:** Controlled Folder Access
**Incident Type:** Implementation

## Scenario / Query
How to enable controlled folder access using Microsoft Intune admin center, MDM, Configuration Manager, Group Policy, or PowerShell?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** Windows 10 or later, Windows Server 2019 or later, Windows Server 2016 and Windows Server 2012 R2 with modern unified solution

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable controlled folder access in the Microsoft Intune admin center
2. Enable controlled folder access using Mobile Device Management (MDM)
3. Enable controlled folder access using Microsoft Configuration Manager
4. Enable controlled folder access using Group Policy
5. Enable controlled folder access using PowerShell

## Validation
1. On a Windows 10/11 or Windows Server 2019+ device, open Windows Security > Virus & threat protection > Ransomware protection and verify 'Controlled folder access' is 'On'. 2. Run PowerShell as admin: Get-MpPreference | Select-Object EnableControlledFolderAccess. Confirm output is '1' (enabled). 3. In Microsoft Intune admin center, navigate to Endpoint security > Attack surface reduction > (policy name) and verify 'Enable controlled folder access' is set to 'Enable'. 4. For MDM, check OMA-URI ./Vendor/MSFT/Policy/Config/Defender/EnableControlledFolderAccess value is 1. 5. For Configuration Manager, verify the client policy shows 'Controlled folder access: Enabled'. 6. For Group Policy, run gpresult /h gp.html and confirm 'Configure controlled folder access' is set to 'Enabled' with mode 'Block' or 'Audit' as intended.

## Rollback
1. In Intune admin center, edit the policy and set 'Enable controlled folder access' to 'Not configured' or 'Disabled', then sync devices. 2. For MDM, set OMA-URI value to 0 or delete the policy. 3. In Configuration Manager, disable the setting in the client policy and redeploy. 4. For Group Policy, set 'Configure controlled folder access' to 'Not configured' and run gpupdate /force. 5. PowerShell: Set-MpPreference -EnableControlledFolderAccess Disabled. 6. Verify rollback: repeat validation steps and confirm 'Controlled folder access' is 'Off' or '0'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
