# Implementation: Microsoft Sentinel

**Domain:** Sentinel
**Subdomain:** Microsoft Sentinel
**Incident Type:** Implementation

## Scenario / Query
How do I automate threat response with playbooks in Microsoft Sentinel after integrating with Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Sentinel, Microsoft Defender XDR components

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Refer to the documentation on Automate threat response with playbooks in Microsoft Sentinel.
2. Access playbooks from the Microsoft Sentinel GitHub Repository.

## Validation
1. In the Azure portal, navigate to Microsoft Sentinel > Automation > Playbooks. Confirm that the playbook you deployed appears in the list and its status is 'Enabled'.
2. Open the playbook and verify that the trigger condition (e.g., 'When a Microsoft Defender XDR alert is created') is correctly configured.
3. Trigger a test alert from Microsoft Defender XDR (e.g., create a simulated alert) and confirm that the playbook runs automatically by checking the playbook's run history in Microsoft Sentinel > Automation > Playbooks > select the playbook > 'Run history'.
4. Verify that the playbook's actions (e.g., creating an incident, sending an email, or updating a ticket) completed successfully by reviewing the output of each action in the run history.

## Rollback
1. In the Azure portal, navigate to Microsoft Sentinel > Automation > Playbooks.
2. Select the playbook you deployed and click 'Disable' to stop it from triggering automatically.
3. If the playbook created any resources (e.g., Logic Apps connections, custom APIs), delete those resources from their respective resource groups.
4. Remove the playbook from Microsoft Sentinel by selecting it and clicking 'Delete', confirming the deletion.
5. If the playbook was imported from the GitHub repository, note that the source code remains in your GitHub fork; you can delete the fork or revert the commit if needed.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
