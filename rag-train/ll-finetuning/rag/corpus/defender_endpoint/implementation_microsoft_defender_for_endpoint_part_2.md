# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to deploy Microsoft Defender for Endpoint onboarding package using Group Policy?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Group Policy deployment method

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open the GP configuration package file (WindowsDefenderATPOnboardingPackage.zip) that you downloaded from the service onboarding wizard.
2. You can also get the package from the Microsoft Defender portal: In the navigation pane, select System > Settings > Endpoints > Device management > Onboarding.
3. Select the operating system.
4. In the Deployment method field, select Group policy.
5. Select Download package and save the .zip file.
6. Extract the contents of the .zip file to a shared, read-only location that can be accessed by the device.
7. You should have a folder called OptionalParamsPolicy and the file WindowsDefenderATPOnboardingScript.cmd.

## Validation
1. On a target device, run 'gpresult /H gpresult.html' and open the HTML file to confirm the 'WindowsDefenderATPOnboardingScript.cmd' policy is applied. 2. Verify the service status by running 'sc query WinDefend' and confirm the state is 'RUNNING'. 3. Check the onboarding status by running 'Get-MpComputerStatus | Select-Object -Property AMProductVersion,AMServiceEnabled,AntispywareEnabled,AntivirusEnabled' in PowerShell and ensure all properties show 'True' and a valid product version.

## Rollback
1. Remove the Group Policy Object (GPO) that deployed the onboarding script. 2. On affected devices, run 'gpupdate /force' to refresh policy and remove the script. 3. Run the uninstall script 'WindowsDefenderATPUninstallScript.cmd' from the extracted package to offboard the device. 4. Verify offboarding by running 'Get-MpComputerStatus | Select-Object -Property AMServiceEnabled' and confirm it returns 'False'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
