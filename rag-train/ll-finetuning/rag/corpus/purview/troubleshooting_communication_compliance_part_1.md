# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the 'Messages scanned today' column showing 0 or a low number for my communication compliance policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy configuration

## Symptoms
- Messages scanned today column shows 0 or a low number
- Policy may not be scanning expected messages

## Error Codes
N/A

## Root Causes
1. The policy might be too strict, for example, focused on just one user or on just one location that the in-scope user doesn't use

## Remediation Steps
1. Review the policy scope to ensure it covers the intended users and locations
2. Adjust the policy to be less restrictive if it is too narrowly focused

## Validation
Check the 'Messages scanned today' column after policy adjustment; it refreshes automatically once per hour and resets at end of UTC day

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
