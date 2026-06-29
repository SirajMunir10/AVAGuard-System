# Implementation: Endpoint Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy to detect printing of protected files?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, printer groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the condition that detects when a protected file is printed from an onboarded device.
2. For more information, see Printer groups.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy you configured. 3. Under 'Locations', confirm that 'Devices' is included and that the policy applies to the correct device groups. 4. Under 'Rules', verify that a rule exists with the condition 'File is printed' and that the condition is set to detect printing of protected files. 5. Use the DLP Alerts dashboard to confirm that a test print of a protected file from an onboarded device generates an alert or event. 6. Run the following PowerShell command to verify policy deployment status: Get-DlpCompliancePolicy -Identity "YourPolicyName" | Format-List Name, Workload, Mode, DistributionStatus

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the DLP policy you modified. 2. Under 'Rules', remove or disable the rule that contains the 'File is printed' condition. 3. If the policy was newly created, delete the policy entirely. 4. Alternatively, set the policy to 'Test' mode to stop enforcement: Set-DlpCompliancePolicy -Identity "YourPolicyName" -Mode Test. 5. Verify rollback by confirming that printing a protected file no longer triggers a DLP event or alert. 6. If needed, restore previous policy configuration from backup or reapply original rules.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
