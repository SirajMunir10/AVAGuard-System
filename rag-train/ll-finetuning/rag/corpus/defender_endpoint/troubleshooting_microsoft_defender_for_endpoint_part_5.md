# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to check activity details and status of actions taken on a device or file in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Action center at https://security.microsoft.com/action-center

## Symptoms
- Unable to determine if an action on a device or file succeeded or failed
- Need to view submission date/time and submitting user for actions

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Action center at https://security.microsoft.com/action-center
2. View details such as investigation package collection, antivirus scan, app restriction, and device isolation
3. Check submission date/time, submitting user, and action success or failure status
4. Alternatively, use the Activities tab in the Incident page to track action details and status

## Validation
Verify that the action status (succeeded or failed) and all related details are displayed in the Action center or Activities tab

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
