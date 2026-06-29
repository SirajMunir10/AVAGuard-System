# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify the source of a Microsoft Defender XDR alert based on its prepended GUID prefix?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Unified alerts queue, unified alerts page, unified investigation, unified incident

## Symptoms
- Alerts with prepended characters in the alert GUID

## Error Codes
N/A

## Root Causes
1. Alerts from different Microsoft security solutions have specific prepended GUID prefixes to indicate their source

## Remediation Steps
1. Identify the prepended character on the alert GUID
2. Use the mapping table: ra{GUID} for alerts from ThreatExperts, ta{GUID} for alerts from custom detections, fa{GUID} for Microsoft Defender for Office 365, da{GUID} for Microsoft Defender for Endpoint, ed{GUID} for alerts from custom detections, aa{GUID} for Microsoft Defender for Identity, ri{GUID} for alerts from XDR detection engine, ca{GUID} for Microsoft Defender for Cloud Apps, ma{GUID} for alerts from App Governance detections and policies, rm{GUID} for alerts from XDR detection engine

## Validation
1. Open the Microsoft Defender XDR portal (https://security.microsoft.com).
2. Navigate to Incidents & alerts > Alerts.
3. Locate an alert with a prepended character in its GUID (e.g., ra{GUID}, ta{GUID}, fa{GUID}, da{GUID}, ed{GUID}, aa{GUID}, ri{GUID}, ca{GUID}, ma{GUID}, rm{GUID}).
4. Confirm the prepended prefix matches the expected source mapping from the remediation steps (e.g., 'ra' for ThreatExperts, 'ta' for custom detections, etc.).
5. Verify the alert details page shows the correct source product (e.g., Microsoft Defender for Endpoint for 'da' prefix).
6. Repeat for at least one alert from each source type present in your environment to ensure the mapping is consistent.

## Rollback
1. If the prepended prefix does not match the expected source, note the actual prefix and consult the Microsoft documentation at https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts for any updates to the mapping table.
2. If the alert source is misidentified, do not change the alert GUID; instead, use the alert's metadata (e.g., 'Detection source' field) to determine the true origin.
3. If the remediation steps caused confusion, revert to the default alert view by clearing any filters applied to the alerts queue.
4. If the issue persists, open a support ticket with Microsoft providing the alert GUID and the observed prefix for further investigation.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
