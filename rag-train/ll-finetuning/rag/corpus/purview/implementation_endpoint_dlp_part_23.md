# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
What are the correct domain patterns to use when configuring sensitive service domains for endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP Service Domains list

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For exact domain match (e.g., contoso.com): Matches contoso.com and any subsite like //contoso.com, //contoso.com/, //contoso.com/anysubsite1, etc. Does not match sub-domains like anysubdomain.contoso.com.
2. For wildcard subdomain match (e.g., *.contoso.com): Matches contoso.com, any subdomain, and any site. Does not match unspecified domains like anysubdomain.contoso.com.AU.
3. For full domain name (e.g., www.contoso.com): Matches only www.contoso.com. Does not match unspecified domains or subdomains like anysubdomain.contoso.com.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Service Domains. 2. Verify that the configured domain patterns (e.g., contoso.com, *.contoso.com, www.contoso.com) are listed exactly as intended. 3. For each pattern, confirm the match behavior by reviewing the official documentation at https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings. 4. Use a test file upload or copy operation to a sensitive service domain to ensure DLP policies trigger as expected for the specified patterns.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Service Domains, remove or edit any incorrectly added domain patterns. 2. Restore the previous list of service domains from a backup or known good configuration. 3. Verify that the corrected list no longer includes unintended domains or patterns. 4. Test DLP policy enforcement to confirm that only the intended domains are affected.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
