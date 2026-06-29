# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
What to do if you're locked out because of an incorrect setting in a Conditional Access policy?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Locked out due to an incorrect setting in a Conditional Access policy

## Error Codes
N/A

## Root Causes
1. Incorrect setting in a Conditional Access policy

## Remediation Steps
1. Check if there are other admins in your organization who aren't blocked yet.
2. An admin with access can disable the policy that's affecting your sign-in.
3. If no admin in your organization can update the policy, submit a support request.
4. Microsoft support reviews and, after confirming, updates the Conditional Access policies that prevent access.

## Validation
1. Confirm that you can sign in to the Azure portal (https://portal.azure.com) with an account that is not affected by the problematic Conditional Access policy.
2. Navigate to Azure Active Directory > Security > Conditional Access.
3. Verify that the policy identified as causing the lockout is now disabled (Status = Off) or has been updated to exclude your account or the affected users.
4. Attempt to sign in with the previously locked-out account to confirm access is restored.

## Rollback
1. If the policy was disabled and you need to re-enable it, sign in as an unaffected admin and navigate to Azure Active Directory > Security > Conditional Access.
2. Locate the policy and set its status back to On.
3. If the policy was modified (e.g., exclusions removed), revert those changes to the original configuration.
4. If you cannot perform these steps because no admin has access, submit a new support request to Microsoft to restore the previous policy state.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
