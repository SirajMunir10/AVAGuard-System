# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I add VPN addresses to Endpoint DLP settings in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open Microsoft Purview portal and go to Data Loss Prevention > Overview > settings gear icon in the upper right corner > Data Loss Prevention > Endpoint DLP settings > VPN settings.
2. Select Add or edit VPN addresses.
3. Enter either the Server address or Network address that you recorded after running Get-VpnConnection.
4. Select Save.
5. Close the item.

## Validation
1. Open Microsoft Purview portal and navigate to Data Loss Prevention > Overview > Settings gear > Data Loss Prevention > Endpoint DLP settings > VPN settings. 2. Confirm the VPN address you added appears in the list. 3. On a domain-joined Windows device connected via that VPN, run 'Get-VpnConnection' in PowerShell and verify the ServerAddress or NetworkAddress matches the entry. 4. Test that DLP policies apply correctly on the VPN connection by attempting to copy sensitive data to an unauthorized location and confirming the action is blocked or audited.

## Rollback
1. Open Microsoft Purview portal and go to Data Loss Prevention > Overview > Settings gear > Data Loss Prevention > Endpoint DLP settings > VPN settings. 2. Select the VPN address you added and choose 'Remove' or 'Delete'. 3. Confirm removal by verifying the address no longer appears in the list. 4. On a domain-joined Windows device connected via that VPN, run 'Get-VpnConnection' to ensure the address is no longer listed in Purview settings. 5. Test that DLP policies revert to default behavior on the VPN connection.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
