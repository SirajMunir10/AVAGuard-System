# Troubleshooting: Device Authentication (AADSTS50155)

**Domain:** Entra ID
**Subdomain:** Device Authentication
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve AADSTS50155: Device authentication failed during hybrid join?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Microsoft Entra ID is unable to authenticate the device to issue a PRT

## Error Codes
- `AADSTS50155`

## Root Causes
1. Device is deleted or disabled

## Remediation Steps
1. Confirm that the device isn't deleted or disabled
2. Follow instructions in Microsoft Entra device management FAQ to re-register the device based on the device join type

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
