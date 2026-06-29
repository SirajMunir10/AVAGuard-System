# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How do I search for alerts using a custom date and time range in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Date picker

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Custom range in the date picker.
2. Specify the start and end dates and times.

## Validation
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Alerts.
3. Click the date picker dropdown and select 'Custom range'.
4. Set a start date/time and an end date/time that covers a known alert period.
5. Click 'Apply' and confirm that alerts from that custom range are displayed.
6. Verify that alerts outside the custom range are not shown.

## Rollback
1. In the Alerts page, click the date picker dropdown again.
2. Select a predefined time range (e.g., 'Last 24 hours', 'Last 7 days', 'Last 30 days').
3. Click 'Apply' to revert to the default time filter.
4. Confirm that the alert list refreshes to show alerts based on the selected predefined range.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
