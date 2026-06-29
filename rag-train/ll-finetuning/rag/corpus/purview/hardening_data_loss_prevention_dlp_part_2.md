# Hardening: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Hardening

## Scenario / Query
A Microsoft 365 tenant has DLP policies that are not being enforced because the required licenses are not assigned to all users. How can an administrator verify that all users covered by a DLP policy have the appropriate licenses and harden the configuration to prevent future gaps?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 or A5 (includes Purview DLP licensing)
- **Configuration:** DLP policies created in the Microsoft Purview compliance portal

## Symptoms
- DLP policy actions (e.g., block, notify) are not applied to some users
- Audit logs show DLP rule matches but no enforcement action taken
- Users without appropriate licenses are inadvertently included in DLP policy scopes

## Error Codes
N/A

## Root Causes
1. Users included in DLP policy scope do not have the required Microsoft 365 E5/A5/G5 or equivalent standalone DLP license
2. DLP policy was configured without verifying license coverage for all scoped users

## Remediation Steps
1. Identify all users scoped in the DLP policy using the Microsoft Purview compliance portal > Data Loss Prevention > Policies > select policy > Locations
2. Verify that each user has an eligible license (e.g., Microsoft 365 E5, A5, G5, or Microsoft 365 E5 Compliance) by using the Microsoft 365 admin center > Users > Active users > select user > Licenses and apps
3. Assign the required license to any user missing it, or remove the user from the DLP policy scope
4. Use the Microsoft Purview compliance portal > Data Loss Prevention > Policies > Policy tips to confirm enforcement is active for all covered users
5. Optionally, use PowerShell cmdlet Get-DlpComplianceRule (from Exchange Online PowerShell) to review rule distribution

## Validation
Run a DLP policy test using the Microsoft Purview compliance portal > Data Loss Prevention > Policies > select policy > Test mode with policy tips to confirm enforcement for all scoped users with licenses.

## Rollback
Remove the license assignment from a user or remove the user from the DLP policy scope via the Locations tab in the policy settings.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp#licensing-for-data-loss-prevention>
