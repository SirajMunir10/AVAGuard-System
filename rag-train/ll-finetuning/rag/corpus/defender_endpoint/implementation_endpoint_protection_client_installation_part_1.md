# Implementation: Endpoint Protection Client Installation

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Protection Client Installation
**Incident Type:** Implementation

## Scenario / Query
How to install the Endpoint Protection client using Command Prompt from the Configuration Manager installation folder?

## Environment Context
- **Tenant Type:** On-premises with Configuration Manager
- **Configuration:** Endpoint Protection client installation via scepinstall.exe

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
4. Run scepinstall.exe, adding any extra command-line properties that you require. Properties include: /s (Run the installer silently), /q (Extract the setup files silently), /i (Run the installer normally), /policy (Specify an antimalware policy file to configure the client during installation), /sqmoptin (Opt-in to the Microsoft Customer Experience Improvement Program (CEIP)).
5. Follow the on-screen instructions to complete the client installation.
6. If you downloaded the latest update definition package, copy the package to the client computer, and then double-click the definition package to install it.

## Validation
1. Open Command Prompt as administrator and run: 'wmic /namespace:\\root\securitycenter2 path antivirusproduct get displayname, productstate' to verify that Microsoft Defender for Endpoint (or System Center Endpoint Protection) appears with a productstate value indicating it is enabled and up to date (e.g., 397568).
2. Run 'sc query Windefend' to confirm the Microsoft Defender Antivirus service is running.
3. Check the client version by running: 'wmic /namespace:\\root\microsoft\securityclient path MSFT_MpComputerStatus get AntivirusSignatureLastUpdated, AntivirusSignatureVersion' to ensure definitions are current.
4. If a policy file was specified during installation, verify the policy is applied by running: 'Get-MpPreference' in PowerShell and checking that settings match the deployed policy.

## Rollback
1. Uninstall the Endpoint Protection client by running: 'msiexec /x {GUID} /quiet' where {GUID} is the product code for System Center Endpoint Protection (typically found via 'wmic product where "name like '%Endpoint Protection%'" get IdentifyingNumber').
2. Alternatively, use the original scepinstall.exe with the /u switch: 'scepinstall.exe /u /s' to silently uninstall.
3. After uninstallation, restart the computer to complete removal.
4. If the client was installed via Configuration Manager, use the Configuration Manager console to remove the deployment from the affected device collection and re-evaluate the deployment status.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
