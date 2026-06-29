# Implementation: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Implementation

## Scenario / Query
How to assign a case from the Cases dashboard in Insider Risk Management?

## Environment Context
- **Tenant Type:** Microsoft 365 organization
- **Configuration:** Insider Risk Management solution enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal with credentials for an admin account in your Microsoft 365 organization.
2. Go to the Insider Risk Management solution.
3. Select Cases in the left navigation.
4. On the Cases dashboard, select the cases that you want to assign.
5. In the command bar over the cases queue, select Assign.
6. On the Assign owner pane on the right side of the screen, search for an admin with the appropriate permissions, and then select the checkbox for that admin.
7. Select Assign.

## Validation
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com) with an admin account that has the appropriate permissions (e.g., Insider Risk Management Admin, Insider Risk Management Analyst, or Insider Risk Management Investigator).
2. Navigate to Insider Risk Management > Cases.
3. On the Cases dashboard, locate the case(s) that were assigned in the remediation steps.
4. Verify that the 'Assigned to' column for each case now displays the name of the admin selected during the assignment.
5. (Optional) Click on the case to open its details and confirm that the 'Owner' field shows the assigned admin.

## Rollback
1. Sign in to the Microsoft Purview portal with an admin account that has the Insider Risk Management Admin or appropriate permissions.
2. Go to Insider Risk Management > Cases.
3. On the Cases dashboard, select the case(s) that were incorrectly assigned.
4. In the command bar, select 'Assign'.
5. In the 'Assign owner' pane, clear the checkbox for the current admin, or search for and select a different admin (e.g., the original owner or another authorized user).
6. Click 'Assign' to save the change.
7. Confirm that the 'Assigned to' column now reflects the correct owner.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
