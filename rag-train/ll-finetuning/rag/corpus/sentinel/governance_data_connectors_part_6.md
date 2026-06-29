# Governance: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Governance

## Scenario / Query
A Microsoft Sentinel workspace is ingesting security events from multiple regions, but the workspace is located in a single Azure region. How can an organization enforce data residency requirements and ensure that logs from non-compliant regions are not stored in the Sentinel workspace?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace in East US, with data sources from West Europe and Southeast Asia

## Symptoms
- Security events from West Europe and Southeast Asia are appearing in the East US workspace
- Compliance audit flags data residency violation for EU and Asian data
- No regional data segregation is configured

## Error Codes
N/A

## Root Causes
1. No Azure Policy or Sentinel workspace-level restriction to limit data ingestion to specific geographic regions
2. Data connectors are configured to send all logs to a single workspace regardless of source region

## Remediation Steps
1. Deploy separate Microsoft Sentinel workspaces per required data residency region (e.g., one in West Europe for EU data, one in Southeast Asia for Asian data)
2. Use Azure Policy to enforce that data connectors from a specific region can only send logs to a workspace in the same region
3. Configure data connectors (e.g., Azure Activity, Azure Security Center, or third-party via CEF/Syslog) to point to the regionally appropriate workspace
4. Optionally, use Azure Lighthouse to manage multiple workspaces centrally while maintaining data residency

## Validation
Verify that logs from West Europe appear only in the West Europe Sentinel workspace and logs from Southeast Asia appear only in the Southeast Asia workspace, and no cross-region data flow exists.

## Rollback
Reconfigure data connectors to point back to the original single workspace and remove the Azure Policy assignment that restricts regional ingestion.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/design-your-workspace-architecture#data-residency-considerations>
