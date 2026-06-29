# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
What are the operating system requirements for endpoint devices to use DLP conditions like 'Document could not be scanned' or 'Document name contains words or phrases'?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview DLP
- **Configuration:** Endpoint DLP policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure endpoint devices run one of the following operating systems: Windows 11 23H2 with KB5032288 (OS Builds 22621.2792 and 22631.2792) Preview, Windows 11 22H2 with KB5032288 (OS Builds 22621.2792 and 22631.2792) Preview, Windows 11 21H2 with KB5033369 (OS Build 22000.2652), Windows 10 22H2 with KB5032278 (OS Build 19045.3758) Preview, Windows 10 21H2 with KB5032278 (OS Build 19045.3758) Preview, Windows Server 2022/2019 with KB5032198 (OS Build 20348.2113) or later, Windows 11 with KB5034848 (OS Builds 22621.3235 and 22631.3235) Preview or later, Windows 10 with KB5034843 (OS Build 19045.4123) Preview or later.
2. For PDF files, ensure Adobe requirements are met as per Microsoft Purview Information Protection Support in Acrobat.

## Validation
1. On each endpoint device, run 'winver' to confirm the OS build matches one of the required versions (e.g., Windows 11 23H2 with OS Build 22621.2792 or 22631.2792). 2. Verify that the required KB update is installed by running 'wmic qfe list brief /format:texttable' and checking for the KB number (e.g., KB5032288). 3. For PDF scenarios, confirm Adobe Acrobat or Reader is installed and that the Microsoft Purview Information Protection add-in is enabled (check under Help > About Plug-ins). 4. Test a DLP policy condition such as 'Document name contains words or phrases' by creating a file with a matching name and verifying that the policy triggers an audit event in the Microsoft 365 Purview compliance portal.

## Rollback
1. If an OS update causes issues, uninstall the KB via 'wusa /uninstall /kb:5032288 /quiet /norestart' (replace KB number as needed) and reboot. 2. If the device was upgraded to a newer OS build, revert to the previous build using Windows Recovery Environment or a system restore point. 3. For Adobe issues, disable or remove the Purview add-in from Acrobat (Help > About Plug-ins > select add-in > Disable) or reinstall Adobe Acrobat without the add-in. 4. If DLP policies are not working as expected, temporarily disable the endpoint DLP policy in the Purview compliance portal (Data Loss Prevention > Policies > select policy > turn off).

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
