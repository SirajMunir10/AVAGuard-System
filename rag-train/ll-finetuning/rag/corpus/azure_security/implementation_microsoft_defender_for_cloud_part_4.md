# Implementation: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Implementation

## Scenario / Query
How do I configure a custom email notification rule in Microsoft Defender for Cloud to alert specific security contacts when a high-severity vulnerability is detected on a critical VM?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with Microsoft Defender for Cloud enabled)
- **Configuration:** Defender for Cloud is enabled on the subscription; security contacts are defined in the Azure portal under Defender for Cloud > Environment Settings > Email notifications.

## Symptoms
- Security team does not receive email alerts for high-severity findings on critical resources.
- Only default subscription owner receives alerts.
- Custom notification rules are not visible in the Defender for Cloud dashboard.

## Error Codes
N/A

## Root Causes
1. Email notification rules have not been configured or are misconfigured in Defender for Cloud.
2. Security contact email addresses are missing or invalid.
3. The 'Send email notification for high severity alerts' toggle is disabled.

## Remediation Steps
1. 1. Navigate to Microsoft Defender for Cloud > Environment Settings > select the relevant subscription or management group.
2. 2. Under 'Email notifications', click 'Edit configuration'.
3. 3. Set 'Send email notification for high severity alerts' to 'On'.
4. 4. Under 'Additional email recipients', add the required email addresses (up to 20).
5. 5. Optionally, enable 'Send email notification for weekly digest' to provide a summary.
6. 6. Click 'Save' to apply the changes.

## Validation
After saving, trigger a test alert (e.g., by deploying a deliberately vulnerable VM) and verify that the configured recipients receive the email notification within 15 minutes.

## Rollback
Return to the same Email notifications configuration page, remove the added email addresses, and set 'Send email notification for high severity alerts' to 'Off'.

## References
- Microsoft Learn: 'Configure email notifications for Microsoft Defender for Cloud alerts' - https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications
