# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I create a scheduled query rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure or Defender portal
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to the Analytics page in Microsoft Sentinel to create a scheduled analytics rule.
2. For Microsoft Sentinel in the Defender portal, select Microsoft Sentinel > Configuration > Analytics.
3. For Microsoft Sentinel in the Azure portal, under Configuration, select Analytics.
4. Select +Create and select Scheduled query rule.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Analytics > Active rules. 2. Locate the newly created scheduled query rule by name. 3. Confirm the rule status is 'Enabled'. 4. Select the rule and verify the rule settings (e.g., query, schedule, alert details) match the intended configuration. 5. Optionally, run the rule's query manually in Log Analytics to confirm it returns expected results.

## Rollback
1. In the Microsoft Sentinel workspace, navigate to Analytics > Active rules. 2. Select the scheduled query rule to be removed. 3. Click 'Delete' and confirm the deletion. 4. If the rule was created as part of a deployment script or template, redeploy the previous version of the template or run the script with the rule definition removed.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
