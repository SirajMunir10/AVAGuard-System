# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure Service domains settings in Endpoint DLP to block or allow uploads of sensitive files to specific cloud service domains?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP Settings > Browser and domain restrictions to sensitive data

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to Endpoint DLP Settings > Browser and domain restrictions to sensitive data.
2. Choose whether to block or allow Service domains by default.
3. If set to Block, use Add cloud service domain to specify domains to block; all other domains are allowed.
4. If set to Allow, use Add cloud service domain to specify domains that are allowed; all other domains have DLP policy restrictions enforced.
5. Ensure the DLP policy rule uses the Audit or restrict activities on devices option with actions like Block with override.
6. Note: Service domains setting only applies to files uploaded via Microsoft Edge, or Google Chrome/Mozilla Firefox with Microsoft Purview Chrome Extension installed.

## Validation
1. Verify that the 'Browser and domain restrictions to sensitive data' setting is configured as intended by navigating to Endpoint DLP Settings > Browser and domain restrictions to sensitive data in the Microsoft Purview compliance portal. 2. Confirm the default action (Block or Allow) matches the desired configuration. 3. Check that the specified cloud service domains are listed under 'Add cloud service domain'. 4. Ensure the DLP policy rule includes the 'Audit or restrict activities on devices' action with 'Block with override' or similar restriction. 5. Test by attempting to upload a sensitive file to a blocked domain via Microsoft Edge (or Chrome/Firefox with the Purview extension) and verify the upload is blocked. 6. Test by uploading to an allowed domain and confirm the upload proceeds without restriction.

## Rollback
1. Navigate to Endpoint DLP Settings > Browser and domain restrictions to sensitive data. 2. If the default action was changed, revert it to the previous setting (Block or Allow). 3. Remove any incorrectly added cloud service domains by selecting them and clicking 'Remove'. 4. If domains were mistakenly removed, re-add them using 'Add cloud service domain'. 5. If the DLP policy rule was modified, edit the policy to restore the original actions (e.g., remove 'Block with override' or revert to 'Audit only'). 6. Verify that uploads to previously blocked domains are no longer blocked, and uploads to previously allowed domains are restricted as before.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
