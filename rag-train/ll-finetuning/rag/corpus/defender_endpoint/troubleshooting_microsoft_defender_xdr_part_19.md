# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How do I use the custom time range picker to focus my investigation on a specific timeframe in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose a timeframe to focus your investigation on the last 24 hours, the last 3 days, and so on.
2. Or choose a specific timeframe by selecting Custom range.

## Validation
1. Open the Microsoft Defender XDR portal (https://security.microsoft.com).
2. Navigate to Incidents & alerts > Incidents and select any incident.
3. In the incident timeline, verify that the default time range (e.g., Last 24 hours) is displayed and functional.
4. Click the time range picker and select 'Custom range'.
5. Set a specific start and end time (e.g., 2025-03-01 00:00 to 2025-03-02 23:59) and apply.
6. Confirm that the incident timeline and related alerts/events are filtered to show only data within that custom timeframe.
7. Switch back to a preset range (e.g., Last 3 days) and verify the timeline updates accordingly.

## Rollback
1. In the Microsoft Defender XDR portal, navigate to Incidents & alerts > Incidents.
2. Open the incident you were investigating.
3. Click the time range picker and select a preset range such as 'Last 24 hours' or 'Last 3 days' to revert from the custom range.
4. Verify that the timeline and related data now reflect the preset range.
5. If the custom range caused display issues, clear browser cache and refresh the portal.
6. If problems persist, sign out and sign back in to the portal to reset session state.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
