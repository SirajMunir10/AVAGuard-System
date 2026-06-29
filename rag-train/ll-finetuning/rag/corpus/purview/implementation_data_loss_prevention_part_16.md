# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to implement a DLP policy using the Australia Financial Data template to detect SWIFT code, Australia tax file number, Australia bank account number, and credit card number?

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
1. Select the Australia Financial Data policy template from the list of predefined templates.
2. The template includes detection for: SWIFT code, Australia tax file number, Australia bank account number, Credit card number.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Confirm the policy named 'Australia Financial Data' (or custom name) is listed with Status 'On'. 3. Open the policy and verify the following sensitive info types are included: SWIFT Code, Australia Tax File Number, Australia Bank Account Number, Credit Card Number. 4. Use the 'Test' feature in the policy to simulate a message containing sample data for each type and confirm detection triggers. 5. Check the Activity explorer for any matched events after the policy is enforced.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the policy. 2. Click 'Disable policy' to stop enforcement immediately. 3. Alternatively, delete the policy by selecting 'Delete policy' and confirming. 4. If the policy was created from a template, note that no default backup exists; re-create from template if needed. 5. Verify no residual policy rules remain by checking the policy list.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
