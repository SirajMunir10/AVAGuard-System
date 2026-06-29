# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to configure endpoint DLP settings to restrict activities for unallowed apps?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Apply restriction to all activity, and select Allow. Audit and Off will not work.
2. For all other apps, set the Access by apps that aren't on the 'unallowed apps' list setting to Block.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP policies. 2. Open the policy you configured. 3. Under 'Access by unallowed apps', confirm 'Apply restriction to all activity' is selected and set to 'Allow'. 4. Under 'Access by apps that aren't on the unallowed apps list', confirm the setting is 'Block'. 5. On a test endpoint, attempt to use an unallowed app to access a protected file; verify the activity is blocked and an audit event is generated in Activity Explorer.

## Rollback
1. In the same policy, under 'Access by unallowed apps', change the setting to 'Audit only' or 'Off' as needed. 2. Under 'Access by apps that aren't on the unallowed apps list', change the setting to 'Allow' or 'Audit only'. 3. Save the policy and wait for propagation (up to 30 minutes). 4. On a test endpoint, verify that the previously blocked app can now access protected files and that audit events reflect the new setting.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
