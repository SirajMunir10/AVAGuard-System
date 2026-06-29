# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to implement a DLP policy using the U.K. Access to Medical Reports Act template to detect U.K. national health service number?

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
1. Select the U.K. Access to Medical Reports Act policy template from the list of predefined templates.
2. The template includes detection for: U.K. national health service number.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Locate the policy created from the 'U.K. Access to Medical Reports Act' template. 3. Verify the policy status is 'Enabled'. 4. Use the DLP policy test functionality or simulate a document containing a valid U.K. National Health Service number (e.g., '123 456 7890') to confirm the policy triggers an alert or blocks the action as configured. 5. Check the DLP activity explorer for matching events.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the policy created from the 'U.K. Access to Medical Reports Act' template. 2. Click 'Disable policy' to stop enforcement immediately. 3. Alternatively, delete the policy by selecting 'Delete policy' and confirming. 4. If the policy was part of a broader deployment, restore any previous DLP policy configuration from backup or reapply the prior policy settings.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
