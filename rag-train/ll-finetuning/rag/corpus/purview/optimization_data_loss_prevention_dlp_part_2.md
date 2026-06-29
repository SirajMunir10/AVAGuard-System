# Optimization: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Optimization

## Scenario / Query
A Microsoft 365 tenant has enabled default DLP policies for financial and medical data, but the DLP reports show a high number of false positive matches. How can an administrator optimize the DLP policy rules to reduce false positives while maintaining compliance coverage?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Default DLP policies for U.S. Financial Data and U.S. Health Records are enabled, with no custom tuning applied.

## Symptoms
- DLP reports show a large volume of policy matches that are not actual sensitive data exposures
- End users receive frequent policy tips for benign content
- Security team spends excessive time reviewing false positive alerts

## Error Codes
N/A

## Root Causes
1. Default DLP policies use broad classification rules that may trigger on common patterns (e.g., credit card numbers in test data)
2. No exclusion rules or confidence level adjustments have been configured
3. Policy rules are not scoped to specific locations or conditions

## Remediation Steps
1. Review the default DLP policies in the Microsoft Purview compliance portal (https://compliance.microsoft.com/datalossprevention)
2. Adjust the confidence level threshold for each sensitive info type to reduce low-confidence matches
3. Add exclusion rules for known false positive patterns (e.g., test environments, specific file names)
4. Scope policies to specific SharePoint sites, OneDrive accounts, or Exchange distribution groups as needed
5. Use the DLP test mode (simulation) to evaluate changes before enforcing

## Validation
Monitor DLP reports for a reduction in false positives while ensuring no genuine sensitive data exposures are missed. Use the DLP simulation mode to validate rule changes.

## Rollback
Revert any changed policy rules to their previous settings via the policy edit page in the Purview compliance portal. If simulation mode was used, disable it.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-get-started>
