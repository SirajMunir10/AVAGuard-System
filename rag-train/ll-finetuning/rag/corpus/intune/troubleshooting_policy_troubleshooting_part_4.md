# Troubleshooting: Policy Troubleshooting

**Domain:** Intune
**Subdomain:** Policy Troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to check tenant status and confirm subscription is active for Intune policy deployment?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Tenant Status

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Check the Tenant Status and confirm the subscription is Active.
2. View details for active incidents and advisories that may impact your policy or profile deployment.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Tenant administration > Tenant status.
3. Verify that the 'Tenant details' section shows 'Service health' as 'Healthy' and 'Subscription status' as 'Active'.
4. Under 'Service health dashboard', check for any active incidents or advisories that could affect policy deployment.
5. Confirm that no critical advisories are listed under 'Incidents' or 'Advisories'.

## Rollback
1. If the subscription is inactive, renew or reactivate the Microsoft Intune subscription via the Microsoft 365 admin center (https://admin.microsoft.com).
2. If an active incident or advisory is impacting policy deployment, wait for the incident to be resolved or follow the guidance provided in the advisory.
3. After resolving the subscription or service health issue, re-attempt the policy deployment from the Intune admin center.

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
