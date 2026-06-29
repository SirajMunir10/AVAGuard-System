# Implementation: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Implementation

## Scenario / Query
How to view alerts from different Microsoft security solutions in the Microsoft Defender portal?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Alerts from Defender for Endpoint, Defender for Office 365, Microsoft Sentinel, Defender for Cloud, Defender for Identity, Defender for Cloud Apps, Defender XDR, App Governance, Microsoft Entra ID Protection, Microsoft Data Loss Prevention

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to Incidents & alerts > Alerts on the quick launch of the Microsoft Defender portal.
2. View alerts for each incident on the incidents queue or on each individual incident's page on the Alerts tab.

## Validation
1. Open the Microsoft Defender portal (https://security.microsoft.com).
2. In the quick launch, select 'Incidents & alerts' > 'Alerts'.
3. Confirm that the Alerts queue displays alerts from the following sources: Defender for Endpoint, Defender for Office 365, Microsoft Sentinel, Defender for Cloud, Defender for Identity, Defender for Cloud Apps, Defender XDR, App Governance, Microsoft Entra ID Protection, and Microsoft Data Loss Prevention.
4. Select any incident from the Incidents queue and navigate to its 'Alerts' tab. Verify that the alerts listed correspond to the incident and include alerts from multiple security solutions as expected.
5. Optionally, use filters (e.g., by service source) to confirm that alerts from each integrated solution appear correctly.

## Rollback
1. If the Alerts page does not display expected alerts, verify that the relevant Microsoft security solutions are properly onboarded and licensed in the tenant.
2. Ensure that the user account has the necessary permissions (e.g., 'View alerts' role in Microsoft Defender XDR).
3. Check service health in the Microsoft 365 admin center for any ongoing incidents affecting alert ingestion.
4. If alerts from a specific solution are missing, review that solution's integration settings (e.g., for Microsoft Sentinel, confirm the data connector is active; for Defender for Cloud Apps, verify the app connector is configured).
5. If the issue persists, refer to the official troubleshooting guide at https://learn.microsoft.com/en-us/defender-xdr/troubleshoot-alerts.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
