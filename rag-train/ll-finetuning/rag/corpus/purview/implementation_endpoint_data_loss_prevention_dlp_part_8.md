# Implementation: Endpoint Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to use the Copy to clipboard condition in DLP policy to block or audit copying from protected files?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Copy to clipboard condition to detect when a user copies information from a protected file to the clipboard.
2. Select one of the following actions: Block, Block with override, or Audit.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was modified. 3. Under 'Locations', confirm the policy applies to 'Devices' (Endpoint). 4. Under 'Rules', select the rule containing the 'Copy to clipboard' condition. 5. Verify that the condition is set to 'Content is copied from a protected file to clipboard' (or similar). 6. Confirm the action is set to one of: 'Block', 'Block with override', or 'Audit'. 7. On a test Windows endpoint, open a protected file (e.g., labeled as confidential) and attempt to copy text to clipboard. 8. Verify that the configured action triggers (e.g., copy is blocked, or an audit event appears in Activity Explorer). 9. Check Activity Explorer for the corresponding DLP rule match event.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was modified. 3. Under 'Rules', select the rule containing the 'Copy to clipboard' condition. 4. Remove the 'Copy to clipboard' condition from the rule, or change the action to 'Audit' (least restrictive) to minimize disruption. 5. Alternatively, disable the rule entirely by toggling it off. 6. Save the policy and allow up to 1 hour for changes to propagate to endpoints. 7. Verify on a test endpoint that copying from protected files is no longer blocked or audited as per the original behavior.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
