# Troubleshooting: Identity Explorer

**Domain:** Defender for Endpoint
**Subdomain:** Identity Explorer
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate external Entra users with direct permissions to cloud resources using predefined scenarios in Identity Explorer?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Identity Explorer predefined scenario: External Entra users with direct permissions to cloud resources

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Search with predefined scenarios.
2. Choose the scenario: External Entra users with direct permissions to cloud resources.
3. This scenario maps to MITRE ATT&CK technique: Lateral Movement.

## Validation
1. In Microsoft 365 Defender, navigate to Identity Explorer. 2. Select 'Search with predefined scenarios'. 3. Choose the scenario 'External Entra users with direct permissions to cloud resources'. 4. Confirm that the query returns a list of external Azure AD users who have direct permissions to cloud resources. 5. Verify that the results include relevant user details such as user name, permissions, and resource scope. 6. Check that the scenario is correctly mapped to MITRE ATT&CK technique: Lateral Movement.

## Rollback
1. If the predefined scenario does not return expected results or causes confusion, revert to a custom KQL query in Identity Explorer. 2. Use the following query as a fallback: 'IdentityDirectoryEvents | where ActionType == "Assign role to user" | where AccountUpn contains "#EXT#" | project Timestamp, AccountUpn, RoleName, ResourceName, ResourceType'. 3. Alternatively, clear the search and select a different predefined scenario or use the default view. 4. If issues persist, contact Microsoft support for assistance with Identity Explorer functionality.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
