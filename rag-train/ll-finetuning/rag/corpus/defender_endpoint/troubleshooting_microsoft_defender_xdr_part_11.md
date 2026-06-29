# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How do I search for specific alerts by title or ID in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Search bar

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enter the search term in the search bar.
2. You can search for alerts based on the alert title or alert ID.

## Validation
1. Navigate to the Microsoft Defender XDR portal (https://security.microsoft.com).
2. In the search bar, enter the alert title or alert ID you expect to find.
3. Confirm that the alert appears in the search results with the correct title and ID.
4. Optionally, click on the alert to verify that the alert details page loads correctly and shows the expected information.

## Rollback
1. If the search does not return the expected alert, verify that the alert exists by checking the Alerts queue under Incidents & alerts > Alerts.
2. Ensure the search term is spelled correctly and matches the exact alert title or ID.
3. If the alert is missing, check for any filtering or scoping that might exclude it (e.g., time range, severity, status).
4. If the issue persists, clear the browser cache and retry the search.
5. As a last resort, use the Advanced Hunting feature to query for the alert using its ID in the AlertEvidence table.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
