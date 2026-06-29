# Hardening: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Hardening

## Scenario / Query
How to configure Cloud Deliver Protection and automatic sample submission via Group Policy to maximize security posture?

## Environment Context
- **Tenant Type:** On-premises Active Directory with Group Policy management
- **Configuration:** Windows Components > Microsoft Defender Antivirus > MAPS

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Browse to Computer Configuration > Policies > Administrative Templates > Windows Components > Microsoft Defender Antivirus > MAPS.
2. Select the 'Send all samples' option to provide the most analysis of binaries/scripts/docs which increases security posture.

## Validation
1. Confirm the Group Policy Object (GPO) is linked to the target organizational unit (OU).
2. On a test machine in the OU, run 'gpupdate /force' from an elevated command prompt.
3. Verify the registry key: HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet\SubmitSamplesConsent exists and its value is 3 (Send all samples).
4. Verify the registry key: HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet\SpyNetReporting exists and its value is 2 (Advanced MAPS membership).
5. Open Windows Security > Virus & threat protection > Manage settings and confirm 'Cloud-delivered protection' and 'Automatic sample submission' are both turned on.

## Rollback
1. Open the Group Policy Management Console (GPMC).
2. Edit the GPO that was modified.
3. Navigate to Computer Configuration > Policies > Administrative Templates > Windows Components > Microsoft Defender Antivirus > MAPS.
4. Set 'Send all samples' to 'Not Configured' or 'Disabled'.
5. Run 'gpupdate /force' on affected machines.
6. Verify the registry keys HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet\SubmitSamplesConsent and SpyNetReporting are deleted or set to default values (0 or absent).
7. Confirm in Windows Security that 'Cloud-delivered protection' and 'Automatic sample submission' are turned off or set to default.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
