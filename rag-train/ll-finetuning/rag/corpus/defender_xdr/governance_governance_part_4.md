# Governance: Governance

**Domain:** Defender XDR
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that Microsoft Defender for Office 365 Safe Attachments policy is not being applied to all users in the tenant. How can the administrator verify and enforce the policy scope using the Microsoft 365 Defender portal?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Safe Attachments policy named 'Default Safe Attachments Policy' with scope set to 'Selected recipients' instead of 'All recipients'

## Symptoms
- Some users receive email attachments that are not scanned by Safe Attachments
- The Safe Attachments policy report shows lower-than-expected scanning volume

## Error Codes
N/A

## Root Causes
1. The Safe Attachments policy scope was configured to apply only to specific users or groups, not to all recipients in the domain

## Remediation Steps
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com)
2. Navigate to Email & Collaboration > Policies & Rules > Threat policies > Safe Attachments
3. Select the policy that is not covering all users and click Edit
4. In the 'Applied to' section, change the scope from 'Selected recipients' to 'All recipients'
5. Save the policy and verify the change in the policy list

## Validation
After updating the policy scope, generate a Safe Attachments report for the next 24 hours and confirm that all users are now included in scanning activity.

## Rollback
Re-edit the policy and revert the scope to the previous selection of recipients or groups.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-policies>
