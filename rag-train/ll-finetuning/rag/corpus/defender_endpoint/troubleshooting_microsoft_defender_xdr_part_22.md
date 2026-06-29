# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate user identities using Insights in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft 365 with Microsoft Defender XDR and Microsoft Sentinel
- **Configuration:** Microsoft Sentinel UEBA enabled; data sources: Syslog, SecurityEvent, AuditLogs, SigninLogs, OfficeActivity, BehaviorAnalytics, Heartbeat, CommonSecurityLog

## Symptoms
- Need to investigate user identities for security signals such as sign-in activity, group changes, and anomalous behavior

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Insights section in the user investigation page
2. Review entity insights automatically highlighted by Microsoft security researchers
3. Select the link accompanying any insight to open the Advanced hunting page with the underlying query and raw results
4. Modify the query or drill down into the results to expand the investigation

## Validation
1. Navigate to the Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to 'Incidents & alerts' > 'Incidents' and select an incident involving a user identity.
3. In the incident page, select the 'User' tab to view the user investigation page.
4. Verify that the 'Insights' section is displayed and contains entity insights (e.g., 'Unusual sign-in activity', 'Group membership changes', 'Anomalous behavior').
5. Click on the link accompanying any insight (e.g., 'View in advanced hunting').
6. Confirm that the Advanced hunting page opens with the underlying query pre-populated and raw results displayed.
7. Optionally, modify the query (e.g., add filters) and run it to ensure the investigation can be expanded.

## Rollback
1. If the Insights section does not appear or insights are missing, verify that Microsoft Defender XDR is properly licensed and the user has appropriate permissions (e.g., Security Reader, Security Administrator).
2. If the Advanced hunting link fails to open, check that the user has permissions to run Advanced hunting queries (e.g., 'Advanced Hunting' role).
3. If the query results are empty or incorrect, review the underlying KQL query for errors and ensure the data sources (e.g., AuditLogs, SigninLogs) are correctly configured and streaming data.
4. If the issue persists, revert to the previous investigation method (e.g., manual log searches in Microsoft Sentinel or Azure AD sign-in logs) and contact Microsoft support for further assistance.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
