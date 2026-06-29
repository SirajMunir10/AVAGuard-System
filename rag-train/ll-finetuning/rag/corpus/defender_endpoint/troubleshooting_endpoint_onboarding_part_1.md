# Troubleshooting: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot onboarding when deploying Microsoft Defender for Endpoint with Group Policy and devices do not appear in the Devices list after an hour?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Group Policy deployment of onboarding script

## Symptoms
- Devices do not appear in the Devices list after an hour of completing the onboarding process
- Group Policy console does not indicate if deployment has succeeded or not

## Error Codes
N/A

## Root Causes
1. Onboarding script may have failed on the devices
2. Additional errors may have occurred on the devices after script completion

## Remediation Steps
1. Check the output of the onboarding script on the devices
2. Refer to 'Troubleshoot onboarding when deploying with a script' for script output analysis
3. If script completes successfully, refer to 'Troubleshoot onboarding issues on the devices' for additional errors

## Validation
On each device, open an elevated command prompt and run: 'cd %ProgramData%\Microsoft\Windows Defender Advanced Threat Protection\OnboardingState' then 'type OnboardingState.txt' to confirm the state is 'Onboarded'. Also run: 'wevtutil qe Microsoft-Windows-Sense/Operational /c:10 /f:text' to check for Sense event logs showing successful connection. In the Microsoft 365 Defender portal, navigate to Devices list and verify the device appears within 1 hour.

## Rollback
On each device, open an elevated command prompt and run: 'cd %ProgramData%\Microsoft\Windows Defender Advanced Threat Protection\OnboardingState' then 'del OnboardingState.txt'. Delete the onboarding script from the Group Policy startup script location. In Group Policy Management Console, remove the onboarding script assignment from the relevant GPO. Force a Group Policy update on affected devices: 'gpupdate /force'. Reboot devices to clear any cached state.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
