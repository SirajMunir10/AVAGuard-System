# Troubleshooting: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve advanced hunting queries blocked due to CPU resource limits?

## Environment Context
- **Tenant Type:** Defender XDR
- **Configuration:** CPU resources quota based on tenant size, evaluated every 15 minutes

## Symptoms
- Portal displays a warning when tenant consumes over 10% of allocated resources
- Queries are blocked if tenant reaches 100% until after the next 15-minute cycle

## Error Codes
N/A

## Root Causes
1. Tenant consumes over 10% of allocated CPU resources
2. Tenant reaches 100% of allocated CPU resources

## Remediation Steps
1. Wait until after the next 15-minute cycle for queries to be unblocked
2. Apply optimization best practices to minimize disruptions

## Validation
1. Check the advanced hunting page in the Microsoft 365 Defender portal to confirm the warning banner is no longer displayed. 2. Run a sample advanced hunting query and verify it executes without being blocked. 3. Review the 'Advanced hunting' > 'Resource consumption' section to confirm CPU usage is below 10% of the tenant's allocated quota.

## Rollback
1. If queries remain blocked, wait for the next 15-minute cycle to complete. 2. If the warning persists, review and optimize existing queries by reducing time range, using more specific filters, and avoiding repeated joins. 3. If issues continue, contact Microsoft support for quota adjustment or further guidance.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
