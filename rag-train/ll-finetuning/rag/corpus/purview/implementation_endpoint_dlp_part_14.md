# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I apply restrictions to specific activities for apps in a restricted app group in endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy, File activities for apps in restricted app groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In your existing or new endpoint DLP policy, locate the File activities for apps in restricted app groups setting.
2. Select 'Apply restrictions to a specific activity'.
3. Choose a default action (Audit only, Block, or Block with override) for activities: Copy to clipboard, Copy to a USB removable drive, Copy to a network drive, and Print.

## Validation
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Data Loss Prevention > Policies and select the endpoint DLP policy you modified.
3. Click 'Edit policy' and go to the 'Locations' step to confirm the policy is still assigned to the correct devices.
4. Proceed to the 'Rules' step, select the rule that contains the 'File activities for apps in restricted app groups' setting.
5. Click 'Edit rule' and verify that under 'File activities for apps in restricted app groups' the option 'Apply restrictions to a specific activity' is selected.
6. Confirm that for each activity (Copy to clipboard, Copy to a USB removable drive, Copy to a network drive, Print) the chosen default action (Audit only, Block, or Block with override) is set as intended.
7. Save the rule and policy, then use the 'Test' feature (if available) or monitor DLP alerts and reports to ensure the restrictions are being enforced as expected.

## Rollback
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Data Loss Prevention > Policies and select the endpoint DLP policy you modified.
3. Click 'Edit policy' and go to the 'Rules' step, then select the rule containing the changed settings.
4. Click 'Edit rule' and locate the 'File activities for apps in restricted app groups' setting.
5. Change the option from 'Apply restrictions to a specific activity' back to the previous setting (e.g., 'Audit only' for all activities, or remove the custom restrictions).
6. Alternatively, if you need to revert the entire policy, delete the rule or disable the policy temporarily.
7. Save the rule and policy, then monitor DLP alerts and reports to confirm the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
