# Implementation: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Implementation

## Scenario / Query
What is the recommended order for piloting and deploying Microsoft Defender XDR components?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Defender XDR

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Start the pilot
2. Pilot and deploy Defender for Identity
3. Pilot and deploy Defender for Office 365
4. Pilot and deploy Defender for Endpoint
5. Pilot and deploy Microsoft Defender for Cloud Apps
6. Practice incident investigation and response

## Validation
1. Confirm that the pilot tenant has Microsoft Defender XDR enabled by navigating to https://security.microsoft.com and verifying the presence of the Microsoft Defender XDR dashboard.
2. Run the following PowerShell command to check the deployment status of Defender for Identity: Get-MsolUser -All | Select-Object UserPrincipalName, IsLicensed. Ensure that at least one user has a valid license for Microsoft Defender for Identity.
3. For Defender for Office 365, run: Get-OrganizationConfig | Format-List Name, IsDehydrated. Verify that the organization is not dehydrated and that the EOP/ATP policies are configured.
4. For Defender for Endpoint, run: Get-MpComputerStatus | Select-Object AMProductVersion, AMRunningMode. Confirm that the endpoint is onboarded and running in active mode.
5. For Microsoft Defender for Cloud Apps, run: Get-MsolAccountSku | Where-Object {$_.AccountSkuId -like '*CLOUDAPPS*'}. Verify that the appropriate licenses are assigned.
6. Simulate an incident by executing a test attack (e.g., using the Microsoft 365 Defender evaluation tools) and confirm that the incident appears in the Microsoft 365 Defender portal with the correct severity and alert details.

## Rollback
1. If the pilot fails, remove all pilot users from the Defender for Identity license assignment: Set-MsolUserLicense -UserPrincipalName <user> -RemoveLicenses <license_sku_id>.
2. For Defender for Office 365, revert any custom policies by running: Remove-AntiPhishPolicy -Identity <policy_name> and Remove-HostedContentFilterPolicy -Identity <policy_name>.
3. For Defender for Endpoint, offboard the pilot machine by running: Set-MpPreference -DisableRealtimeMonitoring $true and then uninstall the Microsoft Defender for Endpoint agent via Programs and Features.
4. For Microsoft Defender for Cloud Apps, remove the app connector by navigating to the Cloud Apps portal > Settings > App connectors and deleting the connector.
5. Disable the Microsoft Defender XDR evaluation by contacting Microsoft support or using the tenant admin portal to remove the trial license.
6. Restore any default security policies that were modified during the pilot by running: Set-OrganizationConfig -IsDehydrated $true (if applicable) and re-enable any default anti-malware or anti-spam policies.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
