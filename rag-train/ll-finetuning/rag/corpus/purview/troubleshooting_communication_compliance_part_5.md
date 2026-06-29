# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to quickly review policy matches on the Pending or Resolved tab in Communication Compliance?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Need to determine the condition or conditions that caused a policy match
- Multiple conditions may be present for a policy match

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select a message to review on the Pending tab or the Resolved tab
2. Look for the alert message bar (yellow banner) at the top of the Source tab
3. If there are multiple conditions, select View all in the banner to see all the conditions that caused the policy match

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policy. 2. Select a policy and click the Pending tab. 3. Click a message to open it. 4. Verify that a yellow banner appears at the top of the Source tab indicating the condition(s) that caused the match. 5. If the banner shows 'View all', click it and confirm a list of all matching conditions is displayed. 6. Repeat steps 2–5 for the Resolved tab.

## Rollback
1. If the yellow banner does not appear or conditions are missing, close the message and re-select it from the same tab. 2. If the issue persists, clear browser cache and re-login to the Purview portal. 3. If still unresolved, verify that the policy is still active and assigned to the correct users/groups. 4. As a last resort, recreate the policy with the same conditions and re-run the investigation.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
