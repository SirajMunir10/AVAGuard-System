# Hardening: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Hardening

## Scenario / Query
How do I block all apps except those explicitly allowed in a restricted app group for endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, Restricted Apps and app groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to endpoint DLP settings.
2. Define allowed or sanctioned apps in the Restricted Apps and app groups list.
3. Apply the restriction level of 'Allow' to explicitly allow activity for a defined app group.
4. Any apps not on this list are effectively blocked.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data loss prevention > Endpoint DLP settings > Restricted Apps and app groups. 2. Confirm that the desired app group is listed with the restriction level set to 'Allow'. 3. From a test device, attempt to use an app that is NOT in the allowed app group to perform a sensitive data operation (e.g., copy to USB). Verify that the action is blocked and a DLP policy match is generated in Activity explorer. 4. From the same test device, use an app that IS in the allowed app group to perform the same sensitive data operation. Verify that the action is permitted and no DLP policy match is generated.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data loss prevention > Endpoint DLP settings > Restricted Apps and app groups. 2. Remove the app group that was added, or change its restriction level from 'Allow' to 'Block' or 'Audit Only' as needed. 3. If the app group was newly created, delete it entirely. 4. From a test device, verify that previously allowed apps are now blocked or audited according to the restored configuration.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
