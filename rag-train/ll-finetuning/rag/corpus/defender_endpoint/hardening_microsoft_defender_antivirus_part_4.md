# Hardening: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Hardening

## Scenario / Query
How to configure cloud deliver timeout and protection level for Microsoft Defender Antivirus using Group Policy?

## Environment Context
- **Tenant Type:** On-premises Active Directory with Group Policy management
- **Configuration:** Windows Components > Microsoft Defender Antivirus > MpEngine

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Browse to Computer Configuration > Policies > Administrative Templates > Windows Components > Microsoft Defender Antivirus > MpEngine.
2. Configure cloud protection level policy to Default Microsoft Defender Antivirus blocking policy.
3. This will disable the policy.
4. This is what is required to set the protection level to the windows default.

## Validation
Run the following command on a test machine to confirm the cloud protection level is set to default: Get-MpPreference | Select-Object -Property CloudBlockLevel. Verify the output shows '0' (default). Also check the registry key: HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\MpEngine\MpCloudBlockLevel. Ensure the value is 0 or the key does not exist. Confirm that the Group Policy object is applied by running gpresult /h gpresult.html and reviewing the 'Microsoft Defender Antivirus' settings.

## Rollback
If the remediation fails or causes issues, revert the Group Policy setting: In the Group Policy Management Console, navigate to Computer Configuration > Policies > Administrative Templates > Windows Components > Microsoft Defender Antivirus > MpEngine. Set the 'Configure cloud protection level' policy to 'Not Configured' or 'Enabled' with a different level as needed. Then run gpupdate /force on affected machines. Alternatively, delete the registry key HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\MpEngine\MpCloudBlockLevel if it exists.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
