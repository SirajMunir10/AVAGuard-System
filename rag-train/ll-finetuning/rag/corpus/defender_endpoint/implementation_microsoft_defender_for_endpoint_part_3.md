# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites for deploying Microsoft Defender for Endpoint using Group Policy?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Group Policy deployment prerequisites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. To use Group Policy (GP) updates to deploy the package, you must be on Windows Server 2008 R2 or later.
2. For Windows Server 2019 and newer, you may need to replace NT AUTHORITY\Well-Known-System-Account with NT AUTHORITY\SYSTEM of the XML file that the Group Policy preference creates.
3. If you're using the new, unified Microsoft Defender for Endpoint solution for Windows Server 2012 R2 and Windows Server 2016, make sure to use the latest ADMX files in your central store to get access to the correct Microsoft Defender for Endpoint policy options.
4. See How to create and manage the Central Store for Group Policy Administrative Templates in Windows and download the latest files for use with Windows 10.

## Validation
1. Verify that the Group Policy Management Console (GPMC) is installed on a supported OS (Windows Server 2008 R2 or later).
2. Confirm that the Group Policy Object (GPO) containing the Defender for Endpoint deployment package is linked to the target organizational unit (OU).
3. On a target Windows Server 2019 or newer machine, run 'gpresult /h gp_report.html' and inspect the report to ensure the policy is applied.
4. Check the XML file created by the Group Policy preference for the deployment package; verify that the account name is 'NT AUTHORITY\SYSTEM' (not 'NT AUTHORITY\Well-Known-System-Account') if the target is Windows Server 2019 or newer.
5. For Windows Server 2012 R2 or 2016 using the unified solution, confirm that the latest ADMX files are present in the Central Store (e.g., %SystemRoot%\sysvol\domain\Policies\PolicyDefinitions) and that the relevant Defender for Endpoint policy settings appear in the GPO editor.

## Rollback
1. Remove the GPO link from the target OU using Group Policy Management Console.
2. Delete the GPO that was created for the deployment, or disable the policy settings within it.
3. If the XML file was modified to replace the account name, revert the change back to 'NT AUTHORITY\Well-Known-System-Account' in the Group Policy preference.
4. If ADMX files were added to the Central Store, remove the Defender for Endpoint related ADMX and ADML files from the Central Store folder.
5. On affected machines, run 'gpupdate /force' to refresh policy and remove any applied settings.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
