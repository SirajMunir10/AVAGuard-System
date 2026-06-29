# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to use the Notify feature to send a warning notice to a user in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance notice templates

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Notify to assign a custom notice template to the message and send a warning notice to the user.
2. Choose the appropriate notice template configured in the Communication Compliance settings area.
3. Select Send to email a reminder to the user that sent the message and to resolve the issue.

## Validation
1. Confirm the notice template is assigned: In the Microsoft 365 Purview compliance portal, navigate to Communication Compliance > Policies > select the relevant policy > open the message in the investigation view. Verify that the 'Notify' action is available and that the correct notice template is selected. 2. Verify the notice was sent: Check the message details for a 'Notice sent' indicator or review the audit log (Search > Audit log search) for 'Sent a notice to a user' activity. 3. Confirm user resolution: In the same message view, ensure the message status changes to 'Resolved' after sending the notice.

## Rollback
1. If the notice was sent in error, contact the user to disregard the warning. 2. To prevent further incorrect notices, temporarily disable the notice template: In Communication Compliance > Settings > Notice templates, select the template and set its status to 'Inactive'. 3. If the policy itself is causing issues, disable the policy: In Communication Compliance > Policies, select the policy and choose 'Disable policy'.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
