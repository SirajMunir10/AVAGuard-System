# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender for Endpoint onboarding issues when deploying with deployment tools?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** Onboarding process with deployment tools

## Symptoms
- Issues encountered during the onboarding process when deploying with one of the deployment tools
- Common errors on devices during onboarding

## Error Codes
N/A

## Root Causes
1. Minimum requirements for onboarding devices to the services may not be met

## Remediation Steps
1. Check if the minimum requirements are met for onboarding devices to the services
2. Learn about the licensing, hardware, and software requirements to onboard devices to the service
3. Review the Microsoft Defender for Endpoint setup guide for best practices and essential tools such as attack surface reduction and next-generation protection
4. Access the Defender for Endpoint automated setup guide in the Microsoft 365 admin center for a customized experience based on your environment

## Validation
1. Verify that each device meets the minimum hardware, software, and licensing requirements as documented in 'Minimum requirements for Microsoft Defender for Endpoint' (https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements).
2. On a test device, run the command: `Get-MpComputerStatus | Select-Object AMProductVersion, AMServiceEnabled, AntispywareEnabled, AntivirusEnabled` to confirm the antimalware client is installed and running.
3. Check the onboarding status by running: `Get-MpPreference | Select-Object -ExpandProperty CloudServiceEnabled` – expected value is True.
4. Review the Microsoft Defender for Endpoint deployment guide and ensure all prerequisites (e.g., Windows version, licensing) are satisfied.
5. Use the Microsoft 365 admin center automated setup guide to validate the configuration matches your environment.

## Rollback
1. If onboarding fails, remove the device from the deployment tool's target group to prevent further attempts.
2. On the affected device, run the command: `Set-MpPreference -DisableRealtimeMonitoring $true` to temporarily disable real-time protection if it interferes with troubleshooting.
3. Uninstall the Defender for Endpoint sensor using the deployment tool or manually via 'Add or Remove Programs' (look for 'Microsoft Defender for Endpoint' or 'Windows Defender Advanced Threat Protection').
4. Revert any group policy or configuration changes that were applied for onboarding.
5. Re-enable real-time monitoring if disabled: `Set-MpPreference -DisableRealtimeMonitoring $false`.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
