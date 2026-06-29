# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
A Conditional Access policy targeting 'All cloud apps' with a 'Require MFA' grant control is not being applied to guest users from external organizations, even though the policy includes 'All external users' in the assignment. What is the most likely cause and how should it be fixed?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Conditional Access policy with 'All cloud apps' and 'Require MFA' grant, assigned to 'All external users'. Guest users from an external Microsoft Entra tenant are able to access applications without MFA.

## Symptoms
- Guest users from external organizations are not prompted for MFA when accessing applications protected by the Conditional Access policy.
- The Conditional Access policy appears to be enabled and correctly scoped to 'All external users'.
- No other Conditional Access policies are blocking or overriding this policy.

## Error Codes
N/A

## Root Causes
1. The 'Require MFA' grant control in a Conditional Access policy does not automatically enforce MFA for guest users from external tenants unless the external tenant trusts the resource tenant's MFA. By default, external users are subject to their home tenant's MFA policies, not the resource tenant's.
2. The resource tenant's cross-tenant access settings for the external organization may not be configured to trust MFA from the resource tenant.

## Remediation Steps
1. In the resource tenant, navigate to 'External Identities' > 'Cross-tenant access settings'.
2. Select the external organization's tenant ID or domain.
3. Under 'Inbound access', go to 'Trust settings' and check the box for 'Trust multi-factor authentication from Microsoft Entra ID tenants'.
4. Save the configuration. This allows the resource tenant's Conditional Access policy to require MFA for guest users from that external organization.

## Validation
After configuring cross-tenant trust for MFA, sign in as a guest user from the external organization. Verify that the user is prompted for MFA when accessing an application covered by the Conditional Access policy.

## Rollback
Uncheck the 'Trust multi-factor authentication from Microsoft Entra ID tenants' option in the cross-tenant access settings for the external organization.

## References
- Microsoft Learn: 'Plan a Microsoft Entra Conditional Access deployment' - https://learn.microsoft.com/en-us/entra/identity/conditional-access/plan-conditional-access
