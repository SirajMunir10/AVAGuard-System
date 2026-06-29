# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to create a Conditional Access policy that blocks noncompliant devices from accessing corporate resources?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Intune integration
- **Configuration:** Conditional Access policy requiring device compliance for all cloud apps

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure admin access to the Microsoft Intune admin center.
2. Ensure permissions equal to the Conditional Access Administrator role in Entra ID for managing Conditional Access policies.
3. Create the policy in Report-only mode first to log what the policy would have done without blocking anyone, confirming scope and catching misconfigurations before enforcement.
4. After validation, enable the policy to enforce blocking of noncompliant devices.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com) with an account that has the Conditional Access Administrator role.
2. Navigate to Endpoint security > Conditional Access > Policies.
3. Locate the newly created policy (e.g., 'Block noncompliant devices').
4. Confirm the policy state is set to 'Report-only' (if not yet enabled) or 'On' (if enforcement is active).
5. Under 'Assignments', verify that 'Users and groups' includes the intended test users or all users.
6. Under 'Cloud apps or actions', confirm 'All cloud apps' is selected.
7. Under 'Conditions', verify that 'Device platforms' includes the relevant platforms (e.g., iOS, Android, Windows).
8. Under 'Grant', confirm that 'Require device to be marked as compliant' is selected and 'Block access' is not selected (since blocking is achieved by denying grant).
9. Use the 'What If' tool in Conditional Access to simulate a sign-in from a noncompliant device and confirm the policy would apply and block access.
10. If the policy is in Report-only mode, check the sign-in logs in Entra ID for the past hour to see entries where the policy was evaluated and would have blocked access.
11. If the policy is enabled, attempt to access a corporate resource (e.g., Exchange Online) from a noncompliant device and verify access is blocked with an appropriate error message.

## Rollback
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com) with an account that has the Conditional Access Administrator role.
2. Navigate to Endpoint security > Conditional Access > Policies.
3. Locate the policy (e.g., 'Block noncompliant devices').
4. If the policy is currently enabled (state 'On'), set the state to 'Off' to immediately stop enforcement.
5. If the policy is in Report-only mode and causing issues, set the state to 'Off' as well.
6. Alternatively, to preserve the policy configuration for later use, change the state to 'Report-only' (if currently 'On') to disable enforcement while retaining the policy definition.
7. Verify the change by refreshing the policy list and confirming the state is now 'Off' or 'Report-only'.
8. If the policy was incorrectly scoped, edit the policy assignments (e.g., remove all users or specific groups) to prevent unintended blocking.
9. Monitor sign-in logs in Entra ID for the next 15 minutes to confirm that blocked users are now able to access resources.
10. If the policy was part of a phased rollout, consider deleting the policy entirely and recreating it with corrected settings.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
