# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I configure a playbook to parse custom details from an incident trigger using a sample JSON payload?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel playbook with incident trigger

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. From the list, in the incident trigger section, find and select Alert Custom Details.
2. This selection automatically adds a For each loop around Parse JSON because an incident contains an array of alerts.
3. In the Parse JSON information pane, select Use sample payload to generate schema.
4. In the Enter or paste a sample JSON payload box, provide a sample payload, and select Done.
5. Find a sample payload by looking in Log Analytics for another instance of this alert, and then copying the custom details object, which you can find under Extended Properties.
6. To access Log Analytics data, go either to the Logs page in the Azure portal or the Advanced hunting page in the Defender portal.

## Validation
1. Open the playbook in Azure Logic Apps Designer. 2. Expand the 'For each' loop that was automatically added. 3. Verify that the 'Parse JSON' action is inside the loop. 4. Click on 'Parse JSON' and confirm that the 'Schema' field contains a valid JSON schema (not empty). 5. Optionally, run the playbook on a test incident and check the 'Parse JSON' action's outputs to ensure custom details are correctly parsed.

## Rollback
1. In the Logic Apps Designer, delete the 'Parse JSON' action and the surrounding 'For each' loop. 2. Re-add the 'Parse JSON' action directly under the trigger (without the loop). 3. Manually enter the JSON schema or use 'Use sample payload to generate schema' again with a corrected payload. 4. Save the playbook.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
