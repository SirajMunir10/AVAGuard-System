# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
What actions automatically resume after a user allows a DLP policy override?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy with 'Block with override' or 'Allow' action

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Once allowed, Endpoint DLP will automatically resume for actions including 'Copy to a network share', 'Copy to a removable USB device', and 'Print'
2. For other actions, users will need to repeat the process after clicking 'Allow' to bypass the policy

## Validation
1. On a test endpoint, trigger a DLP policy that blocks 'Copy to a network share' with an override option. 2. When prompted, click 'Allow' to override the block. 3. Immediately attempt the same 'Copy to a network share' action again. 4. Verify that the action completes without a policy block, confirming automatic resumption. 5. Repeat steps 1-4 for 'Copy to a removable USB device' and 'Print' actions. 6. For a different action (e.g., 'Copy to clipboard'), trigger the policy, click 'Allow', then attempt the same action again. 7. Confirm that the user is prompted again to override, indicating the action is not automatically resumed.

## Rollback
1. If automatic resumption for 'Copy to a network share', 'Copy to a removable USB device', or 'Print' is not desired, reconfigure the Endpoint DLP policy to remove the 'Block with override' action for those activities. 2. Alternatively, set the policy to 'Block' without override for those actions. 3. If automatic resumption is causing unintended data exfiltration, temporarily disable the policy by setting its status to 'Disabled' in the Microsoft Purview compliance portal. 4. Review DLP activity reports to identify any unauthorized transfers that occurred during the automatic resumption period and take corrective action (e.g., revoke access, initiate data recovery).

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
