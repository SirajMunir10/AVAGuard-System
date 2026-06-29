# Troubleshooting: Password Reset Writeback (ServiceBusWarning)

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot ServiceBusWarning event in SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback configuration

## Symptoms
- Retry to connect to tenant's Service Bus instance

## Error Codes
- `ServiceBusWarning`

## Root Causes
1. High-latency or low-bandwidth network connection to Service Bus

## Remediation Steps
1. Check network connection to Service Bus, especially if it is a high-latency or low-bandwidth connection

## Validation
1. Run a network connectivity test to the Service Bus endpoint: Test-NetConnection <servicebus-namespace>.servicebus.windows.net -Port 5671 (or 5672 for AMQP). 2. Measure latency and bandwidth: Use tools like tracert, ping, or iperf to confirm latency < 200ms and bandwidth > 1 Mbps. 3. Check SSPR writeback logs in Entra ID: Sign in to the Entra admin center, navigate to 'Identity' > 'Users' > 'Password reset' > 'Audit logs', and filter for 'ServiceBusWarning' events. Confirm no new warnings after remediation.

## Rollback
1. If network changes were made (e.g., firewall rules, proxy settings), revert to the previous configuration. 2. If the Service Bus connection was reconfigured (e.g., endpoint or namespace), restore the original settings. 3. Re-enable SSPR writeback if it was disabled during troubleshooting: In Entra admin center, go to 'Password reset' > 'Properties', set 'Password writeback' to 'Yes'. 4. Monitor audit logs for recurrence of ServiceBusWarning events.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
