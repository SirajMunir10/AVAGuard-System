# Implementation: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Implementation

## Scenario / Query
How to use Copilot in Defender to convert natural-language questions into KQL queries for proactive threat hunting?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Copilot in Defender enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the query assistant in advanced hunting to convert natural-language questions into ready-to-run KQL queries.
2. The generated KQL query can be run immediately or tweaked to the analyst's needs.

## Validation
1. Open the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Navigate to 'Hunting' > 'Advanced hunting'.
3. In the query assistant pane, enter a natural-language question (e.g., 'Show all sign-ins from suspicious IP addresses in the last 24 hours').
4. Verify that Copilot generates a KQL query in the query editor.
5. Confirm the generated query is syntactically valid by clicking 'Run query' and observing that results are returned without errors.
6. Optionally, modify the query and re-run to confirm the assistant supports iterative refinement.

## Rollback
1. If the Copilot-generated query fails or produces unexpected results, manually clear the query editor and revert to a previously saved or known-good KQL query.
2. If the query assistant is non-functional, disable the Copilot feature temporarily via 'Settings' > 'Microsoft 365 Defender' > 'Copilot in Defender' and toggle off 'Enable Copilot in Defender'.
3. Re-enable the feature after troubleshooting by following the same path and toggling it back on.
4. If issues persist, contact Microsoft support referencing the source documentation at https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
