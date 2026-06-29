# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I configure alert grouping for a custom analytics rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace, custom analytics rule

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set the time frame within which the similar or recurring alerts are grouped together. Alerts outside this time frame generate a separate incident or set of incidents.
2. Choose how alerts are grouped together: Group alerts into a single incident if all the entities match (recommended), Group all alerts triggered by this rule into a single incident, or Group alerts into a single incident if the selected entities and details match.
3. If an incident is resolved and closed, and later on another alert is generated that should belong to that incident, set 'Re-open closed matching incidents' to Enabled if you want the closed incident re-opened, or Disabled if you want the alert to create a new incident. This option isn't available when Microsoft Sentinel is onboarded to the Microsoft Defender portal.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Analytics > Active rules and select the custom analytics rule. 2. Click Edit. 3. Under 'Incident settings', verify that the 'Alert grouping' configuration matches the intended settings: the time frame for grouping, the grouping method (e.g., 'Group alerts into a single incident if all the entities match'), and the 'Re-open closed matching incidents' toggle (Enabled or Disabled). 4. Save the rule if any changes were made. 5. Trigger a test alert that meets the grouping criteria and confirm that alerts are grouped into incidents as configured. 6. Check the Incidents blade to ensure incidents are created or re-opened according to the grouping and re-open settings.

## Rollback
1. In the Microsoft Sentinel workspace, navigate to Analytics > Active rules and select the custom analytics rule. 2. Click Edit. 3. Under 'Incident settings', revert the 'Alert grouping' configuration to the previous values: set the time frame, grouping method, and 'Re-open closed matching incidents' toggle to the original settings. 4. Save the rule. 5. If the rule was newly created with the problematic grouping, delete the rule and restore from a backup or recreate using the previous known-good configuration. 6. Verify that incident generation returns to the expected behavior by reviewing recent incidents.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
