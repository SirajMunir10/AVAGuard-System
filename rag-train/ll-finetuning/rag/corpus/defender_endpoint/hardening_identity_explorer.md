# Hardening: Identity Explorer

**Domain:** Defender for Endpoint
**Subdomain:** Identity Explorer
**Incident Type:** Hardening

## Scenario / Query
How to use predefined identity scenarios in Identity Explorer to identify and harden against identity risks such as privilege escalation and lateral movement?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Identity Explorer with predefined scenarios

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Search with predefined scenarios to run identity-focused queries.
2. Each scenario maps to one or more MITRE ATT&CK techniques and focuses on a specific type of identity risk.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to **Identity Explorer** under **Endpoints** > **Investigation**.
3. Click **Search with predefined scenarios**.
4. Select a predefined scenario (e.g., 'Privilege escalation via Kerberos delegation' or 'Lateral movement using pass-the-hash').
5. Run the query and confirm that results are returned, showing relevant user entities and alerts.
6. Verify that the scenario description matches the expected MITRE ATT&CK technique (e.g., T1558.003 for Kerberos delegation).
7. Check that the query results include actionable data such as user accounts, devices, or alerts that can be used for hardening.

## Rollback
1. If the predefined scenario query returns no results or incorrect data, clear any custom filters applied to the query.
2. Reset the Identity Explorer to default view by clicking **Reset** or **Clear** in the query builder.
3. If the scenario selection is causing confusion, revert to using the standard search bar without predefined scenarios.
4. If the issue persists, verify that the Microsoft 365 Defender tenant has the required license (e.g., Microsoft Defender for Identity) and that data ingestion is active.
5. As a last resort, disable the Identity Explorer feature by restricting access via Azure AD Conditional Access or by contacting Microsoft Support to roll back any recent changes.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
