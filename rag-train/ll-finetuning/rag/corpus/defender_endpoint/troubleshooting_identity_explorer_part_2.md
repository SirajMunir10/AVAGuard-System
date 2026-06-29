# Troubleshooting: Identity Explorer

**Domain:** Defender for Endpoint
**Subdomain:** Identity Explorer
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify Kerberoastable users with a path to a critical asset using predefined scenarios in Identity Explorer?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Identity Explorer predefined scenario: Kerberoastable users with a path to a critical asset

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Search with predefined scenarios.
2. Choose the scenario: Kerberoastable users with a path to a critical asset.
3. This scenario maps to MITRE ATT&CK techniques: Privilege Escalation, Credential Access.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Identity > Identity Explorer.
3. Click 'Search with predefined scenarios'.
4. Select the scenario 'Kerberoastable users with a path to a critical asset'.
5. Confirm that the query returns a list of users who are Kerberoastable and have an attack path to a critical asset.
6. Verify that the results include relevant user details and the associated critical asset path.
7. Optionally, export the results to confirm the data is accurate.

## Rollback
1. If the predefined scenario does not return expected results or causes confusion, clear the current query by clicking 'New query' or resetting the search.
2. Alternatively, manually construct a query using the Identity Explorer query builder to filter for Kerberoastable users and critical asset paths.
3. If the issue persists, refer to the official documentation at https://learn.microsoft.com/en-us/defender-xdr/investigate-users for alternative investigation methods.
4. Contact Microsoft Support if the predefined scenario is unavailable or malfunctioning.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
