# Troubleshooting: Device Registration (304)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to find the phase and error code when a Microsoft Entra hybrid join fails on earlier Windows 10 versions?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Earlier Windows 10 versions, domain-joined device unable to Microsoft Entra hybrid join

## Symptoms
- Device is domain-joined but unable to Microsoft Entra hybrid join

## Error Codes
- `304`
- `305`
- `307`

## Root Causes
N/A

## Remediation Steps
1. In Event Viewer, open the User Device Registration event logs under Applications and Services Log > Microsoft > Windows > User Device Registration.
2. Look for events with event IDs 304, 305, and 307.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
