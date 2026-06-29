# Implementation: Controlled Folder Access

**Domain:** Defender for Endpoint
**Subdomain:** Controlled Folder Access
**Incident Type:** Implementation

## Scenario / Query
How to enable Controlled Folder Access using Microsoft Configuration Manager?

## Environment Context
- **Tenant Type:** On-premises with Configuration Manager
- **Configuration:** Microsoft Configuration Manager, Windows Defender Exploit Guard

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In Microsoft Configuration Manager, go to Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard.
2. Select Home > Create Exploit Guard Policy.
3. Enter a name and a description, select Controlled folder access, and select Next.
4. Choose whether block or audit changes, allow other apps, or add other folders, and select Next.
5. Review the settings and select Next to create the policy.
6. After the policy is created, Close.

## Validation
1. In Configuration Manager console, navigate to Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard. 2. Locate the created Exploit Guard policy and verify its settings include Controlled folder access enabled with the chosen mode (Block or Audit). 3. Deploy the policy to a test collection and confirm the client receives it by checking the client's PolicyAgent.log or using the Configuration Manager client action 'Machine Policy Retrieval & Evaluation Cycle'. 4. On a managed Windows 10/11 device, open Windows Security > Virus & threat protection > Ransomware protection and verify Controlled folder access shows 'On' (Block mode) or 'Audit mode' as configured. 5. Run the PowerShell command 'Get-MpPreference | Select-Object EnableControlledFolderAccess' and confirm the value is 1 (Block) or 2 (Audit).

## Rollback
1. In Configuration Manager console, navigate to Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard. 2. Select the deployed Exploit Guard policy and choose 'Delete' from the ribbon or right-click menu to remove the policy. 3. Alternatively, edit the policy to set Controlled folder access to 'Not configured' and redeploy. 4. On affected clients, run the PowerShell command 'Set-MpPreference -EnableControlledFolderAccess Disabled' to immediately disable the feature. 5. Monitor client devices to confirm Controlled folder access is no longer enforced by checking Windows Security or running 'Get-MpPreference | Select-Object EnableControlledFolderAccess' (should return 0).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
