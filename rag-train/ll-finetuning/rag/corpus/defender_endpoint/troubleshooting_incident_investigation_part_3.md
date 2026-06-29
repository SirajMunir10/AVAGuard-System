# Troubleshooting: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I start investigating an incident in Microsoft Defender XDR?

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
1. Select the incident row, but not selecting the incident name to open a summary pane with key information including priority assessment, factors influencing priority score, incident details, recommended actions, and related threats.
2. Use the up and down arrows at the top of the pane to navigate to the previous or next incident in the incident queue.
3. Select 'Open incident page' to access the main page with full attack story information and tabs for alerts, devices, users, investigations, and evidence.
4. Alternatively, select the incident name from the incident queue to open the main page directly.

## Validation
1. In Microsoft Defender XDR, navigate to Incidents & alerts > Incidents. 2. Select an incident row (not the name) and confirm a summary pane opens displaying priority assessment, factors influencing priority score, incident details, recommended actions, and related threats. 3. Use the up/down arrows at the top of the pane and verify navigation to previous/next incidents in the queue. 4. Select 'Open incident page' and confirm the main page loads with full attack story, tabs for alerts, devices, users, investigations, and evidence. 5. Alternatively, select an incident name directly from the queue and confirm the main page opens correctly.

## Rollback
1. Close any open incident summary pane or main incident page. 2. Return to the incident queue by selecting 'Incidents' in the left navigation. 3. If the incident queue is not visible, refresh the browser or navigate to Microsoft Defender XDR > Incidents & alerts > Incidents. 4. No configuration changes were made; no further rollback actions are required.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
