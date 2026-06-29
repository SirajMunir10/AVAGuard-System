# Troubleshooting: Windows Autopilot (0x80004005)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Entra hybrid join Autopilot deployments that time out with error code 0x80004005?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid
- **Configuration:** Windows Autopilot deployment for hybrid join

## Symptoms
- Devices experience timeout errors during deployment process

## Error Codes
- `0x80004005`

## Root Causes
1. Not specified in source

## Remediation Steps
1. Apply KB5065789 or later for 25H2
2. Apply KB5065426 or later for 24H2
3. Apply KB5070312 or later for 23H2

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
