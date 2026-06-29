# Troubleshooting: User Investigation

**Domain:** Defender for Endpoint
**Subdomain:** User Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate user activities in Microsoft Defender XDR timeline?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** User investigation timeline

## Symptoms
- Need to review user's impacted alerts
- Need to review Active Directory and Microsoft Entra activities
- Need to review cloud apps events
- Need to review device logon events
- Need to review directory services changes

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the user investigation timeline in Microsoft Defender XDR
2. Review user's impacted alerts
3. Review Active Directory and Microsoft Entra activities
4. Review cloud apps events
5. Review device logon events
6. Review directory services changes

## Validation
1. Navigate to https://security.microsoft.com and sign in with appropriate permissions. 2. Go to 'Incidents & alerts' > 'Incidents' and select an incident involving the user. 3. Click the 'User' tab to open the user investigation timeline. 4. Verify that the timeline displays the user's impacted alerts, Active Directory and Microsoft Entra activities, cloud apps events, device logon events, and directory services changes as described in the documentation. 5. Confirm that each section (Alerts, Active Directory, Microsoft Entra, Cloud apps, Device logon, Directory services) shows relevant events and no error messages appear.

## Rollback
1. If the user investigation timeline does not load or shows incorrect data, clear the browser cache and retry. 2. If the issue persists, verify that the user account has the required permissions (e.g., 'Security Reader' or 'Security Administrator') in Microsoft 365 Defender. 3. Ensure that the user's activities are within the data retention period and that the tenant has the necessary licenses (e.g., Microsoft 365 E5 or Defender for Endpoint Plan 2). 4. If the timeline is missing specific event types, check that the corresponding data sources (e.g., Microsoft Defender for Cloud Apps, Microsoft Entra ID) are properly connected and configured in the tenant. 5. If no events appear, verify that the user has actually performed activities in the monitored services during the selected time range.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
