# Troubleshooting: Windows Autopilot (400)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
When trying to import a CSV file with a device hardware hash, why does nothing happen when selecting Import?

## Environment Context
- **Tenant Type:** Azure AD/Entra ID tenant with Windows Autopilot
- **Configuration:** CSV file containing device hardware hash for Autopilot import

## Symptoms
- Nothing happens when selecting Import in the Autopilot device import process
- Error 400 occurs in network trace

## Error Codes
- `400`
- `Cannot convert the literal '[DEVICEHASH]' to the expected type 'Edm.Binary'`

## Root Causes
1. Device hash in the CSV file is incorrectly formatted
2. Hash is Base64 encoded as unpadded Base64 at the device level, but Windows Autopilot expects padded Base64
3. Payload doesn't line up cleanly and padding is necessary

## Remediation Steps
1. Modify the hash to ensure proper Base64 padding
2. Test the hash using PowerShell: [System.Text.Encoding]::ascii.getstring( [System.Convert]::FromBase64String("DEVICE HASH"))
3. If decoding fails and last two characters are not '=', add another '=' character at the end, then try again
4. If decoding fails and last two characters are '=', replace both '=' with a single 'A' character, then try again
5. Continue testing until PowerShell succeeds in decoding the hash without the error 'Invalid length for a Base-64 char array or string'

## Validation
PowerShell command [System.Text.Encoding]::ascii.getstring( [System.Convert]::FromBase64String("DEVICE HASH")) succeeds without error 'Invalid length for a Base-64 char array or string'

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
