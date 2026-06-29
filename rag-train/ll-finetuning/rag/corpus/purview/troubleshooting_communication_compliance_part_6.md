# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to quickly review policy settings without opening a policy in Communication Compliance?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Need to review conditions for each policy to determine risk before opening the policy
- Testing multiple policies with different conditions

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Policy settings to open a panel where you can view the policy settings
2. If you are a member of the Communication Compliance or Communication Compliance Admins role group, you can view and change settings from the panel
3. If you are a member of the Communication Compliance Investigators or Communication Compliance Analysts role group, you can view settings but you cannot change them

## Validation
1. Navigate to the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Go to Communication Compliance > Policies.
3. For each policy listed, click the policy name to select it, then click 'Policy settings' to open the settings panel.
4. Verify that the panel displays the policy conditions (e.g., direction, sensitive info types, keywords) without requiring you to open the full policy editor.
5. Confirm that if you are in the Communication Compliance or Communication Compliance Admins role group, you can toggle settings on/off or modify values; if you are in the Communication Compliance Investigators or Communication Compliance Analysts role group, you can view but not change settings.

## Rollback
1. If the policy settings panel does not appear or shows incorrect conditions, close the panel and refresh the browser.
2. Re-navigate to Communication Compliance > Policies and select the same policy again, then click 'Policy settings' to retry.
3. If the issue persists, verify your role group membership in the Microsoft Purview compliance portal under Roles & scopes > Permissions > Role groups for Communication Compliance.
4. If you lack the required permissions (Communication Compliance or Communication Compliance Admins for edit, or Communication Compliance Investigators/Analysts for view), contact your tenant administrator to adjust role assignments.
5. As a last resort, use the Get-CommunicationCompliancePolicy PowerShell cmdlet (Exchange Online PowerShell) to retrieve policy settings programmatically: Get-CommunicationCompliancePolicy -Identity "PolicyName" | Format-List.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
