# Implementation: Endpoint Protection

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Protection
**Incident Type:** Implementation

## Scenario / Query
How to configure Microsoft Defender for Endpoint using Configuration Manager (SCCM) with the required prerequisites?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Configuration Manager with Endpoint Protection point site system role

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the Endpoint Protection point site system role is installed and configured in Configuration Manager.
2. Verify that antivirus and attack surface reduction policies are properly deployed to the targeted endpoints.

## Validation
1. In the Configuration Manager console, navigate to Administration > Site Configuration > Servers and Site System Roles. Confirm that the 'Endpoint Protection point' role is listed and shows a status of 'Installed'.
2. In the Configuration Manager console, go to Assets and Compliance > Endpoint Protection > Antivirus Policies. Verify that at least one antivirus policy is deployed to a collection containing the targeted endpoints.
3. In the Configuration Manager console, go to Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard > Attack Surface Reduction Policies. Confirm that at least one attack surface reduction policy is deployed to a collection containing the targeted endpoints.
4. On a targeted endpoint, open the Windows Security app and verify that 'Virus & threat protection' shows 'Microsoft Defender Antivirus' as the active antivirus provider and that the policy settings (e.g., real-time protection) are applied as configured.
5. On a targeted endpoint, run the PowerShell command: Get-MpComputerStatus | Select-Object AMProductVersion, AMServiceEnabled, AntivirusEnabled. Confirm that AMServiceEnabled and AntivirusEnabled are both True.

## Rollback
1. In the Configuration Manager console, navigate to Assets and Compliance > Endpoint Protection > Antivirus Policies. Right-click the deployed antivirus policy and select 'Delete' to remove the policy deployment, or modify the deployment to a different collection to stop applying it to the affected endpoints.
2. In the Configuration Manager console, go to Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard > Attack Surface Reduction Policies. Right-click the deployed attack surface reduction policy and select 'Delete' to remove the policy deployment, or modify the deployment to a different collection.
3. If the Endpoint Protection point role was recently added, in the Configuration Manager console, navigate to Administration > Site Configuration > Servers and Site System Roles. Select the site system server, right-click the 'Endpoint Protection point' role, and choose 'Remove Role'. Confirm the removal.
4. On affected endpoints, run the PowerShell command: Set-MpPreference -DisableRealtimeMonitoring $true to temporarily disable real-time protection if needed, or use Group Policy to revert to a previous antivirus configuration.
5. Monitor the endpoints for any residual issues and reapply previous antivirus or attack surface reduction policies as necessary.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
