# Implementation: Domain Management

**Domain:** Entra ID
**Subdomain:** Domain Management
**Incident Type:** Implementation

## Scenario / Query
How do I verify domain ownership and become the admin for a Microsoft 365 tenant?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Domain ownership verification required for admin takeover

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the admin center icon in the left navigation pane, or go to https://admin.cloud.microsoft in a browser.
2. You are redirected to the admin takeover wizard.
3. Select Next and verify that you own the domain you want to take over by adding a TXT record to your domain registrar. The wizard provides the TXT record to add, a link to your registrar's website, and a link to step-by-step instructions.
4. On the 'You're now the admin' page, select 'Go to the admin center'.

## Validation
You have the admin privileges required to manage the account in the admin center. For example, you can manage account users and groups, purchase new subscriptions and make user assignments, and manage the account domains.

## Rollback
If you want to remove your domain from this account so you can add it to another account, see 'Remove a domain from another account'.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/admin/misc/become-the-admin>
