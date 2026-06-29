# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Information Barriers issues in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure that you have the appropriate subscriptions and permissions.
2. Ensure that you meet the necessary prerequisites.
3. Connect to Security & Compliance Center PowerShell.

## Validation
1. Verify that the user account has the required license (e.g., Microsoft 365 E5 or A5) by running: Get-MsolUser -UserPrincipalName <UPN> | Select-Object Licenses. 2. Confirm the user is assigned the Information Barrier Management role by running: Get-RoleGroupMember "Information Barrier Management" | Format-Table Name. 3. Ensure the user can connect to Security & Compliance Center PowerShell by running: Connect-IPPSSession -UserPrincipalName <UPN>. 4. List existing information barrier policies with: Get-InformationBarrierPolicy | Format-Table Name, State, AssignedSegment.

## Rollback
1. If a new policy was applied, remove it by running: Remove-InformationBarrierPolicy -Identity <PolicyGUID> -Confirm:$false. 2. If a policy segment was modified, revert to the previous segment definition using: Set-InformationBarrierPolicy -Identity <PolicyGUID> -AssignedSegment <PreviousSegmentName>. 3. If connectivity changes were made, disconnect the PowerShell session with: Disconnect-ExchangeOnline -Confirm:$false. 4. If permissions were changed, remove the user from the Information Barrier Management role by running: Remove-RoleGroupMember -Identity "Information Barrier Management" -Member <UPN> -Confirm:$false.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
