# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I temporarily suppress a custom analytics rule after an alert is generated in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel Analytics Rule

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Turn the 'Stop running query after alert is generated' setting On.
2. Set 'Stop running query for' to the desired suppression time (up to 24 hours).

## Validation
1. In Microsoft Sentinel, navigate to Analytics > Active rules. 2. Select the custom analytics rule. 3. In the rule details pane, confirm that 'Stop running query after alert is generated' is set to On. 4. Confirm that 'Stop running query for' shows the desired suppression time (e.g., 5 hours). 5. Generate a test alert by triggering the rule's query conditions. 6. Verify that after the alert is generated, the rule stops running the query for the configured suppression period (e.g., no new alerts from that rule during the suppression window).

## Rollback
1. In Microsoft Sentinel, navigate to Analytics > Active rules. 2. Select the custom analytics rule. 3. In the rule details pane, set 'Stop running query after alert is generated' to Off. 4. Click 'Review and update' to save the change. 5. Confirm that the rule resumes running its query continuously without suppression.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
