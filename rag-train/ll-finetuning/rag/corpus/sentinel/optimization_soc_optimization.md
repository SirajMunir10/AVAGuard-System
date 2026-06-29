# Optimization: SOC Optimization

**Domain:** Sentinel
**Subdomain:** SOC Optimization
**Incident Type:** Optimization

## Scenario / Query
How do I find and install recommended analytics rules from a SOC optimization recommendation in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Azure portal or Microsoft Defender portal
- **Configuration:** SOC optimization page

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the details of a SOC optimization recommendation in the SOC optimization page.
2. Scroll to the bottom of the optimization details tab.
3. Select 'Go to Content hub' to find and install the recommended rules specific to that recommendation.

## Validation
1. Navigate to the SOC optimization page in Microsoft Sentinel (Azure portal or Microsoft Defender portal).
2. Locate the specific recommendation you acted on and verify its status shows as 'Completed' or 'Installed'.
3. Go to the Content hub and confirm the recommended analytics rule(s) are now listed as 'Installed'.
4. In the Analytics blade, verify the rule is enabled and appears in the active rules list.
5. Optionally, run a sample query to confirm the rule is generating alerts as expected.

## Rollback
1. In the Analytics blade, locate the installed rule, select it, and choose 'Disable' or 'Delete' to remove it.
2. If the rule was part of a solution, go to the Content hub, find the solution, and select 'Uninstall' to remove all associated content.
3. Return to the SOC optimization page and verify the recommendation status reverts to 'Not started' or 'Pending'.
4. Confirm no alerts from the rule appear in the Incidents queue.
5. If needed, restore any previous configuration by re-enabling any rules that were disabled during the installation.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
