# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I name and define general information for a custom analytics rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure or Defender portal
- **Configuration:** Microsoft Sentinel onboarded to Defender portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enter a unique name for your rule. This field supports plain text only. Any URLs included in the name should follow the percent-encoding format for them to display properly.
2. Enter a free-text description for your rule. If Microsoft Sentinel is onboarded to the Defender portal, this field supports plain text only. Any URLs included in the description should follow the percent-encoding format for them to display properly.
3. Select a severity: Informational (no impact), Low (minimal immediate impact), Medium (limited scope or additional activity required), or High (wide ranging access or impact).
4. Choose MITRE ATT&CK tactics and techniques from the drop-down list. Multiple selections are allowed.
5. Set the rule status: Enabled (runs immediately or at scheduled date/time) or Disabled (created but does not run; enable later from Active rules tab).

## Validation
1. In Microsoft Sentinel (Azure portal or Defender portal), navigate to Analytics > Active rules. 2. Locate the custom rule by its unique name. 3. Verify the rule name displays correctly (no encoding issues). 4. Open the rule and confirm the description is plain text and URLs are percent-encoded. 5. Check the severity matches the selected value. 6. Confirm MITRE ATT&CK tactics/techniques are listed as chosen. 7. Verify the rule status is Enabled or Disabled as intended. 8. If Enabled, confirm the rule is listed as Active and has a next run time.

## Rollback
1. In Microsoft Sentinel (Azure portal or Defender portal), navigate to Analytics > Active rules. 2. Select the custom rule. 3. Click 'Edit' to modify the rule. 4. Revert the rule name to the previous value (ensure plain text and percent-encoding for URLs). 5. Revert the description to the previous plain text. 6. Change the severity back to the original setting. 7. Remove any newly added MITRE ATT&CK tactics/techniques and reapply the original selections. 8. Set the rule status back to the original (Enabled or Disabled). 9. Click 'Review and create' then 'Save' to apply changes.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
