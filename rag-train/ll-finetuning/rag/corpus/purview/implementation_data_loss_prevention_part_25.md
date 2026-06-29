# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How does assigning a DLP policy to an administrative unit affect administrator permissions and visibility?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview and Entra ID
- **Configuration:** Administrative unit restricted administrators.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The administrative unit restricted administrator will only be able to manage the DLP policy for that site.
2. The restricted administrator will only see policy match result data for the administrative unit in activity explorer and the alert dashboard.

## Validation
1. Sign in as the administrative unit restricted administrator. 2. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 3. Confirm the DLP policy assigned to the administrative unit is visible and manageable. 4. Go to Activity explorer and verify that only policy match results for the administrative unit are displayed. 5. Check the Alert dashboard to confirm alerts are scoped to the administrative unit.

## Rollback
1. Sign in as a global administrator or a role with permissions to modify administrative unit assignments. 2. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the DLP policy assigned to the administrative unit. 3. Under 'Assign to administrative units', remove the administrative unit assignment. 4. Save the policy. 5. Verify that the administrative unit restricted administrator can no longer manage the policy or see scoped data.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
