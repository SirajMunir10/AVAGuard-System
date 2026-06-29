# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure user notifications and policy tips for DLP policies in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with user notification and policy tip settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure user notification emails and in-context policy tip popups when a user attempts an activity on a sensitive item that meets rule conditions.
2. Note that an Alert email, Incident Report email, and User Notification will only be sent once per document.
3. Notification emails are sent unprotected.
4. Email notifications are only supported for the Microsoft 365 services as specified: Supported for Exchange, SharePoint, OneDrive for work or school; Not supported for Devices, Fabric and Power-BI, On-premises repositories, Microsoft 365 Copilot (preview), Managed cloud apps.
5. For unmanaged cloud apps (browser and network) in preview, enable email notifications to notify end users via email when their activity is blocked.
6. Configure email notifications for the person who performed the blocked activity and additional recipients such as admins or compliance officers.
7. Email notifications are batched: first policy match sends an immediate notification; additional matches within a rolling 10-minute window are batched into a single email listing all blocked activities; after 10 minutes with no further matches, the window resets.

## Validation
1. Create a DLP policy with user notification and policy tip settings enabled for Exchange, SharePoint, and OneDrive. 2. Trigger a policy match by attempting to share a sensitive document via email or a SharePoint link. 3. Verify that the user receives a policy tip popup in the Outlook web app or SharePoint/OneDrive interface. 4. Check that an email notification is sent to the user and any additional recipients within the first 10-minute window. 5. Confirm that subsequent matches within the same 10-minute window are batched into a single email listing all blocked activities. 6. After 10 minutes with no further matches, verify that the window resets and a new immediate notification is sent for the next match.

## Rollback
1. Disable user notification and policy tip settings in the DLP policy by editing the policy and unchecking 'Notify users with a policy tip' and 'Send notification emails to affected users'. 2. Remove any additional recipients configured for email notifications. 3. Save the policy changes and allow up to 1 hour for propagation. 4. Verify that no policy tips or notification emails are sent upon subsequent policy matches.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
