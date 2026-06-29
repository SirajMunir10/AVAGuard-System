# Implementation: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Implementation

## Scenario / Query
How do retention policies for Exchange display expiry date notifications to users?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Retention policies for Exchange

## Symptoms
- Users see a retention policy name and expiry date at the top of email messages
- Notification is not displayed if the retention policy is retain-only (does not delete items)
- If a retention label is applied, the label name and expiry date replace the policy name and date

## Error Codes
N/A

## Root Causes
1. Retention policies for Exchange have a user presence feature that shows the policy with the shortest expiry date
2. Retain-only policies do not trigger deletion notifications
3. Retention labels override policy notifications when applied to an email

## Remediation Steps
1. Verify that the retention policy is configured to delete items (not retain-only) to show the notification
2. Check if a retention label is applied to the email, as it will replace the policy notification

## Validation
Confirm that users see the retention policy name and expiry date at the top of email messages for policies that delete items.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/retention-policies-exchange>
