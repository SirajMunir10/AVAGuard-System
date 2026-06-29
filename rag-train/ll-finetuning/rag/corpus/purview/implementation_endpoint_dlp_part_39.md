# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to retrieve VPN server address and network name for configuring VPN settings in Endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP VPN settings configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On a DLP monitored Windows device, open a Windows PowerShell window as an administrator.
2. Run the following cmdlet: Get-VpnConnection
3. Among the results of the cmdlet, find the ServerAddress field and record that value. Use the ServerAddress when you create a VPN entry in the VPN list.
4. Find the Name field and record that value. The Name field maps to the Network address field when you create a VPN entry in the VPN list.

## Validation
On a DLP-monitored Windows device, open PowerShell as administrator and run: Get-VpnConnection. Confirm that the output includes a ServerAddress and a Name for each VPN connection. Then, in the Microsoft Purview compliance portal, navigate to Endpoint DLP settings > VPN settings, and verify that the VPN entries you created match the ServerAddress and Name values retrieved from the cmdlet.

## Rollback
In the Microsoft Purview compliance portal, go to Endpoint DLP settings > VPN settings, select the VPN entry you added, and delete it. If the remediation caused connectivity issues, on the Windows device, run the following PowerShell cmdlet as administrator to restore the original VPN configuration: Set-VpnConnection -Name "<OriginalName>" -ServerAddress "<OriginalServerAddress>" -PassThru, replacing placeholders with the original values.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
