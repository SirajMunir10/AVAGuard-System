# Optimization: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Optimization

## Scenario / Query
A tenant has Conditional Access policies that grant access based on device compliance but does not exclude the 'Global Administrator' role. How can this be optimized to reduce risk of lockout and align with Microsoft's recommended practices?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Conditional Access policies targeting all users including Global Administrators without emergency break-glass accounts excluded

## Symptoms
- Potential lockout of Global Administrators if device compliance fails
- No break-glass accounts excluded from Conditional Access policies
- Policy does not include 'Emergency' or 'Break-Glass' accounts as exclusion

## Error Codes
N/A

## Root Causes
1. Conditional Access policy does not exclude at least one emergency access account
2. Global Administrator role not excluded from device compliance requirement

## Remediation Steps
1. Identify or create at least two cloud-only emergency access accounts (e.g., 'emergency1@contoso.com') that are assigned the Global Administrator role and excluded from all Conditional Access policies.
2. Modify the Conditional Access policy to exclude the emergency access accounts under 'Exclude > Users and groups'.
3. Ensure the emergency access accounts are not subject to multi-factor authentication or device compliance requirements.
4. Document the emergency access accounts in a secure, offline location.

## Validation
Sign in with an emergency access account and confirm no Conditional Access policy is triggered. Verify the account can access the Azure portal without MFA or device compliance checks.

## Rollback
Remove the exclusion for the emergency access accounts from the Conditional Access policy, then re-add them to the policy scope.

## References
- CIS Microsoft 365 Foundations Benchmark v2.0.0, Control 1.1.1: 'Ensure that at least two emergency access accounts are configured'
