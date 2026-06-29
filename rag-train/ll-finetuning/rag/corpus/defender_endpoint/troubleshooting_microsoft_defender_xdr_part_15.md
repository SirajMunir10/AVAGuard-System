# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate a user's risk and activity using the Overview tab in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender for Identity, Microsoft Purview Insider Risk Management, Microsoft Sentinel UEBA

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the user's page in Microsoft Defender XDR.
2. Select the Overview tab to view a high-level snapshot.
3. Review the Entity details panel for identity information, including Microsoft Entra ID attributes, contact information, protection and user threat indications, first seen and last seen timestamps, number of devices signed into, linked user accounts, devices, and group memberships.
4. Check the Incidents and alerts section for related alerts and incidents grouped by severity.
5. If Microsoft Defender for Identity is enabled, review Active Directory account control flags (e.g., password-never-expires or account lock status) and the organization tree showing the identity's position in the reporting hierarchy.
6. If Microsoft Purview Insider Risk Management is enabled (Preview), select the insider risk severity to see risk insights about the user.
7. If Microsoft Sentinel UEBA is enabled (Preview), review the user's top three UEBA anomalies from the last 30 days and use links to launch pre-built advanced hunting queries or view all anomalous behaviors on the Microsoft Sentinel events tab.

## Validation
1. Navigate to the user's page in Microsoft Defender XDR and select the Overview tab. 2. Confirm the Entity details panel displays identity information including Microsoft Entra ID attributes, contact info, protection and user threat indications, first seen and last seen timestamps, number of devices signed into, linked user accounts, devices, and group memberships. 3. Verify the Incidents and alerts section shows related alerts and incidents grouped by severity. 4. If Microsoft Defender for Identity is enabled, confirm Active Directory account control flags (e.g., password-never-expires or account lock status) and the organization tree are visible. 5. If Microsoft Purview Insider Risk Management is enabled (Preview), select the insider risk severity and verify risk insights appear. 6. If Microsoft Sentinel UEBA is enabled (Preview), confirm the user's top three UEBA anomalies from the last 30 days are displayed and that links to pre-built advanced hunting queries or the Microsoft Sentinel events tab are functional.

## Rollback
1. If the Overview tab does not load or shows incorrect data, clear the browser cache and retry navigation to the user's page. 2. If Entity details are missing, verify the user's Microsoft Entra ID synchronization and licensing for Microsoft Defender for Identity, Microsoft Purview Insider Risk Management, or Microsoft Sentinel UEBA as applicable. 3. If Incidents and alerts are not grouped correctly, refresh the page or check that the user has associated alerts in Microsoft Defender XDR. 4. If Active Directory account control flags or organization tree are missing, confirm Microsoft Defender for Identity is properly configured and the user is synchronized from on-premises Active Directory. 5. If insider risk severity does not display, ensure Microsoft Purview Insider Risk Management is enabled and the user has risk indicators. 6. If UEBA anomalies are absent, verify Microsoft Sentinel UEBA is enabled and that the user has sufficient activity data in the last 30 days.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
