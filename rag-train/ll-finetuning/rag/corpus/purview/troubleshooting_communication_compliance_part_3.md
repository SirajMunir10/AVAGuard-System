# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to view and act on alerts for message issues that match policy conditions in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policies configured

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. After you configure Communication Compliance policies, you receive alerts for message issues that match your policy conditions
2. To view and act on alerts, assign users the following permissions: The Communication Compliance Analysts or the Communication Compliance Investigators role group, Reviewer in the policy that is associated with the alert
3. After you establish required permissions, use the following working instructions to investigate and remediate issues

## Validation
1. Confirm that the user has been assigned to the Communication Compliance Analysts or Communication Compliance Investigators role group by running: Get-RoleGroupMember "Communication Compliance Analysts" | Format-Table Name, RoleGroup; Get-RoleGroupMember "Communication Compliance Investigators" | Format-Table Name, RoleGroup. 2. Verify the user is listed as a Reviewer in the specific policy associated with the alert by running: Get-CommunicationCompliancePolicy -Identity "PolicyName" | Select-Object -ExpandProperty Reviewers. 3. Navigate to the Microsoft Purview compliance portal > Communication Compliance > Alerts tab and confirm the alert is visible and actionable.

## Rollback
1. Remove the user from the Communication Compliance Analysts or Communication Compliance Investigators role group by running: Remove-RoleGroupMember -Identity "Communication Compliance Analysts" -Member "user@domain.com"; Remove-RoleGroupMember -Identity "Communication Compliance Investigators" -Member "user@domain.com". 2. Remove the user from the Reviewer list of the policy by running: Set-CommunicationCompliancePolicy -Identity "PolicyName" -Reviewers @{Remove="user@domain.com"}. 3. Confirm the user can no longer view or act on alerts by checking the Alerts tab in the Communication Compliance solution.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
