# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to create a Conditional Access policy requiring multifactor authentication, compliant devices, or Microsoft Entra hybrid joined devices?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access Administrator role required

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Conditional Access Administrator.
2. Browse to Entra ID > Conditional Access > Policies.
3. Select New policy.
4. Give your policy a name. Create a meaningful standard for the names of your policies.
5. Under Assignments, select Users or workload identities.
6. Under Include, select All users.
7. Under Exclude: Select Users and groups. Choose your organization's emergency access or break-glass accounts. If you use hybrid identity solutions like Microsoft Entra Connect or Microsoft Entra Connect Cloud Sync, select Directory roles, then select Directory Synchronization Accounts.
8. Under Target resources > Resources (formerly cloud apps) > Include, select All resources (formerly 'All cloud apps'). If you must exclude specific applications from your policy, you can choose them from the Exclude tab under Select excluded cloud apps and choose Select.
9. Under Access controls > Grant. Select Require multifactor authentication, Require device to be marked as compliant, and Require Microsoft Entra hybrid joined device. For multiple controls select Require one of the selected controls. Select Select.
10. Confirm your settings and set Enable policy to Report-only. Select Create to enable your policy.
11. After confirming your settings using policy impact or report-only mode, move the Enable policy toggle from Report-only to On.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator.
2. Browse to Identity > Conditional Access > Policies.
3. Locate the policy you created.
4. Confirm the policy name matches the naming standard you defined.
5. Under Assignments > Users or workload identities, verify:
   - Include: All users is selected.
   - Exclude: Your emergency access or break-glass accounts are listed, and if using hybrid identity solutions, Directory Synchronization Accounts role is excluded.
6. Under Target resources > Resources (formerly cloud apps) > Include, verify All resources is selected (or the specific apps you chose).
7. Under Access controls > Grant, verify:
   - Require multifactor authentication is checked.
   - Require device to be marked as compliant is checked.
   - Require Microsoft Entra hybrid joined device is checked.
   - For multiple controls, Require one of the selected controls is selected.
8. Confirm the Enable policy toggle is set to On (or Report-only if you haven't switched yet).
9. Use the What If tool (under Conditional Access > What If) with a test user to simulate sign-in and confirm the policy applies as expected.
10. Monitor sign-in logs for a test user to verify the policy is enforced (e.g., MFA prompt, device compliance check).

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator.
2. Browse to Identity > Conditional Access > Policies.
3. Locate the policy you created.
4. Set the Enable policy toggle to Off to disable the policy immediately.
5. If you need to delete the policy, select Delete after disabling it.
6. If the policy was in Report-only mode and caused issues, switch it back to Off or delete it.
7. Verify that users are no longer blocked or prompted unexpectedly by checking sign-in logs for a test user.
8. If the policy was partially configured (e.g., incorrect exclusions), edit the policy to correct the assignments or access controls before re-enabling.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
