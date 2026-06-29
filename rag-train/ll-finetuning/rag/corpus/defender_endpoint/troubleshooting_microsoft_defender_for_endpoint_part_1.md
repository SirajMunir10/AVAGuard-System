# Troubleshooting: Microsoft Defender for Endpoint (30)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender for Endpoint onboarding errors based on event codes?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Microsoft Defender for Endpoint service failed to connect to the server at variable
- Microsoft Defender for Endpoint service isn't onboarded and no onboarding parameters were found
- Microsoft Defender for Endpoint service failed to read the onboarding parameters
- Microsoft Defender for Endpoint service failed to change its start type
- Microsoft Defender for Endpoint service failed to persist the onboarding information
- Microsoft Defender for Endpoint can't start command channel with URL: variable
- Microsoft Defender for Endpoint service failed to change the Connected User Experiences and Telemetry service location
- Microsoft Defender for Endpoint service failed to reset health status in the registry
- Failed to enable Microsoft Defender for Endpoint mode in Windows Defender

## Error Codes
- `30`
- `32`
- `55`
- `63`
- `64`
- `68`
- `69`

## Root Causes
1. Device lacks Internet access
2. Onboarding parameters missing or not read
3. Service start type changed unexpectedly
4. Service failed to stop or start
5. Secure ETW autologger creation failed
6. External service start type or state issue

## Remediation Steps
1. Ensure the device has Internet access, then run the entire offboarding process again.
2. Contact support for error code 30.
3. Verify that the service start type is manual and reboot the device for error code 32.
4. Reboot the device for error code 55.
5. Identify what is causing changes in start type of mentioned service. If the exit code isn't 0, fix the start type manually to expected start type for error code 63.
6. Contact support if the event keeps re-appearing for error code 64.
7. Identify what is causing changes in start type. Fix mentioned service start type for error code 68.
8. Start the mentioned service. Contact support if the issue persists for error code 69.
9. Run the onboarding script again.
10. If the event happened during onboarding, reboot and re-attempt running the onboarding script.
11. If the event happened during offboarding, contact support.
12. If the problem persists, contact support.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
