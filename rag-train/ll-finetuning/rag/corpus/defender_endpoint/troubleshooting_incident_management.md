# Troubleshooting: Incident Management

**Domain:** Defender for Endpoint
**Subdomain:** Incident Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to view and interpret incident details in Microsoft Defender XDR, including assignment, classification, categories, and description?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View an incident's details on the right pane of an incident page.
2. Review incident assignment, ID, classification, categories, and first and last activity date and time.
3. Check the incident description for a brief overview of the incident.
4. Note that in some cases, the first alert in the incident is used as the incident description.
5. Understand that the description is only shown in the portal and isn't stored in the activity log, advanced hunting tables, or the Microsoft Sentinel in Azure portal.
6. Microsoft Sentinel customers can view and overwrite the same incident description in the Azure portal by setting the incident description through API or automation.

## Validation
1. Navigate to the Microsoft Defender XDR portal (https://security.microsoft.com) and go to Incidents & alerts > Incidents. 2. Select an incident from the list and confirm the right pane displays the incident details including assignment, ID, classification, categories, first activity, last activity, and description. 3. Verify the description matches the expected content (e.g., first alert description if applicable). 4. For Microsoft Sentinel customers, confirm the description can be viewed and overwritten in the Azure portal via API or automation.

## Rollback
1. If the incident details are not displayed correctly, refresh the incident page or clear the browser cache and retry. 2. If the incident assignment or classification is incorrect, manually reassign or reclassify the incident using the edit options in the right pane. 3. If the description is missing or incorrect, restore the original description by editing the incident in the portal or, for Microsoft Sentinel customers, by resetting the description via API or automation to the previous value. 4. If the issue persists, verify network connectivity and permissions, or contact Microsoft support.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
