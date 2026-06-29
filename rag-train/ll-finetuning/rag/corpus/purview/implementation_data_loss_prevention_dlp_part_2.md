# Implementation: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to configure complex DLP policy conditions for identifying HIPAA-related content using grouped conditions and boolean operators?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview DLP policy with sensitive information types (SITs) and keyword lists

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Identify content that contains specific types of sensitive information, such as a U.S. Social Security Number or Drug Enforcement Agency (DEA) Number.
2. Identify content that is more difficult to identify, such as communications about a patient's care or descriptions of medical services provided, by matching keywords from large keyword lists like the International Classification of Diseases (ICD-9-CM or ICD-10-CM).
3. Group conditions using logical operators (AND, OR) between the groups. For the U.S. Health Insurance Act (HIPAA), group conditions as follows: the first group contains the SITs that identify an individual and the second group contains the SITs that identify medical diagnosis.
4. Use boolean operators (AND, OR, NOT) to define a rule by stating what should be included and then defining exclusions in a different group joined to the first by a NOT.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the newly created HIPAA DLP policy and click 'Edit policy'. 3. Under 'Locations', confirm the policy is applied to the intended workloads (e.g., Exchange, SharePoint, OneDrive, Teams). 4. Under 'Rules', expand the rule containing grouped conditions. 5. Verify that the first condition group includes SITs such as 'U.S. Social Security Number' and 'Drug Enforcement Agency (DEA) Number'. 6. Verify that the second condition group includes SITs for medical diagnosis (e.g., 'International Classification of Diseases (ICD-9-CM)' or 'ICD-10-CM'). 7. Confirm that the groups are joined by the 'AND' operator. 8. If an exclusion group exists, verify it is joined by the 'NOT' operator. 9. Use the 'Test' feature (if available) to simulate a message containing HIPAA data and confirm the policy triggers as expected. 10. Review the policy's audit logs for any matches or alerts.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the HIPAA DLP policy and click 'Edit policy'. 3. Under 'Rules', select the rule with the complex conditions. 4. Remove or modify the grouped conditions to revert to a simpler configuration (e.g., remove the NOT group or change AND to OR). 5. Alternatively, delete the entire rule and recreate it using a simpler condition set. 6. If the policy was newly created, delete the policy entirely. 7. Save the changes and confirm the policy is no longer enforcing the complex conditions. 8. Monitor for any residual policy matches or alerts and clear them if necessary.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
