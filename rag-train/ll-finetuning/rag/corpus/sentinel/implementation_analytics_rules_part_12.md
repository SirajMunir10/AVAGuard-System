# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I configure alert grouping in a Microsoft Sentinel analytics rule to generate a single incident from up to 150 similar or recurring alerts?

## Environment Context
- **Tenant Type:** Microsoft Sentinel workspace
- **Configuration:** Analytics rule alert grouping settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Alert grouping section, set 'Group related alerts, triggered by this analytics rule, into incidents' to Enabled.
2. Set the time frame within which similar or recurring alerts are grouped together using 'Limit the group to alerts created within the selected time frame'.
3. Choose how alerts are grouped by selecting one of the following options: 'Group alerts into a single incident if all the entities match' (recommended), 'Group all alerts triggered by this rule into a single incident', or 'Group alerts into a single incident if the selected entities and details match'.
4. Optionally, set 'Re-open closed matching incidents' to Enabled if you want closed incidents to be re-opened when a new related alert is generated, or Disabled to create a new incident.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under Configuration, select Analytics. 3. Locate and click the analytics rule you configured. 4. On the rule details page, select Edit. 5. Go to the Alert grouping step. 6. Verify that 'Group related alerts, triggered by this analytics rule, into incidents' is set to Enabled. 7. Confirm the time frame selected under 'Limit the group to alerts created within the selected time frame' matches your intended grouping window. 8. Check that the grouping option (e.g., 'Group alerts into a single incident if all the entities match') is correctly chosen. 9. Verify the 'Re-open closed matching incidents' setting is as desired (Enabled or Disabled). 10. Review and save the rule if any changes were needed. 11. Optionally, trigger test alerts to confirm that alerts are grouped into a single incident as expected.

## Rollback
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under Configuration, select Analytics. 3. Locate and click the analytics rule you modified. 4. On the rule details page, select Edit. 5. Go to the Alert grouping step. 6. Set 'Group related alerts, triggered by this analytics rule, into incidents' to Disabled to revert to default behavior (each alert generates its own incident). 7. Alternatively, adjust the time frame or grouping option back to the previous settings. 8. If you enabled 'Re-open closed matching incidents', set it to Disabled. 9. Review and save the rule. 10. Monitor incident creation to ensure alerts are no longer grouped as before.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
