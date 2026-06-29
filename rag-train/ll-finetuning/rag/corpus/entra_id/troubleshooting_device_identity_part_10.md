# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to use Event Viewer to locate error codes during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** federated
- **Configuration:** Windows 10/11 devices

## Symptoms
- Common error codes during hybrid join

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Event Viewer logs to locate the error code, suberror code, server error code, and server error message.
2. In Event Viewer, open the User Device Registration event logs. They're stored under Applications and Services Log > Microsoft > Windows > User Device Registration.
3. Look for event ID 305.

## Validation
1. Open Event Viewer on the affected Windows 10/11 device. 2. Navigate to Applications and Services Log > Microsoft > Windows > User Device Registration. 3. Look for event ID 305. 4. Confirm that the event contains the error code, suberror code, server error code, and server error message as described in the remediation steps. 5. Verify that the error codes match known hybrid join issues and that no new errors appear after remediation.

## Rollback
1. If the remediation causes issues, restore the device to its previous state by reverting any configuration changes made during troubleshooting. 2. If Event Viewer logs were cleared or modified, restore from backup if available. 3. Re-run the hybrid join process using the original settings. 4. Consult the official troubleshooting guide at https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current for additional recovery steps.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
