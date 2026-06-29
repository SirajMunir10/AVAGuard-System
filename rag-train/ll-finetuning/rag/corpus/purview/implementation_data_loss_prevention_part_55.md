# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure Allow/Block cloud service domains and Unallowed browsers list in DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Browser and domain restrictions to sensitive data

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure the Allow/Block cloud service domains and the Unallowed browsers list.
2. When a user attempts to upload a protected file to a cloud service domain or access it from an unallowed browser, configure the policy action to Audit only, Block with override, or Block the activity.

## Validation
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Data Loss Prevention > Policies and select the DLP policy that was configured.
3. Click 'Edit policy' and go to the 'Rules' section.
4. For each rule that includes 'Block cloud service domains' or 'Unallowed browsers' conditions, verify the configured actions (Audit only, Block with override, or Block).
5. Use the DLP Alerts dashboard to confirm no unexpected blocks or overrides occurred for legitimate users.
6. Optionally, run a test by attempting to upload a sensitive file to a blocked cloud service domain from an unallowed browser and confirm the expected action (e.g., block notification) appears.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies.
2. Select the DLP policy that was modified and click 'Edit policy'.
3. Go to the 'Rules' section and locate the rule(s) that contain the 'Block cloud service domains' or 'Unallowed browsers' conditions.
4. Remove or disable those conditions by unchecking the corresponding checkboxes or deleting the condition blocks.
5. Alternatively, change the action for those conditions to 'Audit only' to stop blocking while retaining visibility.
6. Save the policy and confirm the changes are applied by reviewing the policy status.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
