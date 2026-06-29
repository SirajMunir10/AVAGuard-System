# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I select the appropriate authentication method when creating a playbook in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel playbook creation

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Authentication, select from the following methods: OAuth, Service principal, or Managed identity.
2. For optimal security, Microsoft recommends using a managed identity for authentication when possible.

## Validation
1. In the Microsoft Sentinel portal, navigate to Automation > Playbooks and confirm the playbook is listed with a status of 'Enabled'.
2. Open the playbook and verify the authentication method is set to 'Managed identity' (or the chosen method) under the 'Authentication' section.
3. Run a test trigger or manually execute the playbook to confirm it completes without authentication errors.
4. Check the playbook's run history for any 'AuthenticationFailed' or 'Unauthorized' entries.

## Rollback
1. In the Microsoft Sentinel portal, go to Automation > Playbooks and select the affected playbook.
2. Under 'Authentication', change the method back to the previous setting (e.g., from 'Managed identity' to 'OAuth' or 'Service principal').
3. Re-enter any required credentials or connection details if reverting to OAuth or Service principal.
4. Save the playbook and re-run a test to confirm the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
