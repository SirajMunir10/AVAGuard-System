# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to set a preservation period for policy matches in a custom Communication Compliance policy that takes precedence over the global setting?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Custom policy workflow in Communication Compliance

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal with credentials for an admin account in your Microsoft 365 organization.
2. Go to the Communication Compliance solution, then select Policies in the left navigation.
3. Select a time period for preserving policy matches in the policy workflow for a custom policy.

## Validation
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com) with an admin account. 2. Navigate to Communication Compliance > Policies. 3. Select the custom policy you configured. 4. In the policy details pane, verify that the 'Preservation period' field displays the time period you set (e.g., '7 days', '30 days', etc.). 5. Confirm that the policy's preservation period is different from the global setting by checking the global retention settings in Communication Compliance > Settings > Retention. 6. Optionally, use the Get-CommunicationCompliancePolicy PowerShell cmdlet (requires Exchange Online PowerShell) to retrieve the policy's RetentionDuration property and ensure it matches your configured value.

## Rollback
1. Sign in to the Microsoft Purview portal with an admin account. 2. Go to Communication Compliance > Policies. 3. Select the custom policy you modified. 4. In the policy workflow, change the preservation period back to the original value (or to the global default). 5. Save the policy. 6. Verify the change by checking the policy details or using the Get-CommunicationCompliancePolicy cmdlet to confirm the RetentionDuration property has reverted.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
