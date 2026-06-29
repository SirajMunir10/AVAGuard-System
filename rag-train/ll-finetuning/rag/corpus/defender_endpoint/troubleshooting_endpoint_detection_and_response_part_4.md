# Troubleshooting: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Troubleshooting

## Scenario / Query
Why does deep analysis file submission fail or timeout in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Sample collection requires an online Windows 10, Windows 11, or Windows Server 2012 R2+ device

## Symptoms
- Sample collection time varies depending on device availability.
- Collection fails and operation aborts after a 3-hour timeout.

## Error Codes
N/A

## Root Causes
1. No online Windows 10 device (or Windows 11 or Windows Server 2012 R2+) reporting at that time.

## Remediation Steps
1. Ensure at least one supported Windows device (Windows 10, Windows 11, or Windows Server 2012 R2+) is online and reporting.
2. Re-submit the file for deep analysis to get fresh data on the file.

## Validation
1. Check that at least one supported Windows device (Windows 10, Windows 11, or Windows Server 2012 R2+) is online and reporting to Microsoft Defender for Endpoint. Use the Microsoft 365 Defender portal: go to Devices list, filter by OS (Windows 10/11/Server 2012 R2+), and verify the 'Last seen' timestamp is within the last few minutes. 2. Re-submit the file for deep analysis via the Microsoft 365 Defender portal: navigate to the file's page, click 'Deep analysis', and confirm the submission starts without immediate timeout. 3. Monitor the analysis status in the Action center; verify it completes within the expected time (typically under 3 hours).

## Rollback
1. If the re-submission fails again, check the device availability again using the Devices list in Microsoft 365 Defender; ensure at least one supported Windows device is online. 2. If no device is available, wait for a supported device to come online and retry the submission. 3. If the issue persists, review the device's reporting status in the Microsoft 365 Defender portal under Settings > Endpoints > Onboarding; ensure the device is properly onboarded and reporting. 4. As a last resort, contact Microsoft support for further investigation.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
