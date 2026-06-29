# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to configure VPN settings in Microsoft Purview Endpoint DLP to restrict user activities based on VPN connection?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Windows 10 and later (21H1, 21H2) with KB 5018482; Windows 11 21H2, 22H2 with KB 5018483; Windows 10 RS5 (KB 5006744)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the VPN list to control only those actions that are carried out over that VPN.
2. List a VPN in VPN Settings and assign policy actions: Allow (audit with no user notifications or alerts), Audit only (you can add notifications and alerts), Block with override (blocks the action, but the user can override), Block (blocks no matter what).
3. Apply these actions individually or collectively to user activities: Copy to clipboard, Copy to a USB removable device, Copy to a network share, Copy or move using unallowed (restricted) Bluetooth app, Copy or move using RDP.
4. Use the Server address or Network address parameters to define the VPN allowed.

## Validation
1. Verify that the VPN settings are applied correctly by running the following PowerShell command on a test device: Get-MpPreference | Select-Object -ExpandProperty DlpVpnList. 2. Confirm that the expected VPN server addresses or network addresses appear in the output. 3. Simulate a user activity (e.g., copy to clipboard) over the VPN and verify that the configured action (Allow, Audit only, Block with override, or Block) is enforced as expected. 4. Check the DLP alerts and activity reports in the Microsoft Purview compliance portal to ensure the actions are logged correctly.

## Rollback
1. Remove the VPN entry from the VPN list in the Endpoint DLP settings by navigating to Microsoft Purview compliance portal > Data loss prevention > Endpoint DLP settings > VPN settings. 2. Delete the specific server address or network address that was added. 3. Alternatively, use PowerShell to clear the VPN list: Set-MpPreference -DlpVpnList @(). 4. Verify removal by running Get-MpPreference | Select-Object -ExpandProperty DlpVpnList and confirming the list is empty or no longer contains the removed entry.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
