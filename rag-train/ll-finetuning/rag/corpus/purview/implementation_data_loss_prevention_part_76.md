# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure incident reports and alerts in a Microsoft Purview DLP policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with incident reports enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When a rule is matched, you can send an Alert email to your compliance officer (or any people you choose) with details of the event and you can view them in the Microsoft Purview Data Loss Prevention Alerts dashboard and in the Microsoft Defender XDR portal.
2. An alert includes information about the item that was matched, the actual content that matched the rule, and the name of the person who last modified the content.
3. In preview, admin alert emails include details such as: The alert severity, The time the alert occurred, The activity, The sensitive data that were detected, The alias of the user whose activity triggered the alert, The policy that was matched, The alert ID, The endpoint operation that was attempted if the Devices location is in the scope of the policy, The app that was being used, The device name, if the match occurred on an endpoint device.
4. DLP feeds incident information to other Microsoft Purview Information Protection services, like insider risk management. In order to get incident information to insider risk management, you must set the Incident reports severity level to High.
5. Alerts can be sent every time an activity matches a rule, which can be noisy. To help cut down on the noise, they can be aggregated based on number of matches or volume of items over a set period of time.
6. There are two types of alerts that can be configured in DLP policies: Single-event alerts and Aggregate-event alerts.
7. Single-event alerts are typically used in policies that monitor for highly sensitive events that occur in a low volume, like a single email with 10 or more customer credit card numbers being sent outside your organization.
8. In preview user based alert aggregation (preview) modifies the behavior of single event alerts.
9. Aggregate-event alerts are typically used in policies that monitor for events that occur in a higher volume over a period of time. For example, an aggregate alert can be triggered when 10 individual emails each with one customer credit card number is sent outside your org over 48 hours.
10. For rules with Alerts configured on SharePoint, or OneDrive workloads we only send one alert per file per rule. This is true, even if the same violation has been committed by multiple users.
11. When you select Use email incident reports to notify you when a policy match occurs you can choose to include: The name of the person who last modified the content.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. Select the DLP policy you configured. Verify that 'Incident reports' is set to 'High' or the desired severity level. 2. In the same policy, under 'Actions', confirm that 'Send alert to admin' is enabled and the correct recipients are listed. 3. Trigger a test DLP rule match (e.g., send an email containing a credit card number to an external recipient). 4. Check the Microsoft Purview Data Loss Prevention Alerts dashboard (https://compliance.microsoft.com/datalossprevention?view=alerts) for a new alert. 5. Verify the alert contains expected details: severity, time, activity, sensitive data type, user alias, policy name, alert ID, and if applicable, endpoint operation, app, and device name. 6. For aggregate alerts, confirm that the alert is generated only after the specified threshold (e.g., 10 matches in 48 hours) is met. 7. If insider risk management integration is required, confirm that incidents with severity 'High' appear in the insider risk management dashboard.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. Select the DLP policy you modified. 2. Under 'Incident reports', change the severity level to 'Low' or 'None' to disable incident generation. 3. Under 'Actions', disable 'Send alert to admin' by unchecking the option. 4. If user-based alert aggregation was enabled, disable it by setting 'Aggregate alerts' to 'None' or removing the aggregation rule. 5. Remove any custom email recipients from the alert notification list. 6. If the policy was newly created, delete the policy entirely. 7. Wait for propagation (up to 1 hour) and confirm no new alerts appear in the DLP Alerts dashboard for the policy.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
