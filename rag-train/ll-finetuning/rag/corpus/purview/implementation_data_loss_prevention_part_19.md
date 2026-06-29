# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to implement a DLP policy using the Canada Health Information Act (HIA) template to detect Canada passport number, Canada social insurance number, Canada health service number, and Canada Personal Health Identification Number?

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
1. Select the Canada Health Information Act (HIA) policy template from the list of predefined templates.
2. The template includes detection for: Canada passport number, Canada social insurance number, Canada health service number, Canada Personal Health Identification Number.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Confirm the DLP policy created from the Canada Health Information Act (HIA) template is listed with status 'Enabled'. 3. Open the policy and verify that the 'Locations' include the intended workloads (e.g., Exchange email, SharePoint sites, OneDrive accounts). 4. Under 'Rules', confirm that the rule named 'Canada Health Information Act (HIA)' is present and its 'Conditions' include sensitive info types: Canada passport number, Canada social insurance number, Canada health service number, Canada Personal Health Identification Number. 5. Use the 'Test' feature (if available) to simulate a message or document containing one of these sensitive info types and verify that the policy triggers the expected action (e.g., block, notify).

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the DLP policy created from the Canada Health Information Act (HIA) template. 2. Click 'Delete policy' and confirm deletion. 3. Alternatively, if the policy should be retained but disabled, set the policy status to 'Disabled' and save. 4. If the policy was created via PowerShell, use the Remove-DlpCompliancePolicy cmdlet: Remove-DlpCompliancePolicy -Identity 'Canada HIA Policy'. 5. Verify removal by running Get-DlpCompliancePolicy and confirming the policy is no longer listed.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
