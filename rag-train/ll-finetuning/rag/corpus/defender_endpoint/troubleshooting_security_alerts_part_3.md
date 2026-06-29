# Troubleshooting: Security Alerts

**Domain:** Defender for Endpoint
**Subdomain:** Security Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to view and process security alerts in Microsoft Defender for Cloud?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Defender for Cloud enabled, log data collected from Azure/hybrid/multicloud resources

## Symptoms
- Security alerts are listed in Defender for Cloud with prioritization based on severity

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Prioritize alerts based on their alert severity, addressing higher severity alerts first
2. View the alert details and information needed to quickly investigate the problem
3. Follow the steps provided to remediate an attack

## Validation
1. Sign in to the Azure portal (https://portal.azure.com).
2. Navigate to Microsoft Defender for Cloud > Security alerts.
3. Confirm that alerts are displayed and sorted by severity (High, Medium, Low).
4. Select a high-severity alert and verify that the alert details pane opens with full information (description, affected resources, remediation steps, etc.).
5. Click 'View full details' and ensure the alert page shows the attack timeline, entities, and recommended actions.
6. Execute the remediation steps provided in the alert (e.g., 'Take action' button) and confirm the alert status updates to 'Resolved' or 'Dismissed' as appropriate.

## Rollback
1. If a remediation action (e.g., blocking an IP, disabling a user) causes unintended issues, reverse the action immediately:
   - For IP block: Remove the block rule from the relevant network security group or Azure Firewall.
   - For user disable: Re-enable the user account in Azure AD.
   - For resource modification: Restore from a recent backup or revert the configuration change.
2. If an alert was dismissed in error, reopen it by changing the status back to 'Active' in the alert details.
3. If a suppression rule was created, delete or disable the rule to allow future alerts of that type.
4. Verify that the original issue (if any) is no longer causing impact and that security monitoring continues as expected.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/managing-and-responding-alerts>
