# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How does the Service domains setting interact with DLP policy actions (Block with override, Audit only, Block) when a user uploads sensitive data to a domain that is not on the Allow list?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with Service domains set to Allow; at least one service domain must be configured before enforcement.

## Symptoms
- Upload of sensitive file to a domain not on the Allow list is blocked with override option
- Audit event generated when override is chosen
- Alert triggered when override is chosen

## Error Codes
N/A

## Root Causes
1. Service domain not on Allow list triggers policy enforcement based on the configured action (Block with override, Audit only, or Block)

## Remediation Steps
1. Add the desired service domain to the Allow list using FQDN format without ending period (e.g., contoso.com)
2. Ensure at least one service domain is configured before the system enforces restrictions

## Validation
Test upload of sensitive file to the allowed domain; verify upload completes, audit event generated, no alert triggered.

## Rollback
Remove the domain from the Allow list to revert to default enforcement behavior.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
