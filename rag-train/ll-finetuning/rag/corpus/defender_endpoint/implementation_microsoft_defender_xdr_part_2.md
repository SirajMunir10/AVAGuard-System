# Implementation: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Implementation

## Scenario / Query
What are the built-in alert tuning rules in Microsoft Defender XDR and how do they work?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Built-in alert tuning rules

## Symptoms
- Reporting noise from common benign activity

## Error Codes
N/A

## Root Causes
1. Common benign activity triggering alerts

## Remediation Steps
1. Use built-in alert tuning rules that suppress alerts from common benign activity without affecting Automated Investigation and Response (AIR) investigations and email notifications.
2. If the AIR investigation detects malicious or suspicious activity, the new alert is reactivated.

## Validation
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to Settings > Endpoints > Rules > Alert tuning.
3. Confirm that the built-in alert tuning rules are listed and enabled.
4. Verify that alerts from common benign activities (e.g., known safe processes, legitimate admin tools) are no longer appearing in the incidents queue.
5. Check that Automated Investigation and Response (AIR) investigations still trigger for malicious or suspicious activity, and that any suppressed alert is reactivated if AIR detects a threat.
6. Optionally, use the Advanced Hunting query: AlertInfo | where AlertId in (list of previously noisy alert IDs) | project Timestamp, AlertTitle, Severity, AlertId | order by Timestamp desc to confirm suppression.

## Rollback
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to Settings > Endpoints > Rules > Alert tuning.
3. Disable or delete the built-in alert tuning rule that was causing issues.
4. If the rule was customized, revert to the default built-in rule settings.
5. Monitor the alerts queue for the next 24–48 hours to ensure previously suppressed alerts are now appearing as expected.
6. If needed, re-enable any custom alert tuning rules that were disabled during the rollback.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
