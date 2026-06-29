# Troubleshooting: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Troubleshooting

## Scenario / Query
Why are DLP policy restrictions not being applied when a user uploads a sensitive file to a cloud service domain?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP Settings > Browser and domain restrictions to sensitive data

## Symptoms
- User uploads a sensitive file to a cloud service domain and the upload is allowed without block or alert.
- Audit event is generated but no alert is triggered.

## Error Codes
N/A

## Root Causes
1. The Service domains setting is set to Block but the target domain is not on the block list, so all other domains are allowed.
2. The DLP policy rule is set to Audit only instead of Block, so uploads are allowed even for blocked domains.
3. The sensitive file type detected (e.g., physical addresses) may not match the policy condition (e.g., credit card numbers) for alert generation.

## Remediation Steps
1. Verify the Service domains setting: go to Endpoint DLP Settings > Browser and domain restrictions to sensitive data.
2. Check if the target domain is listed in the block list (if set to Block) or allow list (if set to Allow).
3. Ensure the DLP policy rule uses the Audit or restrict activities on devices option set to Block (not Audit only).
4. Confirm the policy condition matches the sensitive information type in the file (e.g., credit card numbers vs. physical addresses).

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Browser and domain restrictions to sensitive data. Confirm the 'Service domains' setting is set to 'Block' and verify the target domain (e.g., 'dropbox.com') is listed in the 'Block these domains' list. If the setting is 'Allow', ensure the domain is not in the 'Allow these domains' list. 2. In the same DLP policy, review the rule action: go to Policy > Edit policy > Edit rule > Actions. Verify that 'Audit or restrict activities on devices' is set to 'Block' (not 'Audit only'). 3. Check the policy condition: under 'Conditions', confirm the 'Sensitive info types' list includes the type detected in the file (e.g., 'U.S. Social Security Number' or 'Credit Card Number'). If the file contains physical addresses, ensure 'Physical Addresses' is selected. 4. Generate a test upload of a file containing the matching sensitive info type to the target domain and confirm the upload is blocked and an alert is generated in the DLP alerts page.

## Rollback
1. If the block is too restrictive, change the 'Service domains' setting back to 'Allow' or remove the target domain from the 'Block these domains' list. 2. If blocking causes false positives, revert the rule action to 'Audit only' by editing the DLP policy rule and setting 'Audit or restrict activities on devices' to 'Audit only'. 3. If the policy condition is too broad, remove the sensitive info type that is causing unintended matches. 4. After any rollback, verify that legitimate uploads to the target domain are allowed and no alerts are generated for non-sensitive files.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
