# Troubleshooting: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot devices not reporting correctly in Defender for Endpoint by checking the Windows diagnostic data service?

## Environment Context
- **Tenant Type:** Windows 10 build 1809 and later
- **Configuration:** Defender for Endpoint EDR service

## Symptoms
- Devices aren't reporting correctly

## Error Codes
N/A

## Root Causes
1. Windows diagnostic data service might have been disabled by other programs or user configuration changes

## Remediation Steps
1. Check that the Windows diagnostic data service is set to automatically start when Windows starts
2. Check that the service is currently running (and start it if it isn't)

## Validation
1. Open Services console (services.msc).
2. Locate 'Connected User Experiences and Telemetry' service.
3. Verify 'Startup type' is 'Automatic'.
4. Verify 'Status' is 'Running'.
5. If not running, right-click and select 'Start'.
6. Run 'sc query DiagTrack' from an elevated command prompt and confirm STATE is 'RUNNING'.
7. Check that the service start type is 'AUTO_START' using 'sc qc DiagTrack'.

## Rollback
1. If the service was changed to 'Automatic' but causes issues, revert to previous startup type via Services console or 'sc config DiagTrack start= <previous_value>'.
2. If the service was started and causes problems, stop it via Services console or 'sc stop DiagTrack'.
3. If the service was disabled and re-enabling causes performance or policy conflicts, set it back to 'Disabled' using 'sc config DiagTrack start= disabled'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
