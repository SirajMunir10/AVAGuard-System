# Governance: Governance

**Domain:** Defender XDR
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
A security operations team notices that Microsoft Defender for Office 365 is not automatically applying Safe Attachments policies to all users. They want to ensure that governance policies are enforced tenant-wide without manual assignment. How can they configure a default policy that covers all users, including future additions?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Office 365 Plan 2
- **Configuration:** Safe Attachments policy not set as default; no transport rule override

## Symptoms
- Some users are not protected by Safe Attachments policy
- New users added to the tenant are not automatically covered by Safe Attachments
- Security team must manually assign Safe Attachments policies to each user or group

## Error Codes
N/A

## Root Causes
1. No default Safe Attachments policy exists; only custom policies assigned to specific groups are configured
2. The 'Built-in Protection' or default policy for Safe Attachments is not enabled

## Remediation Steps
1. In the Microsoft 365 Defender portal, go to Policies & rules > Threat policies > Safe Attachments in the Email & collaboration section.
2. Select the 'Built-in Protection' policy (or create a new policy) and set the 'Applied to' scope to 'All recipients' or 'Default'.
3. Configure the Safe Attachments unknown malware response to 'Block' or 'Replace' as per organizational risk tolerance.
4. Enable the policy and ensure no other policies with higher priority are overriding it for specific users.
5. Verify that the policy is listed with Priority 0 (Lowest) to act as a catch-all for all users not covered by higher-priority custom policies.

## Validation
Send a test email with a benign EICAR test attachment to an unlicensed or new user and confirm it is blocked or quarantined by the Safe Attachments policy.

## Rollback
Disable or delete the default Safe Attachments policy, or change its scope to 'No one' to revert to per-user assignment.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/safe-attachments-about?view=o365-worldwide#built-in-protection>
