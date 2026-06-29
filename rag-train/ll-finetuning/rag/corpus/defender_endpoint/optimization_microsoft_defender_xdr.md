# Optimization: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Optimization

## Scenario / Query
How can a SOC analyst tune alerts to automatically hide or resolve low-priority alerts in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Alert tuning rules

## Symptoms
- High volume of low-priority alerts requiring manual triage
- Alert queue noise from expected organizational behavior

## Error Codes
N/A

## Root Causes
1. Manual triage of alerts that could be automated based on known benign activity

## Remediation Steps
1. Create custom alert tuning rules with conditions based on evidence types such as files, processes, scheduled tasks, and other evidence types that trigger alerts.
2. Apply the alert tuning rule to the selected alert or any alert type that meets the defined conditions.
3. Choose one of the following actions: Hide alert (suppresses the alert and prevents incident creation; only applicable for Defender for Endpoint alerts), Resolve alert (automatically resolves the alert and related incidents), or Set as behavior (converts matching signals into behaviors; not supported for Defender for Cloud or Microsoft Defender for Office 365 alerts).

## Validation
1. Navigate to Microsoft Defender XDR > Incidents & alerts > Alerts. 2. Filter the alert queue by the conditions defined in the tuning rule (e.g., evidence type, severity, title). 3. Confirm that alerts matching the rule conditions no longer appear in the queue (for 'Hide alert' action) or appear with status 'Resolved' (for 'Resolve alert' action). 4. Verify that no new incidents are created for hidden alerts. 5. For 'Set as behavior' action, confirm the signals appear in the 'Behaviors' tab instead of the Alerts queue.

## Rollback
1. Navigate to Microsoft Defender XDR > Settings > Endpoints > Rules > Alert tuning. 2. Locate the custom alert tuning rule created during remediation. 3. Select the rule and choose 'Delete rule' or 'Disable rule' to stop its application. 4. If the rule was applied to specific alerts, manually re-evaluate those alerts: for hidden alerts, they will reappear after rule deletion; for resolved alerts, change their status back to 'New' or 'In progress' as needed. 5. Monitor the alert queue to confirm that previously suppressed or resolved alerts are visible again.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
