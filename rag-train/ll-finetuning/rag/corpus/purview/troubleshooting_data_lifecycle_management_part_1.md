# Troubleshooting: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Troubleshooting

## Scenario / Query
Why do users not see the expiry date notification for a retention policy in Exchange?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Retention policies for Exchange

## Symptoms
- No retention policy name or expiry date displayed at the top of email messages

## Error Codes
N/A

## Root Causes
1. The retention policy is configured to retain items only (retain-only) and does not delete items
2. A retention label is applied to the email, which replaces the policy notification

## Remediation Steps
1. Ensure the retention policy is set to delete items to enable the notification
2. Check if a retention label is applied; if so, the label's name and expiry date will be shown instead

## Validation
Verify that the retention policy has a deletion action configured and no retention label is overriding the notification.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/retention-policies-exchange>
