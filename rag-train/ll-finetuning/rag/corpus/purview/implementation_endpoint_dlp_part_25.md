# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to use the Generative AI Websites group in Microsoft Purview Endpoint DLP default policies?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Data Security Posture Management for AI default policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The Generative AI Websites group contains these supported sites.
2. The group is used for default policies within Data Security Posture Management for AI and can't be edited or deleted.

## Validation
1. In Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies. 2. Locate the default Data Security Posture Management for AI policy (e.g., 'Data Security Posture Management for AI – Endpoint'). 3. Open the policy and review the 'Locations' section to confirm that 'Endpoint devices' is included. 4. Under 'Rules', verify that a rule references the 'Generative AI Websites' group (e.g., in the 'Conditions' or 'Actions' section). 5. Use PowerShell cmdlet Get-DlpCompliancePolicy -Identity "Data Security Posture Management for AI – Endpoint" | Format-List to confirm the policy exists and its settings. 6. Run Get-DlpComplianceRule -Policy "Data Security Posture Management for AI – Endpoint" | Where-Object {$_.AccessScope -eq "GenerativeAIWebsites"} to verify the rule includes the Generative AI Websites group.

## Rollback
1. If the default policy was modified or deleted, restore it from backup or recreate using the default template: In Purview portal, go to Data Loss Prevention > Policies > Create policy > Start with a template > select 'Data Security Posture Management for AI – Endpoint'. 2. If a custom rule referencing the Generative AI Websites group was added and causes issues, remove that rule: In the policy, edit the rule and delete it, or use PowerShell: Remove-DlpComplianceRule -Identity "<RuleName>" -Confirm:$false. 3. If the policy was disabled, re-enable it: Set-DlpCompliancePolicy -Identity "Data Security Posture Management for AI – Endpoint" -Enabled $true. 4. If the Generative AI Websites group was inadvertently removed (though it cannot be edited/deleted per documentation), contact Microsoft Support to restore the default group.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
