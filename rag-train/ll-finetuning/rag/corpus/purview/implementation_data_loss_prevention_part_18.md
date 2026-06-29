# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to implement a DLP policy using the Australia Health Records Act (HRIP Act) Enhanced template to detect Australia tax file number, Australia medical account number, All Full Names, All Medical Terms And Conditions, and Australia Physical Addresses?

## Environment Context
- **Tenant Type:** Purview
- **Configuration:** DLP policy templates

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the Australia Health Records Act (HRIP Act) Enhanced policy template from the list of predefined templates.
2. The template includes detection for: Australia tax file number, Australia medical account number, All Full Names, All Medical Terms And Conditions, Australia Physical Addresses.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Confirm a DLP policy exists with the name derived from 'Australia Health Records Act (HRIP Act) Enhanced' template. 3. Open the policy and verify the 'Locations' tab includes the intended workloads (e.g., Exchange, SharePoint, OneDrive, Teams). 4. Under 'Rules', confirm the rule named 'Australia Health Records Act (HRIP Act) Enhanced' is present and enabled. 5. Select the rule and click 'Edit' > 'Conditions' to verify that the following sensitive info types are listed: Australia Tax File Number, Australia Medical Account Number, All Full Names, All Medical Terms And Conditions, Australia Physical Addresses. 6. Use the 'Test' feature (if available) to simulate a document containing sample data for each sensitive info type and confirm the policy triggers an alert or blocks the content as configured.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Locate the policy created from the 'Australia Health Records Act (HRIP Act) Enhanced' template. 3. Select the policy and click 'Delete policy'. 4. Confirm deletion when prompted. 5. Alternatively, to disable without deleting: open the policy, set 'Status' to 'Off', and save. 6. If the policy was deployed via PowerShell, use Remove-DlpCompliancePolicy -Identity "<PolicyName>" to delete, or Set-DlpCompliancePolicy -Identity "<PolicyName>" -Enabled $false to disable.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
