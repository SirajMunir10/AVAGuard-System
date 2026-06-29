# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'Failed to read the offboarding parameters' error?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Failed to read the offboarding parameters
- Error type: %1, Error code: %2, Description: %3

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the device has Internet access
2. Run the entire offboarding process again

## Validation
1. Verify the device can reach the required Microsoft Defender for Endpoint URLs by running: Invoke-WebRequest -Uri 'https://<your-workspace>.com' -UseBasicParsing (replace with actual endpoint). 2. Confirm the offboarding script was downloaded completely and is not corrupted by checking its hash against the published value. 3. Re-run the offboarding script and observe the output for any error messages. 4. Check the device's Microsoft Defender for Endpoint agent status in the Microsoft 365 Defender portal to ensure it shows as 'Offboarded'.

## Rollback
1. If the device still shows as onboarded or the error persists, re-run the onboarding script to restore the device to a managed state. 2. Verify network connectivity to Microsoft Defender for Endpoint services using the same URL test as in validation. 3. If the offboarding script fails repeatedly, contact Microsoft Support with the exact error code and description from the error message.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
