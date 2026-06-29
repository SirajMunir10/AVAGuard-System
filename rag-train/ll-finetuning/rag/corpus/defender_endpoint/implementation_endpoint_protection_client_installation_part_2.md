# Implementation: Endpoint Protection Client Installation

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Protection Client Installation
**Incident Type:** Implementation

## Scenario / Query
How to install the Endpoint Protection client with an antimalware policy using Command Prompt?

## Environment Context
- **Tenant Type:** On-premises with Configuration Manager
- **Configuration:** Endpoint Protection client installation with antimalware policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Copy scepinstall.exe from the Client folder of the Configuration Manager installation folder to the computer on which you want to install the Endpoint Protection client software.
2. Open Command Prompt as an administrator.
3. Change directory to the folder with the installer.
4. Run the following command: scepinstall.exe /policy <full path>\<policy file>
5. Follow the on-screen instructions to complete the client installation.
6. If you downloaded the latest update definition package, copy the package to the client computer, and then double-click the definition package to install it.

## Validation
1. Open Command Prompt as administrator and run: 'wmic /namespace:\\root\Microsoft\SecurityClient path MsMpAcquisitionStatus get *' to verify the client is installed and the antimalware policy is applied. 2. Check the client UI by navigating to Start > System Center Endpoint Protection and confirm the policy name matches the deployed policy. 3. Review the %ProgramFiles%\Microsoft Security Client\MpCmdRun.exe -ValidateMapsConnection command to ensure the client can communicate with the management point.

## Rollback
1. Uninstall the Endpoint Protection client via Control Panel > Programs and Features > Microsoft System Center Endpoint Protection > Uninstall. 2. If the client was installed with a policy that caused issues, reinstall using the command: 'scepinstall.exe /policy <path_to_backup_policy>' with a known-good policy file. 3. If the update definition package caused problems, remove it by deleting the package file and running 'MpCmdRun.exe -RemoveDefinitions -All' from an elevated command prompt.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
