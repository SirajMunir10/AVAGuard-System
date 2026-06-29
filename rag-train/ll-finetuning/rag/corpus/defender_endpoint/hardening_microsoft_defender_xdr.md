# Hardening: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Hardening

## Scenario / Query
How do I create an alert tuning rule from an alert details page in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Alert tuning rule creation

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose from Hide alert, Resolve alert, or Set as behavior.
2. Enter a meaningful name for your alert and a comment to describe the alert.
3. Select Save.
4. After creating your alert tuning rule from an alert details page, in the Successful rule creation page that appears, add any of the alert-related IOCs as indicators to an allow list to prevent them from being blocked in the future.
5. For example: Add a file to the Select evidence (IOC) to allow list. By default, the file that triggered the alert is already selected.
6. Define a scope for the Select scope to apply to value. By default, the scope that applies to your alert is selected.
7. Select Save to add the file to an allow list and prevent it from being blocked.

## Validation
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to 'Incidents & alerts' > 'Alerts'.
3. Locate the alert for which the tuning rule was created.
4. Verify that the alert now shows the status 'Resolved' or 'Hidden' or 'Set as behavior' as per the rule.
5. Go to 'Settings' > 'Endpoints' > 'Rules' > 'Alert tuning'.
6. Confirm the new rule appears in the list with the name and comment you provided.
7. If IOCs were added to an allow list, go to 'Settings' > 'Endpoints' > 'Indicators' and verify the file or IOC is listed with action 'Allow'.

## Rollback
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to 'Settings' > 'Endpoints' > 'Rules' > 'Alert tuning'.
3. Locate the newly created alert tuning rule.
4. Select the rule and click 'Delete' to remove it.
5. If IOCs were added to an allow list, go to 'Settings' > 'Endpoints' > 'Indicators'.
6. Find the indicator(s) added during the remediation and delete them.
7. Confirm the alert returns to its original state (e.g., active) by checking the alert details page.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
