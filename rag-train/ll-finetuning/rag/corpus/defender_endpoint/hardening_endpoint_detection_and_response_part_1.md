# Hardening: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Hardening

## Scenario / Query
How do I allow or block a file by adding an indicator hash in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Indicators for file hashes

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Add an indicator hash for a file to raise an alert and block the file whenever a device in your organization attempts to run it.
2. To stop blocking a file, remove the indicator via the Edit Indicator action on the file's profile page.
3. Alternatively, edit indicators from the Settings page, under Rules > Indicators.

## Validation
Files automatically blocked by an indicator don't show up in the file's Action center, but the alerts are still visible in the Alerts queue.

## Rollback
Remove the indicator to stop blocking the file.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
