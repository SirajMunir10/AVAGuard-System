# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure additional options for rule processing and priority in a DLP policy with multiple rules?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with multiple rules for Exchange and Teams locations

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the DLP policy editing interface.
2. Locate the 'Additional options' section when editing a rule.
3. Configure rule processing behavior: choose whether to stop processing further rules if there's a match to the rule you're editing.
4. Set the priority for evaluation of the rule.
5. Note: This is only supported for Exchange and Teams locations.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy with multiple rules. 3. Click 'Edit policy' and then 'Edit' for the rule where you configured additional options. 4. Verify that the 'Additional options' section displays the configured rule processing behavior (e.g., 'Stop processing more rules' is checked or unchecked) and the priority order (e.g., rule rank number). 5. Confirm that the rule priority order matches the intended evaluation sequence by reviewing the rule list in the policy editor. 6. For Exchange and Teams locations, send a test message containing sensitive information that matches the rule and verify that the rule is triggered as expected and that subsequent rules are processed or stopped according to the configured behavior.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy with the modified rule. 3. Click 'Edit policy' and then 'Edit' for the rule where additional options were changed. 4. In the 'Additional options' section, revert the rule processing behavior to the original setting (e.g., uncheck 'Stop processing more rules' if it was enabled, or check it if it was disabled). 5. Adjust the rule priority back to its original rank by selecting the appropriate priority number from the dropdown. 6. Click 'Save' to apply the rollback changes. 7. Verify that the rule list order and processing behavior match the pre-change state by reviewing the policy editor.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
