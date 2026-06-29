# Troubleshooting: Password Reset (31034)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to confirm network connectivity for SSPR writeback when firewall or proxy ports are incorrectly configured?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect version 1.1.443.0 and higher

## Symptoms
- Firewall or proxy ports incorrectly configured
- Idle time-outs incorrectly configured

## Error Codes
- `31034`
- `31019`

## Root Causes
1. Outbound HTTPS access to required addresses is blocked

## Remediation Steps
1. On the Entra connect server, open the event viewer logs (Windows logs, application) and locate one of these event IDs: 31034 or 31019.
2. From these Event IDs, identify the name of the service bus listener.
3. Run the following cmdlet: Test-NetConnection -ComputerName <namespace>.servicebus.windows.net -Port 443
4. Or run the following: Invoke-WebRequest -Uri https://<namespace>.servicebus.windows.net -Verbose
5. Replace the <namespace> with the same you extracted from the event IDs previously.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
