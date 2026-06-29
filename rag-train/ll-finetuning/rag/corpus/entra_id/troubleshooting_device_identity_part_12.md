# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to find the error code from Microsoft Entra analytics and operational logs for a failed PRT acquisition on earlier Windows versions?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows versions earlier than Windows 10 May 2021 update (version 21H1)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Event Viewer to look for the log entries logged by the Microsoft Entra CloudAP plug-in during PRT acquisition.
2. In Event Viewer, open the Microsoft Entra Operational event logs. They're stored under Applications and Services Log > Microsoft > Windows > AAD.
3. The CloudAP plug-in logs error events in the operational logs, and it logs the info events in the analytics logs.
4. The analytics and operational log events are both required to troubleshoot issues.

## Validation
1. Open Event Viewer. 2. Navigate to Applications and Services Log > Microsoft > Windows > AAD. 3. Open the Operational log. 4. Look for error events from the CloudAP plug-in. 5. Note the error code from the event details. 6. Open the Analytic log. 7. Look for info events from the CloudAP plug-in. 8. Confirm that both logs contain relevant events for the PRT acquisition attempt.

## Rollback
1. Close Event Viewer. 2. No configuration changes were made, so no rollback is required. 3. If logs were cleared or modified, restore from backup or re-enable logging by ensuring the Analytic log is enabled (right-click Analytic, select Enable Log).

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
