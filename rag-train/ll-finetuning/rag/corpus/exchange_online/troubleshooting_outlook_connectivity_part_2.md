# Troubleshooting: Outlook Connectivity

**Domain:** Exchange Online
**Subdomain:** Outlook Connectivity
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix out-of-date software and corrupted Outlook profiles that prevent sending and receiving email?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange Online

## Symptoms
- Cannot send or receive email
- Multiple users reporting problems

## Error Codes
N/A

## Root Causes
1. Out-of-date Outlook client software
2. Out-of-date Windows operating system software
3. Corrupted Outlook profiles
4. Service issues with Microsoft 365

## Remediation Steps
1. Run Windows Update to ensure latest updates for Outlook and other desktop applications for Microsoft 365
2. Run a Microsoft 365 Diagnostic: Select Run Tests: Outlook User Connectivity to download and run the diagnostic (requires Microsoft 365 administrator account; not available for Microsoft 365 Government, Microsoft 365 operated by 21Vianet, or Microsoft 365 Germany)
3. Admin only: If more than one person is experiencing email problems, go to Microsoft 365 Service health status (admin sign in required) and check the status of services under Exchange Online

## Validation
1. Confirm Windows Update history shows the latest updates installed: Run 'Get-WUHistory | Select-Object -First 10' in PowerShell. 2. Run the Microsoft 365 Diagnostic: Navigate to https://aka.ms/OutlookConnectivity, sign in with a Microsoft 365 administrator account, and run the 'Outlook User Connectivity' test. Verify the test returns 'Pass' with no connectivity errors. 3. Check Microsoft 365 Service Health: Sign in to the Microsoft 365 admin center at https://admin.microsoft.com, go to Health > Service Health, and confirm Exchange Online shows 'Healthy' or 'Service restored' with no active incidents.

## Rollback
1. If Windows Update causes issues, uninstall the most recent update: Go to Settings > Update & Security > Windows Update > View update history > Uninstall updates, select the latest update, and click Uninstall. 2. If the diagnostic tool indicates a problem, follow the on-screen remediation steps provided by the tool; no manual rollback is needed. 3. If service health shows an active incident, no rollback is possible—wait for Microsoft to resolve the issue and monitor the service health dashboard for updates.

## References
- <https://learn.microsoft.com/en-us/exchange/troubleshoot/outlook-connectivity/outlook-connection-issues>
