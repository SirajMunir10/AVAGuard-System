# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to implement a DLP policy using the U.S. Gramm-Leach-Bliley Act (GLBA) Enhanced template to detect credit card number, U.S. bank account number, U.S. Individual Taxpayer Identification Number (ITIN), U.S. social security number (SSN), U.S./U.K. passport number, U.S. driver's license number, All Full Names, and U.S. Physical Addresses?

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
1. Select the U.S. Gramm-Leach-Bliley Act (GLBA) Enhanced policy template from the list of predefined templates.
2. The template includes detection for: Credit card number, U.S. bank account number, U.S. Individual Taxpayer Identification Number (ITIN), U.S. social security number (SSN), U.S./U.K. passport number, U.S. driver's license number, All Full Names, U.S. Physical Addresses.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Confirm the new DLP policy appears in the list with the name derived from the 'U.S. Gramm-Leach-Bliley Act (GLBA) Enhanced' template. 3. Select the policy and verify that the configured sensitive info types include: Credit Card Number, U.S. Bank Account Number, U.S. Individual Taxpayer Identification Number (ITIN), U.S. Social Security Number (SSN), U.S./U.K. Passport Number, U.S. Driver's License Number, All Full Names, and U.S. Physical Addresses. 4. Use the Test-DlpPolicy cmdlet in Security & Compliance PowerShell to simulate a message containing sample data for each sensitive info type and confirm the policy triggers the expected action (e.g., block, notify).

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the newly created GLBA Enhanced policy. 2. Click 'Delete policy' and confirm deletion. 3. Alternatively, if the policy should be retained but disabled, edit the policy and set its status to 'Disabled'. 4. Verify that no DLP policy rules from this template are actively enforcing by checking the policy list and confirming the policy is removed or disabled.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
