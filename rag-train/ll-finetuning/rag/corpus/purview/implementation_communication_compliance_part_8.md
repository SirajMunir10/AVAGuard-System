# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How do I view user activity and risk profile in Communication Compliance during investigation?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Insider Risk Management data sharing enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the User activity view in Communication Compliance.
2. This view provides risk profile, policy matches, and user activities captured by Insider Risk Management and Communication Compliance.
3. View the risk severity of the user from Insider Risk Management in the Source tab if data sharing is enabled.
4. The Communication Compliance policy matches section displays the total number of communication Policy matches and the total number of Remediation actions for the user included in this policy match.
5. Select View details in this section to display a timeline of Communication Compliance activities for the user, including totals for Policy matches and Remediation actions for the user, and details for each activity associated with the user for the past 30 days.
6. The Insider risk activity section displays the total number of Risk activities and the total number of Unusual activities for activities associated with this user for Insider Risk Management policies.

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. Select a policy and open the user activity view for a user under investigation. 2. Confirm the 'Source' tab displays risk severity from Insider Risk Management (if data sharing is enabled). 3. Verify the 'Communication Compliance policy matches' section shows total policy matches and remediation actions. 4. Select 'View details' and confirm a timeline of activities for the past 30 days appears, including policy matches and remediation actions. 5. Check the 'Insider risk activity' section for total risk activities and unusual activities.

## Rollback
1. If the user activity view does not load or shows incorrect data, verify that Insider Risk Management data sharing is enabled in the Communication Compliance settings. 2. If data sharing is disabled, enable it by navigating to Communication Compliance settings and toggling 'Share data with Insider Risk Management'. 3. If the timeline or sections are missing, ensure the user has relevant policy matches and risk activities; if not, no rollback is needed as the view depends on existing data. 4. If the issue persists, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
