# Governance: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Governance

## Scenario / Query
A Microsoft Sentinel workspace is ingesting security events from multiple regions, but the workspace itself is located in a single Azure region. The security team needs to ensure that data residency requirements are met and that no data is being stored outside the approved geographic boundary. How can an administrator verify and enforce data residency for Sentinel workspaces?

## Environment Context
- **Tenant Type:** Enterprise (multi-region)
- **Configuration:** Microsoft Sentinel workspace regional configuration and data ingestion sources

## Symptoms
- Security events from multiple Azure regions are being sent to a single Sentinel workspace
- Compliance team flags potential data residency violation
- No current mechanism to restrict data ingestion based on source region

## Error Codes
N/A

## Root Causes
1. Sentinel workspace is deployed in a single region but ingests data from sources in other regions
2. No data residency policy or Azure Policy enforcement is applied to restrict workspace creation or data ingestion to approved regions

## Remediation Steps
1. Review the Microsoft Sentinel workspace location and ensure it matches the approved data residency region
2. Use Azure Policy to enforce that Sentinel workspaces can only be created in approved regions
3. Configure data connectors to only collect logs from sources within the same region as the workspace, or use Azure Policy to restrict data collection to approved regions
4. For multi-region scenarios, deploy separate Sentinel workspaces per region and use cross-workspace queries or Azure Lighthouse for centralized monitoring

## Validation
Verify that all Sentinel workspaces are located in the approved region(s) and that no data is being ingested from unapproved regions. Use Azure Policy compliance dashboard to confirm policy enforcement.

## Rollback
If a workspace must be moved to a different region, create a new workspace in the target region, reconfigure data connectors, and migrate analytics rules and workbooks. Delete the old workspace after confirming data ingestion is complete.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard#plan-for-data-residency>
- <https://learn.microsoft.com/en-us/azure/governance/policy/overview>
