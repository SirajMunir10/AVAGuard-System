# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to create a Conditional Access policy requiring compliant devices using Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policy with device compliance condition

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use report-only mode for Conditional Access to determine the results of new policy decisions.
2. Device compliance policies work with Microsoft Entra ID.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Global Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the newly created policy (e.g., 'Require compliant device'). 4. Verify the policy is set to 'Report-only' mode. 5. Use the 'What If' tool to simulate a user sign-in: enter a test user's details, select the target cloud app, and confirm the policy applies and the 'Grant' control shows 'Require device to be marked as compliant'. 6. Check the Conditional Access Insights and Reporting workbook to confirm the policy is generating logs in report-only mode without blocking access.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Global Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy that is causing issues. 4. Set the policy state to 'Off' to disable it immediately. 5. If the policy was already enabled, delete the policy by selecting 'Delete' from the policy's context menu. 6. Verify that the policy no longer appears in the list of active policies and that users regain access as expected.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
