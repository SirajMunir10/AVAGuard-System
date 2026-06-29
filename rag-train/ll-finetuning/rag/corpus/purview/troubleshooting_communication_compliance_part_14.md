# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
Why do I see a generic error message 'An error occurred' after selecting Summarize in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance roles and Security Copilot contributor role

## Symptoms
- Generic error message 'An error occurred' appears after selecting Summarize

## Error Codes
N/A

## Root Causes
1. You don't have the required license for Copilot in Microsoft Purview
2. You don't have the required Communication Compliance role and/or the Security Copilot contributor role
3. There's an internal error

## Remediation Steps
1. Ensure you have one of the following Communication Compliance roles: Communication Compliance, Communication Compliance Analysts, Communication Compliance Investigators
2. Ensure you have the Security Copilot contributor role, which should be turned on by default for all users in a Microsoft Entra organization

## Validation
1. Confirm the user has a valid Copilot in Microsoft Purview license by checking the Microsoft 365 admin center: Billing > Licenses > select the user and verify 'Copilot in Microsoft Purview' is assigned.
2. Verify the user has at least one of the required Communication Compliance roles: Communication Compliance, Communication Compliance Analysts, or Communication Compliance Investigators. Run in Exchange Online PowerShell: Get-RoleGroupMember "Communication Compliance" | Format-List Name,WindowsLiveID; Get-RoleGroupMember "Communication Compliance Analysts" | Format-List Name,WindowsLiveID; Get-RoleGroupMember "Communication Compliance Investigators" | Format-List Name,WindowsLiveID.
3. Verify the user has the Security Copilot contributor role. Run in Microsoft Entra admin center: Identity > Roles & admins > Roles & admins > search for 'Security Copilot contributor' > select the role > Assignments > confirm the user is listed.
4. After confirming roles and license, navigate to Communication Compliance > select a policy > open a message > select 'Summarize'. Verify the summary appears without the generic error.

## Rollback
1. If the user was assigned a Communication Compliance role that is not needed, remove it: In Exchange Online PowerShell, run Remove-RoleGroupMember -Identity "Communication Compliance" -Member <user@domain.com> (or the specific role group name).
2. If the Security Copilot contributor role was assigned unnecessarily, remove it: In Microsoft Entra admin center, go to Identity > Roles & admins > Roles & admins > select 'Security Copilot contributor' > Assignments > select the user > Remove assignment.
3. If a license was assigned incorrectly, unassign it: In Microsoft 365 admin center, Billing > Licenses > select the user > uncheck 'Copilot in Microsoft Purview' > Save.
4. After rollback, test the Summarize feature again to confirm the error returns to its previous state.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
