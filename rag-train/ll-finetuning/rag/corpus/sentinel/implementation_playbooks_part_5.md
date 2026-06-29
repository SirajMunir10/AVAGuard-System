# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I create a playbook in Microsoft Sentinel using a Standard logic app for virtual network integration?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Standard logic app type, virtual network integration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If your playbooks need access to protected resources that are inside or connected to an Azure virtual network, create a Standard logic app workflow.
2. Standard workflows run in single-tenant Azure Logic Apps and support using private endpoints for inbound traffic so that your workflows can communicate privately and securely with virtual networks.
3. Standard workflows also support virtual network integration for outbound traffic.

## Validation
1. In the Azure portal, navigate to your Standard logic app resource. 2. Under 'Settings', select 'Networking'. 3. Confirm that 'Virtual network integration' is enabled and shows the correct virtual network and subnet. 4. Under 'Settings', select 'Identity' and verify that a system-assigned managed identity is enabled. 5. In Microsoft Sentinel, go to 'Automation' > 'Playbooks' and confirm the playbook appears with status 'Enabled'. 6. Test the playbook by triggering it from an alert or incident and verify it runs successfully without connectivity errors.

## Rollback
1. In the Azure portal, navigate to the Standard logic app. 2. Under 'Settings', select 'Networking' and disable 'Virtual network integration'. 3. If private endpoints were created for inbound traffic, delete them under 'Networking' > 'Private endpoint connections'. 4. In Microsoft Sentinel, under 'Automation' > 'Playbooks', select the playbook and click 'Disable' or 'Delete' to remove it. 5. If the playbook was associated with an automation rule, edit or delete the rule in 'Automation' > 'Automation rules'.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
