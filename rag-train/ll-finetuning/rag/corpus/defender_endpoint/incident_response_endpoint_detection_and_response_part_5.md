# Incident Response: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Incident Response

## Scenario / Query
How to investigate a contained user in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Contain User feature enabled

## Symptoms
- User has been contained due to suspicious activity
- Blocked actions by the compromised user need to be reviewed

## Error Codes
N/A

## Root Causes
1. User account compromised or exhibiting malicious behavior

## Remediation Steps
1. View blocked actions by the compromised user in the device timeline view
2. In the device timeline, examine specific events including protocol and interface granularity
3. Identify the relevant MITRE Technique associated with each event
4. Use advanced hunting to expand the investigation
5. Query the DeviceEvents table for any action type starting with 'contain'
6. Review all singular blocking events related to Contain User in the tenant
7. Dive deeper into the context of each block
8. Extract the different entities and techniques associated with those events

## Validation
1. Navigate to Microsoft Defender XDR > Device timeline for the contained user's device. 2. Filter by 'Contain User' action type and verify blocked actions are listed. 3. Run advanced hunting query: `DeviceEvents | where ActionType startswith 'Contain' | project Timestamp, DeviceName, AccountName, ActionType, AdditionalFields` and confirm results show containment events. 4. For each event, confirm MITRE technique mapping is visible in the event details.

## Rollback
1. In Microsoft Defender XDR, go to the device page for the contained user's device. 2. Select 'Release from containment' to remove the user containment. 3. Verify the user's actions are no longer blocked by checking the device timeline for 'Release containment' events. 4. If containment was applied via a conditional access policy, remove the user from the policy exclusion list or disable the policy. 5. Monitor the user's activity for 24 hours to ensure no further suspicious behavior.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
