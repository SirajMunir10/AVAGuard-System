# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot a Communication Compliance policy that shows 0 or low messages scanned today?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policies configured in Microsoft Purview portal

## Symptoms
- Messages scanned today column shows 0 or a low number

## Error Codes
N/A

## Root Causes
1. Policy might be too strict, for example focused on just one user or just one location that the in-scope user doesn't use

## Remediation Steps
1. Review the policy configuration to ensure it is not overly restrictive
2. Adjust the policy scope to include appropriate users and locations

## Validation
1. In the Microsoft Purview compliance portal, navigate to Communication Compliance > Policies. 2. Select the policy in question and review the 'Status' and 'Messages scanned today' column. 3. Confirm the count is now greater than zero and reflects expected message volume. 4. Optionally, use the 'Export logs' feature to download a detailed report of scanned messages for the day to verify the increase.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Communication Compliance > Policies. 2. Select the policy that was modified. 3. Under 'Policy settings', revert the scope to the original users, groups, or locations that were in place before the adjustment. 4. Save the policy and monitor the 'Messages scanned today' column to ensure it returns to the previous low or zero count.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
