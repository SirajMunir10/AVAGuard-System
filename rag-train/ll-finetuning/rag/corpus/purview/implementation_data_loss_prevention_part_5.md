# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policies to show matched conditions for Exchange Online events including non-sensitive information type conditions?

## Environment Context
- **Tenant Type:** E3 or E5 license holders
- **Configuration:** Auditing enabled; Advanced classification scanning and protection enabled; Windows 10 x64 (build 1809 or later) or Windows 11

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Auditing
2. Enable Advanced classification scanning and protection
3. Ensure Windows OS meets minimum build requirements (Windows 10 x64 build 1809 or later, or Windows 11; see KB5023773 for required builds)
4. For Exchange Online DLP events, matched conditions include enhanced detail for non-sensitive information type (SIT) conditions in addition to SIT matches

## Validation
1. Confirm auditing is enabled: Run `Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled` in Exchange Online PowerShell; verify output is 'True'. 2. Confirm Advanced classification scanning and protection is enabled: In the Microsoft Purview compliance portal, navigate to Data classification > Classifiers > Exact data match (EDM) and verify the feature is active. 3. Verify Windows OS build: On a managed Windows 10 device, run `winver` and confirm build is 1809 or later (or Windows 11). 4. Test DLP policy for Exchange Online: Create or use an existing DLP policy with a non-sensitive information type condition (e.g., 'Credit Card Number' with confidence level 'High'). Send a test email containing that pattern to an internal recipient. 5. Check DLP alert details: In the Microsoft Purview compliance portal, go to Data Loss Prevention > Alerts, locate the alert for the test email, and open it. Confirm the 'Matched conditions' section includes both the sensitive information type (e.g., 'Credit Card Number') and the non-sensitive condition (e.g., 'Content contains' or 'Sender is').

## Rollback
1. Disable auditing: In Exchange Online PowerShell, run `Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $false`. 2. Disable Advanced classification scanning and protection: In the Microsoft Purview compliance portal, navigate to Data classification > Classifiers > Exact data match (EDM) and disable the feature. 3. Downgrade Windows OS if necessary: Revert to a previous build via Windows Update or system restore (not recommended unless required). 4. Remove or modify the DLP policy: In the Microsoft Purview compliance portal, go to Data Loss Prevention > Policies, select the test policy, and either delete it or remove the non-sensitive condition. 5. Clear test alerts: In the Microsoft Purview compliance portal, go to Data Loss Prevention > Alerts, select any test alerts, and dismiss or delete them.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
