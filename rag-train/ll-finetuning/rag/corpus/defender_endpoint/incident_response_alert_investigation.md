# Incident Response: Alert Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Alert Investigation
**Incident Type:** Incident Response

## Scenario / Query
How to classify and resolve an alert in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Mark the alert's status as Resolved
2. Classify the alert as either False alert or True alert
3. If classified as a true alert, select a determination
4. If experiencing a false alert with a line-of-business application, create a suppression rule to avoid this type of alert in the future

## Validation
1. In Microsoft Defender for Endpoint, navigate to the Alerts queue and locate the alert. 2. Confirm the alert status shows 'Resolved'. 3. Verify the classification (False alert or True alert) is set as intended. 4. If classified as True alert, confirm the determination (e.g., 'Malware', 'Phishing', 'Unwanted software') is selected. 5. If a suppression rule was created for a false alert, go to Settings > Endpoints > Rules > Suppression rules and verify the rule is present and enabled.

## Rollback
1. In Microsoft Defender for Endpoint, navigate to the Alerts queue and locate the alert. 2. Change the alert status back to 'In progress' or 'New' as needed. 3. Clear the classification by selecting 'Not classified' or reclassify as appropriate. 4. If a determination was set, remove or change it. 5. If a suppression rule was created, go to Settings > Endpoints > Rules > Suppression rules, find the rule, and delete or disable it.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/investigate-alerts>
