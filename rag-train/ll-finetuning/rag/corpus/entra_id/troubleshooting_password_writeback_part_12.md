# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot password writeback permissions errors or federated account issues during configuration?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Permissions error on the cloud or on-premises administrator account specified during configuration
- Error when attempting to use a federated cloud Hybrid Administrator when disabling password writeback

## Error Codes
N/A

## Root Causes
1. Permissions error on the cloud or on-premises administrator account
2. Using a federated account while configuring the password writeback capability

## Remediation Steps
1. Check your administrative permissions
2. Ensure that you're not using a federated account while configuring the password writeback capability

## Validation
1. Verify that the cloud administrator account used for Microsoft Entra Connect has the 'Hybrid Identity Administrator' role assigned in Entra ID. Run: Get-MgRoleManagementDirectoryRoleAssignment -Filter "principalId eq '<admin-object-id>'" | Where-Object {$_.RoleDefinition.DisplayName -eq 'Hybrid Identity Administrator'}. 2. Confirm the on-premises AD account used by Entra Connect has 'Reset Password' and 'Change Password' extended rights on the user objects and the 'Replicating Directory Changes' permission on the domain. Use: dsacls 'CN=User,CN=<domain>,CN=Microsoft,CN=Program Data,CN=Root,DC=<domain>,DC=com' /G '<account>:CA;Reset Password;user' and dsacls '<domain DN>' /G '<account>:CA;Replicating Directory Changes'. 3. Ensure the account used to configure password writeback is not a federated account. Check the user's 'UserPrincipalName' and 'Issuer' in Entra ID: Get-MgUser -UserId '<admin-upn>' | Select-Object UserPrincipalName, @{N='Federated';E={$_.OnPremisesImmutableId -ne $null}}. 4. Test password writeback by resetting a test user's password from the Entra admin center and verifying the change replicates on-premises within 30 seconds.

## Rollback
1. If permissions were incorrectly modified, restore the original permissions on the on-premises AD account using: dsacls '<DN>' /R '<account>' and then reapply the correct permissions as per the validation steps. 2. If a federated account was used, switch to a non-federated cloud-only account with 'Hybrid Identity Administrator' role. Remove the federated account from the Entra Connect configuration: In the Microsoft Entra Connect wizard, select 'Customize synchronization options', then under 'Password writeback', clear the checkbox and re-enter credentials using a non-federated account. 3. If password writeback stops working after changes, re-enable it via the wizard: Select 'Enable password writeback' and provide the correct non-federated admin credentials. 4. As a last resort, run: Set-ADSyncPasswordWritebackConfiguration -Enable $false -Credential (Get-Credential) to disable, then re-enable with proper credentials.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
