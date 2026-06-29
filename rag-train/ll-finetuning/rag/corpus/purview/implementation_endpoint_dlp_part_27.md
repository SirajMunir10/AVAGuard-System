# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure sensitive service domain groups with URL patterns and IP addresses for endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy with sensitive service domain groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set the Match type to IP address or IP address range and then enter a specific IP address or an IP range in the Sensitive service domain field.
2. Select Add site to add the selection to the Sensitive service domain group.
3. Supported syntax examples: 1.1.1.1-2.2.2.2, 2001:0db8:85a3:0000:0000:8a2e:0370:7334, 2001:0db8:85a3:0000:0000:8a2e:0370:7320-2001:0db8:85a3:0000:0000:8a2e:0370:7334
4. URL patterns support actions: Print the site, Copy data from the site, Save the site as local files (save-as), Paste to supported browsers, Upload to a restricted cloud service domain.
5. IP address and IP address range support actions: Print the site, Copy data from the site, Save the site as local files (save-as), Upload to a restricted cloud service domain (Windows only).
6. Sensitive service domain groups contain a preconfigured group for Generative AI websites.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP policies. 2. Select the policy that was configured with sensitive service domain groups. 3. Under 'Locations', confirm the policy is applied to the intended devices. 4. Under 'Rules', verify the rule includes a sensitive service domain group with the correct URL patterns and IP addresses. 5. Use the 'Test' feature in the policy to simulate an action (e.g., copy to clipboard) on a target URL or IP address from the group and confirm the expected action is blocked or allowed. 6. On a test device, attempt to upload a file to a restricted cloud service domain listed in the group and verify the DLP policy enforces the configured action (e.g., block upload).

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP policies, select the policy that was modified. 2. Under 'Rules', edit the rule that contains the sensitive service domain group. 3. Remove the sensitive service domain group or delete the specific URL patterns and IP addresses that were added. 4. Alternatively, disable the rule or policy temporarily by toggling the status to 'Off'. 5. Save the changes and confirm the policy is no longer enforcing the unintended restrictions. 6. If the policy was newly created, delete the policy entirely.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
