# Troubleshooting: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve issues where Privileged Identity Management cannot access Azure resources due to missing role assignment?

## Environment Context
- **Tenant Type:** Azure AD tenant with PIM enabled
- **Configuration:** Privileged Identity Management service principal (MS–PIM)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
1. The Privileged Identity Management service principal (MS–PIM) is not assigned the User Access Administrator role at the subscription or management group level.

## Remediation Steps
1. Assign the User Access Administrator role to the Privileged Identity Management service principal name (MS–PIM) at the subscription level.
2. Assign the role at a management group level or at the subscription level, depending on your requirements.

## Validation
1. Open Azure portal and navigate to Subscriptions. Select the target subscription. 2. Go to Access control (IAM) > View access for this resource. 3. In the search box, enter 'MS-PIM' and verify that the service principal appears with the 'User Access Administrator' role. 4. Alternatively, run Azure CLI: az role assignment list --scope /subscriptions/<subscription-id> --assignee 'MS-PIM' --output table. Confirm the output includes 'User Access Administrator'.

## Rollback
1. In Azure portal, go to the subscription or management group where the role was assigned. 2. Navigate to Access control (IAM) > Role assignments. 3. Find the assignment for 'MS-PIM' with role 'User Access Administrator'. 4. Select the assignment and click 'Remove'. 5. Confirm removal. 6. Alternatively, run Azure CLI: az role assignment delete --scope /subscriptions/<subscription-id> --assignee 'MS-PIM' --role 'User Access Administrator'.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-troubleshoot>
