# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How do I interpret the 'New pending today' column in communication compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy monitoring

## Symptoms
- New pending today count may not match expectations

## Error Codes
N/A

## Root Causes
1. Value updates whenever you open the page; may not reflect real-time changes without manual refresh

## Remediation Steps
1. Select the Refresh button to get the latest count
2. Note that at the end of the UTC day, the count resets to zero

## Validation
After refreshing, the number should match the count on the Pending tab

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
