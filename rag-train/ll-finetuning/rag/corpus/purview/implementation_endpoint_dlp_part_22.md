# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure sensitive service domains for endpoint DLP to control file uploads to specific websites?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy with Service Domains list

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Exclude the protocol (anything before //) from the domain.
2. Only include the host name, without any subsites.
3. Use a wildcard (*) to specify all domains or subdomains.
4. Configure up to 50 domains under Sensitive Service domains.
5. Note: The Service domains list setting only applies to file uploads to websites. Actions like pasting into a browser don't follow the Service Domain list.

## Validation
1. Open the Microsoft Purview compliance portal and navigate to Data Loss Prevention > Endpoint DLP settings > Sensitive service domains. 2. Confirm that the configured domains match the remediation guidance: no protocol prefix (e.g., 'contoso.com' not 'https://contoso.com'), only host names without subsites, and wildcards used appropriately. 3. Verify the total number of entries does not exceed 50. 4. Test a file upload to a website that matches a configured domain and confirm the DLP policy blocks or allows the upload as intended. 5. Test a file upload to a website that does not match any configured domain and confirm the default DLP action applies. 6. Confirm that clipboard paste actions to the same domains are not affected by the service domain list.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Endpoint DLP settings > Sensitive service domains. 2. Remove or edit any incorrectly added domains to restore the previous list. 3. If the entire list needs to be cleared, delete all entries. 4. If the policy itself is causing issues, temporarily disable the Endpoint DLP policy that references the service domains list. 5. Re-test file uploads to ensure the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
