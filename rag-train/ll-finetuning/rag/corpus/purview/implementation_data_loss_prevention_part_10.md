# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I prioritize VPN over Corporate network in Endpoint DLP network restrictions?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP network restrictions with both VPN and Corporate network selected

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If both VPN and Corporate network are selected under Network restrictions, Endpoint DLP applies the action based on the order.
2. To have the action for VPN applied, move the VPN entry above Corporate network to have higher priority.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Network restrictions. 2. Confirm that both 'VPN' and 'Corporate network' entries are present. 3. Verify that the 'VPN' entry is listed above the 'Corporate network' entry. 4. Use the 'Test' feature (if available) to simulate a file operation over VPN and confirm the intended DLP action is triggered. 5. Optionally, run the PowerShell cmdlet Get-DlpEndpointNetworkRestriction to programmatically verify the order of entries.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Network restrictions, select the 'VPN' entry and use the 'Move down' option to place it below the 'Corporate network' entry. 2. Alternatively, use the PowerShell cmdlet Set-DlpEndpointNetworkRestriction to reorder the entries, setting the priority of 'Corporate network' higher than 'VPN'. 3. Verify the change by checking the order in the portal or using Get-DlpEndpointNetworkRestriction.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
