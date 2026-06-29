# Troubleshooting: Policy Compliance (AADSTS53003: Access has been blocked by Conditional Access policies. The access policy does not allow token issuance.)

**Domain:** Governance
**Subdomain:** Policy Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that they cannot access a SharePoint Online site, and the error message indicates that access is blocked by a Conditional Access policy. How do I troubleshoot and resolve this issue?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Conditional Access policies configured via Azure AD

## Symptoms
- User receives an access denied error when trying to access SharePoint Online
- Error message references a Conditional Access policy blocking the request

## Error Codes
- `AADSTS53003: Access has been blocked by Conditional Access policies. The access policy does not allow token issuance.`

## Root Causes
1. The user's sign-in does not meet the conditions of the assigned Conditional Access policy (e.g., device compliance, location, or MFA requirement)

## Remediation Steps
1. 1. Sign in to the Azure portal as a Global Administrator or Security Administrator.
2. 2. Navigate to Azure Active Directory > Security > Conditional Access > Troubleshoot using the 'What If' tool.
3. 3. Enter the user's details, the target cloud app (SharePoint Online), and the sign-in conditions.
4. 4. Review the policies that apply and identify which policy is blocking access.
5. 5. Adjust the policy conditions or grant controls to allow the user's access, or ensure the user meets the policy requirements (e.g., enroll device in Intune, perform MFA).
6. 6. If the policy is correct, instruct the user to meet the requirements (e.g., use a compliant device, connect from a trusted location).

## Validation
After remediation, ask the user to attempt access to SharePoint Online again. Verify that the sign-in logs show a success with no policy blocking.

## Rollback
If the policy change causes unintended access, revert the policy to its previous state using the Azure AD Conditional Access policy version history or by restoring from backup.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if>
