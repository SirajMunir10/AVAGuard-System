# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot device onboarding issues related to internet connectivity for Microsoft Defender for Endpoint sensor?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Microsoft Windows HTTP (WinHTTP) configuration

## Symptoms
- Sensor fails to report data
- Sensor cannot communicate with Microsoft Defender for Endpoint service

## Error Codes
N/A

## Root Causes
1. Device lacks Internet connection
2. WinHTTP cannot detect proxy servers in the environment
3. Proxy configuration prevents connectivity

## Remediation Steps
1. Ensure the device has an Internet connection
2. Verify client connectivity to Microsoft Defender for Endpoint service URLs as described in the 'Verify client connectivity to Microsoft Defender for Endpoint service URLs' topic
3. If verification fails and environment uses a proxy, configure proxy and Internet connectivity settings as described in the 'Configure proxy and Internet connectivity settings' topic

## Validation
1. Run 'Test-NetConnection -ComputerName <DefenderEndpointURL> -Port 443' to verify connectivity to the service URLs listed in the 'Verify client connectivity to Microsoft Defender for Endpoint service URLs' topic.
2. Execute 'netsh winhttp show proxy' to confirm WinHTTP proxy settings match the environment's proxy configuration.
3. Check the Microsoft Defender for Endpoint sensor status via 'Get-MpComputerStatus | Select-Object -Property CloudConnectionState' to ensure it reports 'Connected'.

## Rollback
1. If connectivity tests fail after remediation, restore previous WinHTTP proxy settings using 'netsh winhttp reset proxy'.
2. Revert any changes to Windows Firewall rules or network configuration that were modified to allow connectivity.
3. If the device was added to a proxy bypass list, remove the bypass entry and re-enable the original proxy configuration.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
