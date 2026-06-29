# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
What are the key activities to perform when troubleshooting Windows Autopilot?

## Environment Context
- **Tenant Type:** Microsoft Entra ID and Microsoft Intune or non-Microsoft MDM
- **Configuration:** Windows Autopilot configuration requirements

## Symptoms
- Unexpected OOBE screens displayed
- Microsoft Entra credentials page not customized with organization-specific details
- Device unable to join Microsoft Entra ID
- Device unable to enroll in Microsoft Intune or non-Microsoft MDM service

## Error Codes
N/A

## Root Causes
1. Microsoft Entra ID and Microsoft Intune or non-Microsoft MDM service not configured as specified in Windows Autopilot configuration requirements
2. Network connectivity issues preventing access to services described in Windows Autopilot networking requirements

## Remediation Steps
1. Review configuration: Are Microsoft Entra ID and Microsoft Intune or a non-Microsoft mobile device management (MDM) service configured as specified in Windows Autopilot configuration requirements?
2. Check network connectivity: Can the device access the services described in Windows Autopilot networking requirements?
3. Windows out-of-box experience (OOBE) behavior: Are the expected OOBE screens displayed? Is the Microsoft Entra credentials page customized with organization-specific details as expected?
4. Microsoft Entra join issues: Is the device able to join Microsoft Entra ID?
5. MDM enrollment issues: Is the device able to enroll in Microsoft Intune or non-Microsoft MDM service?
6. Review logs that are automatically collected upon Windows Autopilot failure. For more information, see Collect diagnostics from a Windows device.

## Validation
1. Verify Microsoft Entra ID and Intune/MDM configuration per Windows Autopilot requirements: In the Microsoft Intune admin center, navigate to Devices > Windows > Windows enrollment > Autopilot and confirm that the Autopilot deployment profile is assigned to the device group. In Microsoft Entra admin center, go to Identity > Devices > Device settings and ensure 'Users may join devices to Microsoft Entra ID' is set to 'All' or 'Selected'. For MDM, verify MDM discovery URL is configured in Microsoft Entra ID (Identity > Devices > MDM). 2. Check network connectivity: On the affected device, open a command prompt and run 'nslookup login.microsoftonline.com' and 'nslookup enterpriseregistration.windows.net' to confirm DNS resolution. Also run 'Test-NetConnection login.microsoftonline.com -Port 443' to verify TCP connectivity. 3. Validate OOBE behavior: On a test device, perform a reset and observe OOBE screens. Confirm that the Microsoft Entra credentials page shows the organization-specific branding (e.g., company logo and sign-in text). 4. Test Microsoft Entra join: On the device, run 'dsregcmd /status' and verify that 'AzureAdJoined' is 'YES' and 'DomainJoined' is 'NO'. 5. Test MDM enrollment: On the device, run 'dsregcmd /status' and check that 'MdmUrl' is set to the Intune or non-Microsoft MDM service URL and 'MdmTouUrl' is present. Also verify in Intune admin center that the device appears under Devices > All devices. 6. Collect diagnostics: If any step fails, run 'Get-AutopilotDiagnostics' from the Windows Autopilot diagnostics module or collect the MDM diagnostic logs via 'mdmdiagnosticstool.exe'.

## Rollback
1. If Autopilot profile assignment is incorrect: In Intune admin center, navigate to Devices > Windows > Windows enrollment > Autopilot, select the deployment profile, and under 'Assignments', remove the incorrect device group or modify the profile settings to match requirements. 2. If Microsoft Entra device join settings are misconfigured: In Microsoft Entra admin center, go to Identity > Devices > Device settings and revert 'Users may join devices to Microsoft Entra ID' to the previous setting (e.g., 'None' or 'Selected'). 3. If MDM discovery URL is incorrect: In Microsoft Entra admin center, go to Identity > Devices > MDM and restore the previous MDM discovery URL or clear it if not needed. 4. If network changes caused issues: Restore any firewall or proxy rules that were modified, or revert DNS settings to previous values. 5. If OOBE customization is incorrect: In Intune admin center, navigate to Devices > Windows > Windows enrollment > Autopilot, select the deployment profile, and under 'Out-of-box experience (OOBE)', revert any changed settings (e.g., hide or show screens, branding). 6. If device enrollment failed and needs to be retried: On the device, run 'dsregcmd /leave' to disjoin from Microsoft Entra ID, then restart and go through OOBE again. Alternatively, reset the device using Windows recovery options.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
