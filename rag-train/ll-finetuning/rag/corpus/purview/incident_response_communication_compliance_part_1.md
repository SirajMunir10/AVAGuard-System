# Incident Response: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Incident Response

## Scenario / Query
How to investigate unusual user activities in Communication Compliance using the timeline and insider risk data?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Insider Risk Management data sharing enabled

## Symptoms
- Unusual activities for a user that are considered potentially risky and a departure from typical activities

## Error Codes
N/A

## Root Causes
1. User activities that are unusual and a departure from typical activities

## Remediation Steps
1. Select View details in the Unusual activities section to display a timeline of insider risk activity for the user
2. Review the timeline which includes: insider risk severity level, totals for All activities and Unusual activities, and details for each activity from the Activity explorer in Insider Risk Management
3. To view insider risk activities in insider risk management, select Open in insider risk management
4. Review the Timeline section which displays a history of all communications for user activities
5. For each Copilot interaction, review the user prompt and Copilot response details with date and time in UTC
6. View the User activity section to see risk profile, policy matches, and user activities captured by Insider Risk Management and Communication Compliance
7. View the risk severity of the user from Insider Risk Management in the Source tab if data sharing is enabled

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > select the relevant policy. 2. For the user in question, click 'View details' in the Unusual activities section. 3. Confirm the timeline displays insider risk severity level, totals for All activities and Unusual activities, and details for each activity from the Activity explorer in Insider Risk Management. 4. Click 'Open in insider risk management' and verify the Timeline section shows a history of all communications for user activities. 5. For each Copilot interaction, verify the user prompt and Copilot response details with date and time in UTC are displayed. 6. In the User activity section, confirm risk profile, policy matches, and user activities captured by Insider Risk Management and Communication Compliance are visible. 7. If data sharing is enabled, in the Source tab verify the risk severity of the user from Insider Risk Management is displayed.

## Rollback
1. If the timeline or activity details are not loading correctly, refresh the Communication Compliance policy page and re-select the user. 2. If insider risk data is missing, verify that Insider Risk Management data sharing is enabled in the Communication Compliance policy settings. 3. If Copilot interaction details are incomplete, check that the user has a valid Copilot license and that Copilot data is being captured in the policy. 4. If the User activity section does not show expected data, ensure the user is assigned to the appropriate Insider Risk Management policy and that data sharing is enabled. 5. If the Source tab does not display risk severity, confirm that Insider Risk Management data sharing is enabled in the Communication Compliance policy settings and that the user has risk severity data in Insider Risk Management.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
