# Implementation: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Implementation

## Scenario / Query
How to send an email notice to a user from an insider risk management case in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Insider Risk Management solution enabled, admin account with appropriate permissions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal with credentials for an admin account in your Microsoft 365 organization.
2. Go to the Insider Risk Management solution.
3. Select Cases in the left navigation.
4. Select a case, and then select Send email notice on the case action toolbar.
5. In the Send e-mail notice dialog box, select the Choose a notice template dropdown control to select the notice template for the notice. This selection pre-fills the other fields in the notice.
6. Review the notice fields and update as appropriate. The values you enter override the values in the template.
7. Select Send to send the notice to the user.

## Validation
1. Sign in to the Microsoft Purview portal with the same admin account used to send the notice. 2. Navigate to Insider Risk Management > Cases. 3. Select the case from which the notice was sent. 4. On the case details page, scroll to the 'User activity' or 'Case notes' section to confirm the notice is listed as a sent notification. 5. Optionally, check the user's mailbox (if accessible) to verify the email was delivered.

## Rollback
1. Sign in to the Microsoft Purview portal with an admin account. 2. Navigate to Insider Risk Management > Cases. 3. Select the case where the notice was sent. 4. In the case action toolbar, select 'Send email notice' again. 5. In the dialog, choose a notice template that indicates a retraction or correction (if available) or send a follow-up notice explaining the error. 6. If the original notice contained incorrect information, contact the user directly via another channel to clarify. 7. Document the incident and corrective actions taken.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
