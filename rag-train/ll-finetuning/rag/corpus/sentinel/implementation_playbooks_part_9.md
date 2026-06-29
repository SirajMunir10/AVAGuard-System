# Implementation: Playbooks

**Domain:** Sentinel
**Subdomain:** Playbooks
**Incident Type:** Implementation

## Scenario / Query
How do I configure the Pricing plan and Zone redundancy for a Logic App used as a Microsoft Sentinel playbook?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Logic App Standard workflow creation in Azure portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Pricing plan, select the compute resources and their pricing for your logic app.
2. Under Zone redundancy, you can enable this capability if you selected an Azure region that supports availability zone redundancy. For this example, leave the option disabled.

## Validation
1. In the Azure portal, navigate to the Logic App resource. 2. Under 'Settings', select 'Pricing plan' and confirm the selected plan matches the intended compute resources and pricing. 3. Under 'Settings', select 'Zone redundancy' and verify the setting is disabled (or enabled as per the original configuration). 4. Optionally, run the Azure CLI command: az logicapp show --name <logic-app-name> --resource-group <resource-group-name> --query "properties.configuration.zoneRedundant" to confirm the zone redundancy setting.

## Rollback
1. In the Azure portal, navigate to the Logic App resource. 2. Under 'Settings', select 'Pricing plan' and change it back to the original plan. 3. Under 'Settings', select 'Zone redundancy' and set it to the original value (e.g., disabled if it was changed to enabled). 4. Optionally, run the Azure CLI command: az logicapp update --name <logic-app-name> --resource-group <resource-group-name> --set properties.configuration.zoneRedundant=false to revert the zone redundancy setting.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/create-playbooks>
