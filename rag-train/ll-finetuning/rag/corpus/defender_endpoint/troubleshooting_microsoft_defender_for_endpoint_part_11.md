# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'The start type of the service is unexpected' issue?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The start type of the service is unexpected. Service name: %1, actual start type: %2, expected start type: %3

## Error Codes
N/A

## Root Causes
1. Changes in start type

## Remediation Steps
1. Identify what is causing changes in start type
2. Fix mentioned service start type

## Validation
1. Open an elevated Command Prompt and run 'sc query <service_name>' to confirm the service start type matches the expected value (e.g., 'AUTO_START', 'DEMAND_START', 'DISABLED').
2. Verify the service is running by checking its status in the Services console (services.msc) or via 'sc query <service_name>'.
3. Review the Microsoft Defender for Endpoint onboarding health status in the Microsoft 365 Defender portal (https://security.microsoft.com) under Endpoints > Onboarding to ensure the device shows as 'Active' or 'Onboarded'.
4. Check the most recent MDE onboarding logs at 'C:\ProgramData\Microsoft\Windows Defender\Platform\<version>\MpCmdRun.log' for any remaining 'unexpected start type' errors.

## Rollback
1. If the service start type was changed incorrectly, revert it to the original start type using 'sc config <service_name> start=<original_start_type>' (e.g., 'sc config Sense start=auto').
2. Restart the service with 'sc start <service_name>' or 'net start <service_name>'.
3. If the device becomes unresponsive or loses protection, reboot the device to restore previous service states.
4. Re-run the MDE onboarding script (e.g., 'WindowsDefenderATPOnboardingScript.cmd') from the Microsoft 365 Defender portal to reapply the correct service configurations.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
