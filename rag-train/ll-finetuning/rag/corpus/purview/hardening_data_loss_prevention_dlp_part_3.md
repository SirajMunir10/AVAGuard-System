# Hardening: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Hardening

## Scenario / Query
A Microsoft 365 tenant has DLP policies enabled, but the admin notices that sensitive data is still being exfiltrated via email. How can the admin harden the DLP configuration to prevent bypass by users who override policy tips?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** DLP policies with 'Notify user' action enabled, but 'Override' option is allowed

## Symptoms
- Users receive policy tips but can override them and send sensitive data
- DLP incident reports show high number of overrides
- Sensitive data continues to leave the organization via email

## Error Codes
N/A

## Root Causes
1. DLP policy action is set to 'Notify user' without blocking the action
2. The 'Override' option is enabled, allowing users to bypass the policy

## Remediation Steps
1. Modify the DLP policy to change the action from 'Notify user' to 'Block the action' for high-risk sensitive information types
2. Disable the 'Override' option in the policy tip settings to prevent users from bypassing the block
3. Optionally, require users to provide a business justification when overriding, and log those justifications for audit

## Validation
Send a test email containing a credit card number to an external recipient; the email should be blocked and the sender should not see an override option.

## Rollback
Revert the DLP policy action back to 'Notify user' and re-enable the 'Override' option in the policy tip settings.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-create-manage-policy>
