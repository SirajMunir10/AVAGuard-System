# Troubleshooting: Defender for Cloud

**Domain:** Defender for Endpoint
**Subdomain:** Defender for Cloud
**Incident Type:** Troubleshooting

## Scenario / Query
Why does remediating an agent-based security alert not automatically remediate the corresponding agentless scan alert?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Agent-based and agentless scanners both active in Defender for Cloud

## Symptoms
- After remediating an agent-based security alert, the agentless scan alert for the same issue remains unresolved

## Error Codes
N/A

## Root Causes
1. Remediating one alert (agent-based or agentless) does not remediate the other alert until the next scan is completed

## Remediation Steps
1. Review the agentless scan's results on the Security alerts page
2. Remediate the agentless scan alert separately after the next scan completes

## Validation
1. Navigate to Microsoft Defender for Cloud > Security alerts. 2. Filter by the specific alert name that was remediated via agent-based detection. 3. Confirm that the corresponding agentless scan alert for the same issue still appears with status 'Active'. 4. Wait for the next scheduled agentless scan to complete (typically within 24 hours). 5. After the scan, refresh the alerts page and verify that the agentless alert is now resolved or no longer present.

## Rollback
1. If the agentless alert remains unresolved after the next scan, manually remediate the agentless alert by following the remediation steps provided in the alert details. 2. If the agent-based alert was inadvertently dismissed or suppressed, re-enable the alert rule in Defender for Cloud > Security policy to ensure future detections are captured. 3. If the agent-based remediation caused unintended changes, restore the affected resource from a known good backup or configuration snapshot.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/managing-and-responding-alerts>
