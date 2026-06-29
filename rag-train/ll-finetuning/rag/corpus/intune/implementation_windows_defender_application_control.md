# Implementation: Windows Defender Application Control

**Domain:** Intune
**Subdomain:** Windows Defender Application Control
**Incident Type:** Implementation

## Scenario / Query
How to deploy App Control policies via Intune, Configuration Manager, or PowerShell?

## Environment Context
- **Tenant Type:** Windows 10/11 or Windows Server 2016+
- **Configuration:** App Control policies can be deployed via MDM (e.g., Intune), Configuration Manager, or PowerShell

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create App Control policies on any client edition of Windows 10 or Windows 11, or on Windows Server 2016 and higher.
2. Deploy App Control policies via a Mobile Device Management (MDM) solution, for example, Intune.
3. Alternatively, deploy via a management interface such as Configuration Manager.
4. Alternatively, deploy via a script host such as PowerShell.
5. Group Policy can also be used to deploy App Control policies, but is limited to single-policy format policies that work on Windows Server 2016 and 2019.

## Validation
1. On a Windows 10/11 or Windows Server 2016+ client, run in PowerShell as Administrator: Get-CIPolicy -FilePath C:\temp\current.xml. Verify the policy contains the expected rules. 2. Check the event log: Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-CodeIntegrity/Operational'; ID=3076} | Select-Object -First 5. Confirm events show the policy is active. 3. For Intune: In the Microsoft Intune admin center, go to Endpoint Security > Attack surface reduction > App Control for Business. Verify the policy is listed with a status of 'Succeeded' for targeted devices. 4. For Configuration Manager: In the Configuration Manager console, go to Assets and Compliance > Endpoint Protection > Windows Defender Application Control. Confirm the policy is deployed and compliance is reported. 5. For PowerShell: Run Get-AppLockerPolicy -Local | Test-AppLockerPolicy -Path C:\Windows\System32\notepad.exe -User Everyone. Verify the output indicates the file is allowed or denied as expected.

## Rollback
1. Remove the App Control policy via Intune: In the Intune admin center, go to Endpoint Security > Attack surface reduction > App Control for Business, select the policy, and click Delete. 2. Remove via Configuration Manager: In the Configuration Manager console, go to Assets and Compliance > Endpoint Protection > Windows Defender Application Control, right-click the policy, and select Delete. 3. Remove via PowerShell: Run Remove-AppLockerPolicy -Local -PolicyType Exe -ErrorAction SilentlyContinue; Remove-AppLockerPolicy -Local -PolicyType Script -ErrorAction SilentlyContinue; Remove-AppLockerPolicy -Local -PolicyType Msi -ErrorAction SilentlyContinue. 4. Reboot the device to ensure the policy is no longer enforced. 5. Verify removal: Run Get-AppLockerPolicy -Local | Select-Object -ExpandProperty RuleCollections. Confirm no rules are present.

## References
- <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview>
