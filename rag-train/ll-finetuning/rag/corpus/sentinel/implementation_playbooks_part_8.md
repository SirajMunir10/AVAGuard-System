# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I configure authentication for a Microsoft Sentinel playbook?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Authentication options for Microsoft Sentinel connector

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Based on your selected authentication option, provide the necessary parameter values for the corresponding option.
2. For Tenant ID, select your Microsoft Entra tenant ID.
3. When you finish, select Sign in.

## Validation
1. In the Microsoft Sentinel portal, navigate to Automation > Playbooks and select the playbook. 2. Under Playbook Authentication, confirm the authentication method (e.g., Managed Identity or Service Principal) is configured. 3. Verify the Tenant ID matches your Microsoft Entra tenant ID. 4. Run a test trigger or action in the playbook and check the run history for successful authentication (no 401 or 403 errors).

## Rollback
1. In the playbook's Logic App designer, open the Microsoft Sentinel connector action. 2. Change the authentication method back to the previous setting (e.g., from Managed Identity to Service Principal or vice versa). 3. If using Service Principal, re-enter the previous Tenant ID, Client ID, and Client Secret. 4. Select Sign in to re-authenticate with the original credentials. 5. Save the playbook.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
