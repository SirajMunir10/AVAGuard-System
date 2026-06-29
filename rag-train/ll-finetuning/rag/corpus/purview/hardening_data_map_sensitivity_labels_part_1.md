# Hardening: Data Map / Sensitivity Labels

**Domain:** Purview
**Subdomain:** Data Map / Sensitivity Labels
**Incident Type:** Hardening

## Scenario / Query
How do I harden Microsoft Purview by disabling public network access and enforcing private endpoint connections for the Microsoft Purview account?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Purview account with public network access enabled

## Symptoms
- Data sources can connect to the Purview account over the public internet
- No private endpoint configured for the Purview account
- Security team identifies risk of data exfiltration via public endpoints

## Error Codes
N/A

## Root Causes
1. Public network access is set to 'Enabled' on the Purview account
2. No private endpoint connections have been created or approved for the Purview account

## Remediation Steps
1. 1. In the Azure portal, navigate to your Microsoft Purview account.
2. 2. Under 'Settings', select 'Network'.
3. 3. Set 'Public network access' to 'Disabled'.
4. 4. Under 'Private endpoint connections', create a new private endpoint for the Purview account following the documented procedure.
5. 5. Approve the private endpoint connection in the Purview account networking blade.
6. 6. Verify that all data sources are configured to use the private endpoint DNS zone.

## Validation
Confirm that 'Public network access' is set to 'Disabled' and that the private endpoint connection status shows 'Approved' in the Purview account networking blade.

## Rollback
Set 'Public network access' back to 'Enabled' and remove the private endpoint connection if needed.

## References
- <https://learn.microsoft.com/en-us/purview/configure-private-endpoints>
