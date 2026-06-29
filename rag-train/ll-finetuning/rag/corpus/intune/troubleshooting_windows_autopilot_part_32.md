# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why does uninstalling the Intune Connector for Active Directory through the Settings app not fully remove the application?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Uninstalling the Intune Connector for Active Directory through the Settings app does not fully remove the application

## Error Codes
N/A

## Root Causes
1. The Intune Connector for Active Directory needs to be uninstalled using both the Settings app and the Intune Connector for Active Directory installed executable ODJConnectorBoostrapper.exe

## Remediation Steps
1. Run ODJConnectorBoostrapper.exe and select the Uninstall option
2. Ensure the ODJConnectorBoostrapper.exe installer version matches the version of the connector that's being uninstalled

## Validation
1. Open Control Panel > Programs and Features and verify that 'Intune Connector for Active Directory' is no longer listed.
2. Run 'services.msc' and confirm that the 'Intune Connector for Active Directory' service is not present.
3. Check the registry key 'HKLM\SOFTWARE\Microsoft\Intune\ODJConnector' and ensure it does not exist.
4. Verify that the folder 'C:\Program Files\Microsoft Intune\ODJConnector' has been removed.
5. Optionally, run 'ODJConnectorBootstrapper.exe /uninstall' from an elevated command prompt to confirm no components remain.

## Rollback
1. If the uninstall was incomplete or caused issues, reinstall the Intune Connector for Active Directory by downloading the matching version of ODJConnectorBootstrapper.exe from the Microsoft Intune admin center.
2. Run the installer with default settings to restore the connector.
3. After installation, verify the service 'Intune Connector for Active Directory' is running and the connector appears in the Intune admin center under 'Tenant administration > Connectors and tokens'.
4. If the connector still fails, use the same ODJConnectorBootstrapper.exe to perform a repair installation by selecting the 'Repair' option.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
