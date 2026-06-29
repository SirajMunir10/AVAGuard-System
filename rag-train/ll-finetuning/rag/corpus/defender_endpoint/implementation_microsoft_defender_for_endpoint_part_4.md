# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to configure endpoint protection settings via Group Policy for Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Windows 10, Windows 11, or Windows Server 2019 and later

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Perform group policy edits from a system running Windows 10, Windows 11, or Windows Server 2019 and later to ensure you have all of the required Microsoft Defender Antivirus capabilities.
2. You may need to close and reopen the group policy object to register the Defender ATP configuration settings.
3. All policies are located under Computer Configuration\Policies\Administrative Templates.
4. Policy location: \Windows Components\Windows Defender ATP - Enable/Disable Sample collection: Enabled - 'Enable sample collection on machines' checked.
5. Policy location: \Windows Components\Microsoft Defender Antivirus - Configure detection for potentially unwanted applications: Enabled, Block.
6. Policy location: \Windows Components\Microsoft Defender Antivirus\MAPS - Join Microsoft MAPS: Enabled, Advanced MAPS.
7. Policy location: \Windows Components\Microsoft Defender Antivirus\MAPS - Send file samples when further analysis is required: Enabled, Send safe samples.
8. Policy location: \Windows Components\Microsoft Defender Antivirus\Real-time Protection - Turn off real-time protection: Not configured (implied by omission), Turn on behavior monitoring: Enabled, Scan all downloaded files and attachments: Enabled, Monitor file and program activity on your computer: Enabled.
9. Policy location: \Windows Components\Microsoft Defender Antivirus\Scan - Check for the latest virus and spyware security intelligence before running a scheduled scan: Enabled. Recommend performing a weekly quick scan, performance permitting.
10. Policy location: \Windows Components\Microsoft Defender Antivirus\Microsoft Defender Exploit Guard\Attack Surface Reduction - Open the Configure Attack Surface Reduction policy. Select Enabled. Select the Show button. Add each GUID in the Value Name field with a value of 2. This sets each up for audit only.
11. Policy location: \Windows Components\Microsoft Defender Antivirus\Microsoft Defender Exploit Guard\Controlled Folder Access - Enabled, Audit Mode.

## Validation
1. On a domain-joined Windows 10/11 or Windows Server 2019+ client, run 'gpresult /h gp_report.html' and open the report. Verify under 'Computer Configuration\Administrative Templates\Windows Components\Windows Defender ATP' that 'Enable/Disable Sample collection' is set to 'Enabled' with 'Enable sample collection on machines' checked.
2. In the same report, navigate to 'Windows Components\Microsoft Defender Antivirus' and confirm 'Configure detection for potentially unwanted applications' is 'Enabled' and set to 'Block'.
3. Under 'Windows Components\Microsoft Defender Antivirus\MAPS', verify 'Join Microsoft MAPS' is 'Enabled' with 'Advanced MAPS' selected, and 'Send file samples when further analysis is required' is 'Enabled' with 'Send safe samples'.
4. Under 'Real-time Protection', confirm 'Turn off real-time protection' is 'Not configured', 'Turn on behavior monitoring' is 'Enabled', 'Scan all downloaded files and attachments' is 'Enabled', and 'Monitor file and program activity on your computer' is 'Enabled'.
5. Under 'Scan', verify 'Check for the latest virus and spyware security intelligence before running a scheduled scan' is 'Enabled'.
6. Under 'Microsoft Defender Exploit Guard\Attack Surface Reduction', confirm 'Configure Attack Surface Reduction' is 'Enabled' and each listed GUID has a value of 2.
7. Under 'Controlled Folder Access', verify it is 'Enabled' and set to 'Audit Mode'.
8. Run 'Get-MpComputerStatus' in PowerShell and confirm 'AMRunningMode' is 'Normal' and 'RealTimeProtectionEnabled' is 'True'.

## Rollback
1. On a domain controller or management workstation with Group Policy Management Console, edit the same GPO. For each policy set above, change the setting to 'Not configured' or revert to the original value.
2. Specifically: Under 'Windows Components\Windows Defender ATP', set 'Enable/Disable Sample collection' to 'Not configured'.
3. Under 'Windows Components\Microsoft Defender Antivirus', set 'Configure detection for potentially unwanted applications' to 'Not configured'.
4. Under 'MAPS', set both 'Join Microsoft MAPS' and 'Send file samples when further analysis is required' to 'Not configured'.
5. Under 'Real-time Protection', set 'Turn off real-time protection' to 'Enabled' (if it was previously enabled) or 'Not configured', and revert 'Turn on behavior monitoring', 'Scan all downloaded files and attachments', and 'Monitor file and program activity on your computer' to 'Not configured'.
6. Under 'Scan', set 'Check for the latest virus and spyware security intelligence before running a scheduled scan' to 'Not configured'.
7. Under 'Attack Surface Reduction', set 'Configure Attack Surface Reduction' to 'Not configured'.
8. Under 'Controlled Folder Access', set it to 'Not configured'.
9. Close the GPO editor and force a Group Policy update on affected clients with 'gpupdate /force'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
