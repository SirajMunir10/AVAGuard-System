# Troubleshooting: Identity Explorer

**Domain:** Defender for Endpoint
**Subdomain:** Identity Explorer
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify service accounts with RDP access to critical device using predefined scenarios in Identity Explorer?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Identity Explorer predefined scenario: Service accounts with RDP access to critical device

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Search with predefined scenarios.
2. Choose the scenario: Service accounts with RDP access to critical device.
3. This scenario maps to MITRE ATT&CK technique: Lateral Movement.

## Validation
1. Open Microsoft 365 Defender portal (https://security.microsoft.com).
2. Navigate to Identity Explorer under Identities > Identity Explorer.
3. Click 'Search with predefined scenarios' and select 'Service accounts with RDP access to critical device'.
4. Confirm the query returns a list of service accounts that have RDP access to critical devices.
5. Verify that the results include the expected service accounts and critical devices based on your environment.
6. Check that the scenario is mapped to MITRE ATT&CK technique: Lateral Movement (T1021).

## Rollback
1. If the predefined scenario does not return expected results or causes confusion, revert to a custom query by clicking 'New query' in Identity Explorer.
2. Remove any filters or conditions that were automatically applied by the predefined scenario.
3. Alternatively, close the Identity Explorer blade and reopen it to reset the query interface.
4. If the issue persists, clear browser cache or use an InPrivate/Incognito session to access the portal.
5. For persistent problems, contact Microsoft Support with the scenario details and environment context.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
