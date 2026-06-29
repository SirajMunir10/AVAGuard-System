# Hardening: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Hardening

## Scenario / Query
A Microsoft Sentinel workspace is ingesting security events from multiple sources, but the customer wants to ensure that only authorized data connectors are enabled and that unused or risky connectors are disabled to reduce the attack surface. How can an administrator audit and disable unused data connectors in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with multiple data connectors enabled, some of which are no longer in use or are considered high-risk.

## Symptoms
- Unused data connectors are visible in the Microsoft Sentinel Data connectors blade
- Security team wants to minimize the number of active data connectors to reduce potential misconfiguration or abuse
- No clear process to identify which connectors are actively sending data versus those that are idle

## Error Codes
N/A

## Root Causes
1. Data connectors were enabled during initial deployment and never reviewed or disabled
2. Lack of a formal data connector lifecycle management process
3. No monitoring of connector health or data ingestion status

## Remediation Steps
1. Navigate to Microsoft Sentinel > Data connectors blade to review all enabled connectors
2. For each connector, check the 'Status' column and the 'Data received' graph to determine if it is actively sending data
3. For connectors that are not actively sending data and are not required, select the connector and click 'Disconnect' to disable it
4. Document the decision and maintain a list of approved connectors in the organization's security operations procedures

## Validation
After disabling unused connectors, verify that the connector no longer appears in the list of enabled connectors and that no new data is ingested from that source. Confirm with the security team that the disabled connectors are not needed for any active use case.

## Rollback
To re-enable a disabled connector, navigate to the Data connectors blade, select the connector, and follow the configuration steps to reconnect it. Note that historical data from that connector remains in the workspace.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference>
