# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Conditional Access policy evaluation using the What If tool?

## Environment Context
- **Tenant Type:** Entra ID tenant
- **Configuration:** Conditional Access policies

## Symptoms
- Access to the What If page requires authorization
- Sign-in or directory change prompts appear

## Error Codes
N/A

## Root Causes
1. User lacks sufficient permissions to access the Conditional Access What If tool

## Remediation Steps
1. Try signing in with appropriate credentials
2. Try changing directories to the correct tenant

## Validation
1. Sign in to the Azure portal (https://portal.azure.com) with credentials that have at least the Conditional Access Administrator, Security Administrator, or Global Reader role.
2. Navigate to Microsoft Entra ID > Security > Conditional Access > What If.
3. Verify that the What If page loads without sign-in or directory change prompts.
4. Confirm that you can specify a user, application, or other conditions and run a What If evaluation.
5. Check that the evaluation results display the applicable Conditional Access policies and their effects.

## Rollback
1. If the What If page still shows authorization errors, sign out of the current session and sign in with a different account that has the required permissions (Conditional Access Administrator, Security Administrator, or Global Reader).
2. If directory change prompts appear, ensure you are in the correct tenant directory by selecting the appropriate directory from the Directory + subscription filter in the Azure portal.
3. If the issue persists, verify the user's role assignments in Microsoft Entra ID > Roles and administrators and assign the necessary role if missing.
4. As a last resort, clear the browser cache and cookies, then retry accessing the What If tool.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if>
