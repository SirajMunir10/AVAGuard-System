# Implementation: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
What are the available DLP actions for Windows and macOS devices?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with Devices location

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For onboarded Windows devices, you can set actions to: Allow, Audit only, Block with override, or Block.
2. For onboarded macOS devices, you can set actions to: Audit only, Block with override, or Block.
3. When Block is selected: User related activity is blocked, and auditing is enabled. Admins may optionally see alerts.
4. When Block with override is selected: This option acts as a standard block but permits users to bypass it.

## Validation
1. Confirm that the DLP policy includes the 'Devices' location and is applied to the intended user/device groups.
2. For Windows devices: In the DLP policy rule, verify that the action for a sensitive info type is set to 'Allow', 'Audit only', 'Block with override', or 'Block' as intended.
3. For macOS devices: In the same policy rule, verify that the action is set to 'Audit only', 'Block with override', or 'Block' (not 'Allow').
4. Use the Microsoft Purview compliance portal > Data Loss Prevention > Policies > select the policy > Edit policy > Review the actions under each rule.
5. Optionally, simulate a DLP event on a test device to confirm the action behaves as expected (e.g., block, audit, or allow with override).

## Rollback
1. If the remediation caused unintended blocking or auditing, edit the DLP policy rule and change the action back to the previous setting (e.g., from 'Block' to 'Audit only' or 'Allow').
2. For Windows devices: If 'Block with override' was set and users cannot bypass, revert to 'Audit only' or 'Allow'.
3. For macOS devices: If 'Block' was set and it is too restrictive, change to 'Audit only' or 'Block with override'.
4. Save the policy and allow up to 1 hour for changes to propagate.
5. Verify the rollback by checking the policy actions in the compliance portal and testing on a device.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
