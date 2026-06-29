# Hardening: Data Map

**Domain:** Purview
**Subdomain:** Data Map
**Incident Type:** Hardening

## Scenario / Query
How can I harden my Microsoft Purview account by disabling public network access and enforcing private endpoint connections?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Purview (formerly Azure Purview) account with public network access enabled

## Symptoms
- Data map is accessible over the public internet
- Security compliance scanners flag the account as having public endpoints enabled
- Audit logs show connection attempts from unknown public IP addresses

## Error Codes
N/A

## Root Causes
1. The Purview account was created with public network access set to 'Enabled'
2. No private endpoint was configured for the Purview account
3. Network isolation requirements were not applied during deployment

## Remediation Steps
1. Navigate to the Microsoft Purview account in the Azure portal.
2. Under 'Settings', select 'Networking'.
3. Set 'Public network access' to 'Disabled'.
4. Under 'Private endpoint connections', create a new private endpoint for the Purview account following the documented guidance.
5. Ensure the private endpoint is in the same virtual network as your data sources and scanning infrastructure.
6. After disabling public access, update any scanning runtimes or integration runtimes to use the private endpoint DNS configuration.

## Validation
After remediation, attempt to access the Purview account's data map endpoint from a public IP address. The connection should be refused. Then verify that scanning and data ingestion still succeed via the private endpoint.

## Rollback
Re-enable public network access in the Networking settings of the Purview account, and remove the private endpoint if no longer needed.

## References
- <https://learn.microsoft.com/en-us/purview/configure-private-endpoints?tabs=portal#disable-public-network-access>
