# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve an alert when a user has an out-of-office message turned on and is not tagged as high risk?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- User has Out-of-office message turned on
- User isn't tagged as high risk

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If both conditions are true, SecOps marks the alert as legitimate travel and resolves it.
2. A notification is posted in Microsoft Teams after the alert is resolved.

## Validation
1. Confirm the user's out-of-office message is enabled by checking their mailbox settings in Exchange Online: Get-Mailbox -Identity <user> | Select-Object AutoReplyState, AutoReplyMessage. 2. Verify the user is not tagged as high risk in Microsoft Defender XDR by reviewing the user's risk level in the Microsoft 365 Defender portal under Incidents & alerts > Alerts > select the alert > User details. 3. Ensure the alert is marked as 'Resolved' with classification 'Legitimate travel' in the Microsoft 365 Defender portal. 4. Check the Microsoft Teams channel configured for alert notifications to confirm a notification was posted after resolution.

## Rollback
1. If the alert was incorrectly resolved, reopen it in the Microsoft 365 Defender portal by selecting the alert and choosing 'Reopen'. 2. Remove the 'Legitimate travel' classification by editing the alert and setting classification to 'Not set' or appropriate value. 3. If needed, disable the user's out-of-office message via Exchange Online: Set-Mailbox -Identity <user> -AutoReplyState Disabled. 4. If the Teams notification was posted in error, delete the message from the Teams channel manually.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
