# Troubleshooting: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How to view and manage users identified in a Microsoft Defender XDR incident?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Incident investigation interface

## Symptoms
- Users view lists all users identified as part of or related to an incident

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the check mark for a user to see details of the user account threat, exposure, and contact information.
2. Select the user name to see additional user account details.
3. To learn how to view additional user information and manage the users of an incident, see investigate users.

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents.
3. Select an incident from the list.
4. In the incident details pane, locate the 'Users' tab or section.
5. Verify that the list of users identified as part of or related to the incident is displayed.
6. Select the check mark for a user and confirm that details such as user account threat, exposure, and contact information appear.
7. Select the user name and confirm that additional user account details are shown.
8. Optionally, follow the link 'investigate users' to ensure the documentation page loads correctly.

## Rollback
1. If the users list is not visible or details are missing, refresh the incident page by pressing F5 or clicking the refresh icon.
2. If the issue persists, clear the browser cache and cookies, then reload the Microsoft 365 Defender portal.
3. Verify that the user has the required permissions (e.g., View incidents, Manage incidents) by checking roles in Microsoft 365 Defender > Permissions.
4. If the problem continues, open a support ticket with Microsoft providing the incident ID and a description of the missing user details.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
