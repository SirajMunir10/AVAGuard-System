# Troubleshooting: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Troubleshooting

## Scenario / Query
How do I assess the impact of a threat on my organization using the Overview section of a Threat Analytics report?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Threat Analytics reports available in Microsoft 365 Defender portal

## Symptoms
- Active alerts and incidents associated with a tracked threat
- Impacted assets with active alerts

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the Related incidents chart to see the number of active alerts and incidents, and their severity.
2. Review the Alerts over time chart to see the number of Active and Resolved alerts over time.
3. Review the Impacted assets chart to see the number of distinct assets with at least one active alert.
4. Review both org- and user-level policies for overrides that cause the delivery of threat emails.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Threat Analytics under the Endpoints section.
3. Select the specific threat report you are investigating.
4. In the Overview section, verify the 'Related incidents' chart displays the expected number of active alerts and incidents with correct severity levels.
5. Check the 'Alerts over time' chart to confirm it shows both Active and Resolved alerts over the relevant time period.
6. Review the 'Impacted assets' chart to ensure it lists the correct number of distinct assets with at least one active alert.
7. Confirm that org- and user-level policy overrides for threat email delivery are correctly reflected in the report.

## Rollback
1. If the remediation steps caused issues, revert any changes made to org- or user-level email delivery policies by restoring previous policy configurations.
2. For policy overrides, use Exchange admin center or PowerShell to remove or disable any newly created transport rules or anti-spam policies that were added.
3. If alerts or incidents were dismissed or resolved incorrectly, reopen them via the Microsoft 365 Defender portal by selecting the alert/incident and choosing 'Reopen'.
4. If impacted assets were incorrectly excluded, remove any exclusions added to Defender for Endpoint device groups or indicators.
5. Verify that the Threat Analytics report Overview section returns to its pre-remediation state by re-checking the charts and policy settings.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
