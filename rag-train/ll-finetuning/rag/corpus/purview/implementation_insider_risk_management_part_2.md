# Implementation: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Implementation

## Scenario / Query
How do I configure administrative unit scoping for Insider Risk Management cases?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Policies scoped by one or more administrative units

## Symptoms
- Insider Risk Management users cannot see cases for users outside their administrative scope

## Error Codes
N/A

## Root Causes
1. Administrative unit scoping restricts case visibility to users within the defined scope

## Remediation Steps
1. Scope your policies by one or more administrative units
2. Give ownership of a case only to Insider Risk Management users with the appropriate role group permissions
3. Ensure the user highlighted in the alert is in scope of the admin unit
4. Unrestricted administrators can see all cases for all users in the organization

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user who is a member of the Insider Risk Management role group and is scoped to the administrative unit(s) that include the test user.
2. Navigate to Insider Risk Management > Cases.
3. Confirm that the test user’s cases are visible in the list.
4. Sign in as a different user who is a member of the Insider Risk Management role group but is NOT scoped to the administrative unit containing the test user.
5. Navigate to Insider Risk Management > Cases and verify that the test user’s cases are NOT visible.
6. (Optional) As an unrestricted administrator (e.g., Global Admin), confirm that all cases for all users are visible regardless of administrative unit scoping.

## Rollback
1. If the scoping causes unintended visibility restrictions, remove the administrative unit scoping from the Insider Risk Management role group:
   - In the Microsoft Purview compliance portal, go to Roles & scopes > Role groups.
   - Select the Insider Risk Management role group (e.g., Insider Risk Management Admins, Analysts, or Investigators).
   - Under 'Assigned administrative units', remove any assigned administrative units.
2. Alternatively, if the scoping was applied via a policy, edit the policy in Insider Risk Management > Policies, and clear the 'Scope by administrative units' setting.
3. Verify that all users with the Insider Risk Management role group can now see cases for all users in the organization.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
