# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How do I filter the timeline by type, alert severity, activity type, app, location, or protocol in Microsoft Defender XDR?

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
1. Use the timeline filters to narrow results by Type (alerts and/or user's related activities), Alert severity, Activity type, App, Location, or Protocol.
2. Each filter depends on the others, and the options in each filter only contain data that's relevant for the specific user.

## Validation
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to 'Incidents & alerts' > 'Incidents' and select an incident.
3. Click the 'User' tab to open the user investigation page.
4. In the timeline section, verify that the 'Type' filter is present and functional: select 'Alerts' and confirm only alert-related events are shown; then select 'User's related activities' and confirm only activity events appear.
5. Test the 'Alert severity' filter: choose a severity (e.g., High) and verify that only alerts with that severity are displayed.
6. Test the 'Activity type' filter: select an activity type (e.g., Log in) and confirm the timeline updates accordingly.
7. Test the 'App' filter: pick an application (e.g., Office 365) and verify the timeline shows only events from that app.
8. Test the 'Location' filter: select a location (e.g., a specific IP or country) and confirm filtering works.
9. Test the 'Protocol' filter: choose a protocol (e.g., HTTP) and verify the timeline is filtered.
10. Ensure that when multiple filters are applied, the options in each filter only contain data relevant to the specific user and the other active filters.

## Rollback
1. Clear all applied filters by clicking the 'Clear filters' button (or resetting each filter to its default 'All' state).
2. If the timeline does not return to showing all events, refresh the page or navigate away and back to the user investigation page.
3. If filters become unresponsive or cause errors, close the browser tab and reopen the Microsoft Defender XDR portal, then re-navigate to the incident and user investigation.
4. If the issue persists, clear browser cache and cookies, then retry.
5. As a last resort, use a different browser or an InPrivate/Incognito session to access the portal.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
