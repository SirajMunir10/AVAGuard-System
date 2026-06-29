# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
Which role groups can create and manage unrestricted DLP policies in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy management roles

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign users to the Compliance administrator role group.
2. Assign users to the Compliance data administrator role group.
3. Assign users to the Information Protection role group.
4. Assign users to the Information Protection Admin role group.
5. Assign users to the Security administrator role group.

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user assigned to one of the role groups listed in the remediation steps.
2. Navigate to Data Loss Prevention > Policies.
3. Click 'Create policy' and select a template (e.g., 'Custom').
4. On the 'Name your policy' page, enter a test policy name and click 'Next'.
5. On the 'Choose locations' page, select 'Exchange email' and 'SharePoint sites'.
6. On the 'Define policy settings' page, choose 'Create or customize advanced DLP rules'.
7. Add a rule with an action such as 'Block people from sharing and restrict access to shared content'.
8. Complete the wizard and confirm the policy is created and appears in the policy list.
9. Attempt to modify the policy (e.g., change locations or rules) and save changes.
10. Delete the test policy to clean up.
11. Verify that a user not in these role groups cannot create or manage DLP policies (optional negative test).

## Rollback
1. If a user was incorrectly added to a role group, sign in to the Microsoft 365 admin center (https://admin.microsoft.com) as a Global Administrator.
2. Go to Roles > Role assignments.
3. Select the role group (e.g., Compliance administrator) and remove the user from the group.
4. Repeat for any other role groups where the user was incorrectly added.
5. If a test DLP policy was created and not deleted, navigate to Data Loss Prevention > Policies in the Purview compliance portal.
6. Select the test policy and click 'Delete policy'.
7. Confirm deletion.
8. If any unintended changes were made to existing DLP policies, restore them from backup or reconfigure them to their previous state using the policy edit wizard.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
