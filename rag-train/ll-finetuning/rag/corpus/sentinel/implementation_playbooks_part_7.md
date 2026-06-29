# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I configure authentication for a Microsoft Sentinel playbook connection using managed identity, OAuth, or service principal?

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
1. On the Create connection pane, provide the required information to connect to Microsoft Sentinel.
2. For Authentication, select from the following methods: OAuth, Service principal, or Managed identity.
3. For optimal security, Microsoft recommends using a managed identity for authentication when possible.

## Validation
1. In the Azure portal, navigate to the playbook's Logic App resource. 2. Under 'Identity', verify that 'System assigned' managed identity is enabled (if using managed identity). 3. Go to the playbook's 'API Connections' and select the Microsoft Sentinel connection. 4. In the connection's 'Authentication' tab, confirm the authentication method matches the intended configuration (e.g., 'Managed Identity'). 5. Run a test trigger or action in the playbook to confirm successful authentication and data retrieval.

## Rollback
1. In the Azure portal, navigate to the Logic App resource for the playbook. 2. Under 'API Connections', select the Microsoft Sentinel connection. 3. In the connection pane, change the 'Authentication' method back to the previous method (e.g., from 'Managed Identity' to 'OAuth' or 'Service Principal'). 4. If using managed identity, disable 'System assigned' identity under 'Identity' if it was enabled. 5. Reconfigure any dependent permissions (e.g., role assignments for the service principal) to match the previous authentication method. 6. Test the playbook to confirm it operates with the original authentication settings.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
