# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
Devices are not appearing in the devices list within an hour after onboarding, even though deployment tools did not indicate an error.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Devices not appearing in the devices list after onboarding
- No error indicated by deployment tools

## Error Codes
N/A

## Root Causes
1. Error occurred with the Microsoft Defender for Endpoint agent
2. Diagnostic data service not enabled
3. Service not set to start
4. Device has no Internet connection
5. Microsoft Defender Antivirus disabled by a policy

## Remediation Steps
1. View agent onboarding errors in the device event log
2. Ensure the diagnostic data service is enabled
3. Ensure the service is set to start
4. Ensure the device has an Internet connection
5. Ensure that Microsoft Defender Antivirus is not disabled by a policy

## Validation
1. On the affected device, open Event Viewer and navigate to 'Applications and Services Logs/Microsoft/Windows/Sense/Operational'. Look for event IDs 1 (onboarding success) or 5 (onboarding error). If event ID 1 is present, onboarding succeeded. 2. Run 'services.msc' and verify that the 'Microsoft Defender Antivirus Service' (WinDefend) is running and not disabled. 3. Run 'services.msc' and verify that the 'Connected User Experiences and Telemetry' (DiagTrack) service is set to 'Automatic' and running. 4. From the device, run 'ping microsoft.com' to confirm internet connectivity. 5. In the Microsoft Defender portal, navigate to 'Devices list' and confirm the device appears within one hour.

## Rollback
1. If the diagnostic data service was enabled, set it back to its original state (e.g., 'Disabled' or 'Manual') via 'services.msc'. 2. If the service start type was changed, revert to the original setting (e.g., 'Manual' or 'Disabled') via 'services.msc'. 3. If Microsoft Defender Antivirus was re-enabled via policy, reapply the policy that disabled it. 4. If internet connectivity was restored by changing network settings, revert those changes. 5. If the device was re-onboarded, re-run the original onboarding script or package to restore the previous state.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
