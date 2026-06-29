# Troubleshooting: Identity Explorer

**Domain:** Defender for Endpoint
**Subdomain:** Identity Explorer
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate non-privileged users with a path to own AD domain (DCSync) using predefined scenarios in Identity Explorer?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Identity Explorer predefined scenario: Non-privileged users with a path to own AD domain (DCSync)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Search with predefined scenarios.
2. Choose the scenario: Non-privileged users with a path to own AD domain (DCSync).
3. This scenario maps to MITRE ATT&CK techniques: Privilege Escalation, Credential Access.

## Validation
1. In Microsoft 365 Defender, navigate to Identity Explorer. 2. Click 'Search with predefined scenarios'. 3. Verify that the scenario 'Non-privileged users with a path to own AD domain (DCSync)' is listed and selectable. 4. Run the scenario and confirm that the results display users and paths that match the expected output for DCSync attack paths. 5. Optionally, cross-reference the results with the MITRE ATT&CK techniques (Privilege Escalation, Credential Access) as documented.

## Rollback
1. If the predefined scenario does not appear or returns unexpected results, clear any custom filters or saved queries in Identity Explorer. 2. Refresh the Identity Explorer page to reload the default predefined scenarios. 3. If the issue persists, verify that the Microsoft 365 Defender tenant has the required licenses and permissions for Identity Explorer as per Microsoft documentation. 4. As a last resort, contact Microsoft support to restore the default predefined scenarios.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
