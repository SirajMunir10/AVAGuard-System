# Governance: Governance

**Domain:** Defender XDR
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
A security operations team notices that Microsoft Defender for Office 365 Safe Attachments and Safe Links policies are not being applied to all users. How can they verify and enforce consistent policy assignment across the tenant using Microsoft 365 Defender and Microsoft 365 admin center?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Safe Attachments and Safe Links policies are configured but not assigned to all users or domains

## Symptoms
- Users report receiving malicious attachments that should have been blocked by Safe Attachments
- Safe Links are not being rewritten for some recipients
- Security team finds that some users are not covered by any Safe Attachments or Safe Links policy

## Error Codes
N/A

## Root Causes
1. Policies were created but not assigned to all users, groups, or domains
2. Policies were assigned to a subset of users but not to all required recipients
3. Policy priority order may cause unintended gaps in coverage

## Remediation Steps
1. In the Microsoft 365 Defender portal, go to Email & collaboration > Policies & rules > Threat policies > Safe Attachments and Safe Links.
2. Review each policy's 'Applied to' section to ensure it covers all users, groups, or domains as intended.
3. If a policy is missing coverage, edit the policy and add the missing recipients or create a new policy with broader scope.
4. Ensure that the default policy (which applies to all users not covered by custom policies) is enabled and configured with appropriate settings.
5. Use the Microsoft 365 admin center to verify that all users have the required licenses for Defender for Office 365.

## Validation
In the Microsoft 365 Defender portal, navigate to Reports > Email & collaboration > Threat protection status report and filter by Safe Attachments or Safe Links to confirm that all users are showing detection activity. Alternatively, use the 'Threat protection status' report to identify users with no policy coverage.

## Rollback
If a policy change causes unintended blocking, edit the policy to revert the scope or settings, or disable the policy temporarily. For the default policy, you can disable it but this is not recommended; instead, adjust custom policies to cover the intended users.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-policies?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/defender-office-365/safe-links-policies?view=o365-worldwide>
