# Incident Response: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Incident Response

## Scenario / Query
How to investigate data loss prevention alerts, including the lifecycle of alerts from creation through final remediation and policy tuning?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Purview DLP alert investigation

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Understand the lifecycle of alerts from creation through final remediation and policy tuning
2. Use the tools introduced to investigate alerts

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) and navigate to Data Loss Prevention > Alerts. 2. Verify that the alert you investigated is listed and its status reflects the expected lifecycle stage (e.g., Active, Investigating, Resolved). 3. Confirm that any policy tuning changes you made are reflected in the DLP policy configuration under Data Loss Prevention > Policies. 4. Use the Activity explorer to confirm that the relevant DLP rule matches and actions are logged as expected. 5. Run the following PowerShell command to list DLP alerts and their status: Get-DlpComplianceAlert | Where-Object {$_.Status -eq 'Resolved'} | Format-Table Name, Status, LastModifiedTime

## Rollback
1. If policy tuning caused unintended blocking or false positives, revert the policy changes: In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies, select the modified policy, and restore the previous rule settings or disable the policy temporarily. 2. If an alert was incorrectly dismissed or resolved, reopen it: In the Alerts list, select the alert, click 'Manage alert', and change the status back to 'Active' or 'Investigating'. 3. To restore a deleted or modified DLP rule, use the Microsoft Purview compliance portal to recreate the rule from backup or previous configuration export. 4. If needed, use the following PowerShell command to reset a DLP policy to its default state: Set-DlpCompliancePolicy -Identity 'PolicyName' -ExchangeLocation $null -SharePointLocation $null -OneDriveLocation $null -TeamsLocation $null -EndpointDlpLocation $null (adjust locations as needed). 5. Monitor the Alerts page and Activity explorer for any recurrence of the original issue after rollback.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
