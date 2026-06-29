# Incident Response: Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How to view the history of contain user actions in Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Defender for Endpoint onboarded devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View the contain user actions in the History view of the Action Center.
2. Check when the action occurred and which users in your organization were contained.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Action Center > History.
3. Filter by 'Contain user' action type.
4. Confirm that the list shows the expected contain user actions with timestamps and affected user accounts.

## Rollback
1. In the Microsoft 365 Defender portal, go to Action Center > History.
2. Locate the contain user action you need to revert.
3. Select the action and choose 'Release user' (or 'Uncontain user') to restore the user's access.
4. Verify the user is no longer contained by checking the user's status in the Action Center history or by attempting to access a blocked resource.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
