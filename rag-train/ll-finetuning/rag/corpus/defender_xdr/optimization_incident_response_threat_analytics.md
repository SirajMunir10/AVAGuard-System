# Optimization: Incident Response & Threat Analytics

**Domain:** Defender XDR
**Subdomain:** Incident Response & Threat Analytics
**Incident Type:** Optimization

## Scenario / Query
A security operations team notices that Microsoft Defender XDR incident correlation is missing alerts from Microsoft Defender for Cloud Apps. How can they verify and enable the required data connector to ensure all cloud app signals are included in incident correlation?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender XDR and Defender for Cloud Apps licensed
- **Configuration:** Data connectors between Microsoft Defender XDR and Microsoft Defender for Cloud Apps must be enabled to allow cross-domain incident correlation.

## Symptoms
- Incidents in Microsoft Defender XDR do not include alerts from Defender for Cloud Apps.
- Defender for Cloud Apps alerts appear only in the Defender for Cloud Apps portal, not in the unified incidents queue.
- The 'Data connectors' page in Microsoft Defender XDR shows the Defender for Cloud Apps connector as 'Not enabled' or 'Failed'.

## Error Codes
N/A

## Root Causes
1. The data connector between Microsoft Defender XDR and Microsoft Defender for Cloud Apps has not been enabled or has been disabled.
2. Required permissions or licensing for cross-product data sharing are missing.

## Remediation Steps
1. Sign in to the Microsoft Defender portal (https://security.microsoft.com) as a Global Administrator or Security Administrator.
2. Navigate to Settings > Microsoft Defender XDR > Data connectors.
3. Locate the 'Microsoft Defender for Cloud Apps' connector and select 'Enable'.
4. If prompted, review and accept the data sharing terms.
5. Wait up to 24 hours for historical data to synchronize and for new alerts to appear in incident correlation.
6. Verify by creating a test alert in Defender for Cloud Apps (e.g., by triggering a risky sign-in) and confirming it appears as an alert in the Microsoft Defender XDR incidents queue.

## Validation
After enabling the connector, navigate to Incidents & alerts > Incidents in the Microsoft Defender portal. Confirm that alerts originating from Defender for Cloud Apps are now included in incident correlation. You can filter by 'Service source: Microsoft Defender for Cloud Apps' to verify.

## Rollback
To disable the connector, navigate again to Settings > Microsoft Defender XDR > Data connectors, select the Microsoft Defender for Cloud Apps connector, and choose 'Disable'. Note that disabling will stop new alert ingestion but will not remove already correlated incidents.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/enable-microsoft-defender-for-cloud-apps-connector>
