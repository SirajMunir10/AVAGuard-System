# Optimization: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Optimization

## Scenario / Query
A tenant has over 200 Conditional Access policies, many of which are in 'Report-only' mode and have never been enabled. How can the administrator identify and clean up unused or redundant policies to reduce complexity and improve performance?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Conditional Access policies with status set to 'report-only' and no modifications in the last 90 days

## Symptoms
- High number of Conditional Access policies causing administrative confusion
- Multiple policies with overlapping conditions and controls
- Policies in 'Report-only' mode that have been active for more than 90 days without being enabled or disabled

## Error Codes
N/A

## Root Causes
1. Lack of regular policy lifecycle management
2. No process to review and retire unused policies
3. Policies created for testing or temporary scenarios and never cleaned up

## Remediation Steps
1. Use the Conditional Access insights and reporting workbook in the Azure portal to review policy usage and effectiveness
2. Identify policies that have been in 'Report-only' mode for more than 90 days and have no sign-in logs showing impact
3. Disable or delete policies that are no longer needed, following the documented guidance: 'If a policy is no longer needed, you can delete it'
4. Consolidate multiple policies with similar conditions into a single policy using the 'What If' tool to verify coverage

## Validation
After cleanup, verify that the number of active policies is reduced and that the remaining policies cover all required scenarios without overlap. Use the Conditional Access 'What If' tool to test that intended users and apps are still protected.

## Rollback
If a deleted policy is needed again, recreate it using the original configuration from the audit log or a backup export. Policies in 'Report-only' mode can be re-enabled from the Azure portal.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-lifecycle>
