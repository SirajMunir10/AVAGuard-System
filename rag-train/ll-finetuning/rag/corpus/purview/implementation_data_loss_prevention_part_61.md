# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure DLP policy mode and deployment options?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy mode settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose to run the policy in simulation mode with or without showing policy tip by selecting the Run the policy in simulation mode option.
2. Choose to run the policy as soon as an hour after it's created by selecting the Turn it on right away option.
3. Choose to just save it and come back to it later by selecting the Keep it off option.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy you configured. 3. In the policy details pane, under 'Policy mode', verify the selected mode matches the intended deployment option (e.g., 'Run the policy in simulation mode', 'Turn it on right away', or 'Keep it off'). 4. If simulation mode is selected, confirm that 'Show policy tips while in simulation mode' is enabled or disabled as desired. 5. Use the Get-DlpCompliancePolicy cmdlet in Security & Compliance PowerShell: run `Get-DlpCompliancePolicy -Identity "<PolicyName>" | Format-List Mode, SimulationMode` and verify the Mode property is 'Test' (simulation) or 'Enable' (turned on) or 'Disable' (kept off), and SimulationMode is $true or $false accordingly.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the policy. 2. Under 'Policy mode', change the mode to the previous desired state (e.g., from 'Turn it on right away' to 'Keep it off' or 'Run the policy in simulation mode'). 3. If reverting to simulation mode, adjust the 'Show policy tips while in simulation mode' checkbox as needed. 4. Alternatively, use the Set-DlpCompliancePolicy cmdlet in Security & Compliance PowerShell: run `Set-DlpCompliancePolicy -Identity "<PolicyName>" -Mode <PreviousMode> -SimulationMode <$true/$false>` where <PreviousMode> is 'Test' (simulation) or 'Enable' (turned on) or 'Disable' (kept off). 5. Confirm the change by running `Get-DlpCompliancePolicy -Identity "<PolicyName>" | Format-List Mode, SimulationMode`.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
