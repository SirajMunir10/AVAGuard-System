# Troubleshooting: Device Actions (Not Supported)

**Domain:** Intune
**Subdomain:** Device Actions
**Incident Type:** Troubleshooting

## Scenario / Query
Why do I get a 'Not Supported' message when I issue a passcode reset to my Android 8.0 or later personally owned work profile enrolled device?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Android 8.0 or later personally owned work profile enrolled device

## Symptoms
- Not Supported message when issuing a passcode reset

## Error Codes
- `Not Supported`

## Root Causes
1. The reset token hasn't been activated on the device

## Remediation Steps
1. Require a personally owned work profile passcode in your configuration policy
2. The end user must set an appropriate personally owned work profile passcode
3. The end user must accept the secondary prompt to allow passcode reset

## Validation
After these steps are complete, you should no longer receive this response

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/remote-actions/troubleshoot-device-actions>
