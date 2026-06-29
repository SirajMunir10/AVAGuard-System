# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to deploy Microsoft Defender Antivirus and attack surface reduction policies through Microsoft Configuration Manager (SCCM)?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Configuration Manager (SCCM)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Endpoint Protection and configure custom client settings.
2. Install the Endpoint Protection client from a command prompt.
3. Verify the Endpoint Protection client installation.

## Validation
1. In the Configuration Manager console, go to 'Assets and Compliance' > 'Endpoint Protection' > 'Antimalware Policies' and confirm the policy is deployed to the target collection. 2. On a managed client, open the Endpoint Protection client UI and verify the policy name and settings are applied. 3. Run 'Get-MpComputerStatus' in PowerShell on a client to confirm AMProductVersion and AMServiceEnabled are correct. 4. Check the client's %ProgramFiles%\Microsoft Security Client\MpCmdRun.exe exists and run 'MpCmdRun -GetDeviceContext' to verify enrollment.

## Rollback
1. In the Configuration Manager console, under 'Administration' > 'Client Settings', locate the custom client settings that enabled Endpoint Protection and either disable the 'Manage Endpoint Protection client on client computers' setting or remove the deployment to the affected collection. 2. On each client, run 'MpCmdRun -RemoveDefinitions -All' to clear policies, then uninstall the Endpoint Protection client via 'Programs and Features' or by running 'Msiexec /x {GUID}' where GUID is from the client installation. 3. Redeploy the previous antimalware policy or reinstall the client if needed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
