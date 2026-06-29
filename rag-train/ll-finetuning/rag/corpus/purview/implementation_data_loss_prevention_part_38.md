# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure conditions in a Microsoft Purview DLP policy to match sensitive content based on context and risk level?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy rule conditions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define conditions to specify what items to look for and the context in which they are used.
2. Use conditions to assign different actions to different risk levels (e.g., sensitive content shared internally vs. externally).
3. Select the 'Content contains' condition for all locations.
4. Select multiple instances of each content type and refine using 'Any of these' (logical OR) or 'All of these' (logical AND) operators.
5. Choose from sensitive information types, sensitivity labels, retention labels, or Trainable Classifiers.
6. For sensitivity labels and retention labels, the rule will only look for their presence.
7. Adjust the predefined confidence level for SITs if needed.
8. Define maximum unique instance count parameters for SITs (note: duplicate SIT words across different attachments in a single email are counted only once toward the unique count).
9. Optionally, integrate Adaptive Protection by configuring Insider risk level for Adaptive Protection as a condition for Exchange Online, Devices, Teams, and unmanaged cloud apps locations.
10. Select from available Insider risk levels: Elevated risk level, Moderate risk level, Minor risk level.
11. Note: If multiple locations are selected, only common conditions are available.
12. DLP policies for Exchange scan non-system generated emails and journaling emails.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was configured. 3. Click 'Edit policy' and review the 'Rules' section. 4. Verify that the rule contains the 'Content contains' condition with the expected sensitive information types, sensitivity labels, retention labels, or trainable classifiers. 5. Confirm that the logical operators (Any of these / All of these) are set as intended. 6. For each sensitive information type, check that the confidence level and unique instance count parameters match the desired configuration. 7. If Adaptive Protection was integrated, verify that the 'Insider risk level for Adaptive Protection' condition is present and set to the correct risk level (Elevated, Moderate, or Minor). 8. Use the 'Test' feature in the DLP policy to simulate a message containing the defined sensitive content and confirm that the policy triggers the expected action (e.g., block, notify). 9. Review DLP alerts and reports in the compliance portal to ensure the policy is detecting and acting on the sensitive content as configured.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was modified. 3. Click 'Edit policy' and go to the 'Rules' section. 4. Remove or revert any newly added conditions (e.g., delete the 'Content contains' condition, remove added sensitive information types, or reset confidence level and instance count to previous values). 5. If Adaptive Protection was added, remove the 'Insider risk level for Adaptive Protection' condition. 6. If logical operators were changed, revert them to the original setting (e.g., change from 'All of these' back to 'Any of these'). 7. Save the policy and confirm that the previous behavior is restored by testing with the same sample content used during validation. 8. Monitor DLP alerts and reports to ensure no unintended policy actions are occurring.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
