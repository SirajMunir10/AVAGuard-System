# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure business justification options in policy tips for endpoint DLP?

## Environment Context
- **Tenant Type:** Purview
- **Configuration:** Endpoint DLP policy with Block with override setting

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose from one of the following options: Show default options and custom text box, Only show default options, Only show custom text box.
2. To create customized options, select Customize the options drop-down menu and enter up to five customized options such as: 'This is part of an established business workflow', 'My manager has approved this action', 'Urgent access required; I'll notify my manager separately', 'The information in these files is not sensitive', 'Other'.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP policies. 2. Select the policy configured with 'Block with override' and click 'Edit'. 3. Under 'User notifications and overrides', verify that 'Configure business justification' is enabled and the chosen option (e.g., 'Show default options and custom text box') is selected. 4. If custom options were added, confirm they appear in the drop-down list. 5. On a test endpoint, trigger the DLP rule and confirm the policy tip displays the business justification options as configured.

## Rollback
1. In the same policy edit flow, under 'User notifications and overrides', set 'Configure business justification' to 'Off' or revert to the previous option (e.g., 'Only show default options'). 2. Remove any custom options by clearing the 'Customize the options drop-down menu' field. 3. Save the policy and wait for propagation (up to 24 hours). 4. Verify on a test endpoint that the policy tip no longer shows the custom business justification options.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
