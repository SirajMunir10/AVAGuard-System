# Troubleshooting: Microsoft Defender for Endpoint onboarding (29)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Defender for Endpoint offboarding error Event ID 29?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 29: Failed to read the offboarding parameters.

## Error Codes
- `29`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
1. On the affected device, open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > SENSE > Operational. Verify that no new Event ID 29 errors appear after remediation. 2. Run the command 'sc query sense' from an elevated command prompt and confirm the service status is 'RUNNING'. 3. Attempt to offboard the device using the official offboarding script or via Microsoft Defender portal; confirm the offboarding completes without error.

## Rollback
1. If the remediation fails, re-run the onboarding package for the device from the Microsoft Defender portal (Settings > Endpoints > Onboarding). 2. Restart the Microsoft Defender for Endpoint service by running 'net stop sense' then 'net start sense' from an elevated command prompt. 3. If issues persist, reinstall the Microsoft Defender for Endpoint agent by uninstalling the current version and deploying the latest onboarding package from the portal.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
