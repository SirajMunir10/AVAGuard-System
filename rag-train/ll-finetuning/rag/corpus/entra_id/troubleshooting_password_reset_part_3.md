# Troubleshooting: Password Reset (32002)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error 32002 'Error Connecting to ServiceBus' during password writeback?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Microsoft Entra Connect machine event log contains error 32002 thrown by PasswordResetService
- Error reads: 'Error Connecting to ServiceBus. The token provider was unable to provide a security token.'

## Error Codes
- `32002`

## Root Causes
1. On-premises environment isn't able to connect to the Azure Service Bus endpoint in the cloud
2. Firewall rule blocking an outbound connection to a particular port or web address

## Remediation Steps
1. Update firewall rules to allow outbound connections to the Azure Service Bus endpoint
2. Restart the Microsoft Entra Connect server

## Validation
Password writeback should start working again after updating rules and restarting

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
