# Incident Response: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Incident Response

## Scenario / Query
How to view insider risk activities for a user from Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Insider Risk Management data sharing enabled

## Symptoms
- Risk activities and unusual activities for a user associated with Insider Risk Management policies

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View the Insider risk activity section which displays the total number of Risk activities and total number of Unusual activities for activities associated with this user for Insider Risk Management policies
2. Select View details in this section to display a timeline of insider risk activity for the user
3. Review the timeline which includes: the insider risk severity level, totals for All activities and Unusual activities, and details for each activity associated with the user from the Activity explorer in Insider Risk Management

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > select a policy > select a user report. 2. In the user report, locate the 'Insider risk activity' section. 3. Confirm the section displays the total number of Risk activities and total number of Unusual activities for the user. 4. Select 'View details' to open the timeline. 5. Verify the timeline shows: insider risk severity level, totals for All activities and Unusual activities, and details for each activity linked to the Activity explorer in Insider Risk Management. 6. Cross-check that the activities match those in Insider Risk Management > Activity explorer for the same user.

## Rollback
1. If the Insider risk activity section is missing or incorrect, verify that Insider Risk Management data sharing is enabled in the Communication Compliance policy settings. 2. If data sharing is disabled, enable it: In Communication Compliance > Policy settings > turn on 'Share data with Insider Risk Management'. 3. If the timeline shows incomplete data, ensure the user is assigned an appropriate Insider Risk Management policy and that activities are being logged. 4. If issues persist, contact Microsoft Support to validate data synchronization between Communication Compliance and Insider Risk Management.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
