# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How do I use the Hide alert feature for Defender for Endpoint alerts?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Hide alert feature

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose Hide alert from the alert details page.
2. Enter a meaningful name for your alert and a comment to describe the alert.
3. Select Save.

## Validation
1. Navigate to Microsoft Defender XDR (https://security.microsoft.com) and go to Incidents & alerts > Alerts. 2. Locate the alert that was hidden and verify it no longer appears in the default alert list. 3. Use the 'Hidden alerts' filter or view to confirm the alert is listed there with the custom name and comment provided. 4. Optionally, run the advanced hunting query: AlertInfo | where AlertId == "<AlertId>" | project AlertId, Title, Classification, Determination, ServiceSource, IsHidden, HiddenBy, HiddenReason | where IsHidden == true to confirm the alert is marked as hidden.

## Rollback
1. Navigate to Microsoft Defender XDR (https://security.microsoft.com) and go to Incidents & alerts > Alerts. 2. Apply the 'Hidden alerts' filter to locate the hidden alert. 3. Open the alert details page. 4. Select 'Unhide alert' to restore the alert to the active alert list. 5. Confirm the alert reappears in the default alert view without the custom name and comment.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
