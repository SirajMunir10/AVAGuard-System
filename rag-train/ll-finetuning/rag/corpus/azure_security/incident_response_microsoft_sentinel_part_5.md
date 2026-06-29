# Incident Response: Microsoft Sentinel

**Domain:** Azure
**Subdomain:** Microsoft Sentinel
**Incident Type:** Incident Response

## Scenario / Query
A security operations analyst notices that a Microsoft Sentinel incident for 'MFA Denied' has been automatically generated but no assigned owner or status change has occurred. The analyst needs to understand how to triage, investigate, and remediate this incident using built-in Microsoft Sentinel capabilities.

## Environment Context
- **Tenant Type:** Enterprise (Azure AD P2, Microsoft Sentinel enabled)
- **Configuration:** Microsoft Sentinel analytics rule 'MFA Denied' enabled; default incident configuration; no automation rules yet configured for incident owner assignment

## Symptoms
- Incident titled 'MFA Denied' appears in Microsoft Sentinel with status 'New' and no assigned owner
- Alert details show multiple failed MFA attempts from a single user within a short time window
- No automated response or playbook has been triggered

## Error Codes
N/A

## Root Causes
1. No automation rule configured to assign incident owner or change status upon creation
2. Analytics rule 'MFA Denied' is enabled but lacks a linked playbook for automated response

## Remediation Steps
1. Open the incident in Microsoft Sentinel and review the alert details, entities, and timeline
2. Manually assign the incident to a senior analyst and change status to 'Active'
3. Use the built-in investigation graph to explore related entities and events
4. Create an automation rule that automatically assigns incidents of this type to a specific security group and sets status to 'Active'
5. Optionally, create a playbook (Azure Logic App) that triggers on this incident to block the user or require re-authentication, then attach it to the analytics rule

## Validation
Verify that the incident status is updated to 'Active' and that the assigned owner appears in the incident details. If a playbook was attached, confirm it executed successfully by checking the playbook run history.

## Rollback
Remove the automation rule or playbook association from the analytics rule if the automated behavior is no longer desired. Manually reassign incidents if needed.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents>
- <https://learn.microsoft.com/en-us/azure/sentinel/automate-responses-with-playbooks>
