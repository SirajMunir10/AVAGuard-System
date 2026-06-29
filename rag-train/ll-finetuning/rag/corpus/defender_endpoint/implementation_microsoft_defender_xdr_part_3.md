# Implementation: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Implementation

## Scenario / Query
How do I pilot and evaluate Microsoft Defender XDR components in a production tenant before full deployment?

## Environment Context
- **Tenant Type:** production
- **Configuration:** Microsoft Defender XDR

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Step through the entire process of piloting the components of Microsoft Defender XDR in your production tenant to evaluate their features and capabilities.
2. Complete the deployment across your organization after evaluation.

## Validation
1. Confirm that the Microsoft Defender XDR evaluation environment is active by navigating to the Microsoft 365 Defender portal (https://security.microsoft.com) and verifying that the 'Evaluation' or 'Pilot' banner is displayed. 2. Verify that the required licenses (e.g., Microsoft 365 E5, Microsoft Defender for Office 365 Plan 2, Microsoft Defender for Endpoint Plan 2) are assigned to at least one pilot user group. 3. Check that the pilot devices are onboarded to Microsoft Defender for Endpoint by running the following PowerShell command as an administrator on a pilot device: 'Get-MpComputerStatus | Select-Object AMRunningMode, AMProductVersion, OnboardingState'. Confirm that 'OnboardingState' is 'Onboarded'. 4. Validate that Microsoft Defender for Office 365 is enabled for the pilot user group by running the Exchange Online PowerShell command: 'Get-OrganizationConfig | Format-List Name, IsDehydrated, EOPEnabled, ATPEnabled'. Ensure 'ATPEnabled' is True. 5. Confirm that Microsoft Defender for Identity is configured by checking the Microsoft 365 Defender portal > Settings > Identities > Data sources and verifying that the domain controller is listed as a data source. 6. Verify that Microsoft Defender for Cloud Apps is connected by navigating to the Microsoft 365 Defender portal > Cloud Apps > Connected apps and confirming that at least one app (e.g., Office 365) is connected. 7. Simulate a test alert by running a non-malicious file (e.g., a PowerShell script that triggers a test alert) on a pilot device and confirm that the alert appears in the Microsoft 365 Defender portal within 10 minutes.

## Rollback
1. Remove pilot devices from Microsoft Defender for Endpoint by running the following PowerShell command on each device: 'Set-MpPreference -DisableRealtimeMonitoring $true' and then uninstall the Microsoft Defender for Endpoint agent via 'Programs and Features' or by running the uninstall script provided in the Microsoft 365 Defender portal. 2. Disable Microsoft Defender for Office 365 for the pilot user group by running the Exchange Online PowerShell command: 'Set-OrganizationConfig -ATPEnabled $false'. 3. Remove the Microsoft Defender for Identity sensor from the domain controller by running the uninstaller from 'Programs and Features' or by running the command: 'MDEInstall.exe /uninstall'. 4. Disconnect Microsoft Defender for Cloud Apps by navigating to the Microsoft 365 Defender portal > Cloud Apps > Connected apps, selecting the connected app, and clicking 'Disconnect'. 5. Remove the pilot user group from the evaluation scope by navigating to the Microsoft 365 Defender portal > Settings > Endpoints > Advanced features and disabling the 'Evaluation' toggle. 6. Revoke any pilot-specific licenses from the pilot users by using the Microsoft 365 admin center > Billing > Licenses > select the license product > 'Assign licenses' and uncheck the pilot users. 7. Clear any test alerts by navigating to the Microsoft 365 Defender portal > Incidents & alerts > Alerts, selecting the test alert, and clicking 'Manage alert' > 'Close alert' with a classification of 'False positive'.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
