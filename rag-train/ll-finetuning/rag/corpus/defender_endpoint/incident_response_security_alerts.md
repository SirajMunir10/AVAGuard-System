# Incident Response: Security Alerts

**Domain:** Defender for Endpoint
**Subdomain:** Security Alerts
**Incident Type:** Incident Response

## Scenario / Query
How to use MITRE ATT&CK matrix mapping in Defender for Cloud alerts for incident response?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Defender for Cloud workload protection plans enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Defender for Cloud leverages the MITRE Attack Matrix to associate alerts with their perceived intent
2. Helps formalize security domain knowledge

## Validation
1. In the Azure portal, navigate to Microsoft Defender for Cloud > Security alerts. 2. Select an alert from the list. 3. In the alert details pane, verify that the 'MITRE ATT&CK' field is populated with one or more tactics (e.g., Initial Access, Execution) and techniques (e.g., T1078, T1059). 4. Confirm that the alert's 'Intent' property (visible in the alert JSON or via Azure Resource Graph) matches the expected MITRE tactic. 5. Optionally, run the following Azure Resource Graph query to list alerts with their MITRE mapping: securityresources | where type == 'microsoft.security/locations/alerts' | project alertName, properties.compromisedEntity, properties.mitreAttTacK, properties.intent

## Rollback
1. If the MITRE mapping is incorrect or missing, verify that the Defender for Cloud workload protection plans are enabled for the relevant resource types (e.g., Servers, SQL, Storage) by navigating to Defender for Cloud > Environment settings > [subscription] > Defender plans. 2. Ensure the alert is not suppressed or dismissed incorrectly by checking the alert's status and history. 3. If the mapping issue persists, open a support request with Microsoft Azure Support, referencing the alert ID and expected MITRE mapping. No direct rollback action exists for MITRE mapping as it is automatically assigned by Defender for Cloud based on alert logic.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-overview>
