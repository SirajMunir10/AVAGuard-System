# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why did enrollments start failing when using the Intune Connector for Active Directory?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Intune Connector for Active Directory

## Symptoms
- Enrollments failing when using the Intune Connector for Active Directory

## Error Codes
N/A

## Root Causes
1. Intune Connector for Active Directory is outdated or legacy version is still being used

## Remediation Steps
1. Update the Intune Connector for Active Directory to version 6.2501.2000.5 or later
2. Ensure the legacy version isn't still being used

## Validation
1. On the server hosting the Intune Connector for Active Directory, open 'Programs and Features' (appwiz.cpl) and verify the installed version is 6.2501.2000.5 or later. 2. Run 'Get-Service -Name IntuneConnector*' in PowerShell and confirm the service status is 'Running'. 3. Check the Intune Connector logs at %ProgramData%\Microsoft\Intune\IntuneConnector\Logs for any errors. 4. In the Microsoft Intune admin center, navigate to 'Tenant administration' > 'Connectors and tokens' > 'Windows Autopilot' and verify the connector shows a 'Healthy' status.

## Rollback
1. If the update fails or causes issues, uninstall the current Intune Connector via 'Programs and Features'. 2. Reinstall the previous known-working version from the Microsoft Intune Connector download page. 3. Restart the Intune Connector service: 'Restart-Service -Name IntuneConnector*'. 4. Re-run the validation steps to confirm the connector returns to a healthy state.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
- <https://learn.microsoft.com/en-us/mem/intune/fundamentals/intune-connector-for-active-directory-requirements>
