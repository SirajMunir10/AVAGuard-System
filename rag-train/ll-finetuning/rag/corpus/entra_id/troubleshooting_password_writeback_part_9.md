# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to disable and re-enable the password writeback feature to resolve connectivity issues?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect with Password Writeback enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. As an administrator on the server that runs Microsoft Entra Connect, open the Microsoft Entra Connect Configuration wizard.
2. In Connect to Microsoft Entra ID, enter your Microsoft Entra Hybrid Administrator credentials.
3. In Connect to AD DS, enter your on-premises Active Directory Domain Services admin credentials.
4. In Uniquely identifying your users, select the Next button.
5. In Optional features, clear the Password writeback check box.
6. Select Next through the remaining dialog pages without changing anything until you get to the Ready to configure page.
7. Check that the Ready to configure page shows the Password writeback option as disabled.
8. Select the green Configure button to commit your changes.
9. In Finished, clear the Synchronize now option, and then select Finish to close the wizard.
10. Reopen the Microsoft Entra Connect Configuration wizard.
11. Repeat steps 2-8, this time selecting the Password writeback option on the Optional features page to re-enable the service.

## Validation
1. On the Microsoft Entra Connect server, open the Microsoft Entra Connect Configuration wizard and navigate to the Ready to configure page. Confirm that the Password writeback option is displayed as enabled. 2. Run the following PowerShell command as an administrator: `Get-ADSyncGlobalSettings | Where-Object {$_.Name -eq 'PasswordWritebackEnabled'}`. Verify the output shows the setting is enabled. 3. Trigger a password change for a test user in Microsoft Entra ID and confirm the change is written back to on-premises AD DS within the expected synchronization interval.

## Rollback
1. On the Microsoft Entra Connect server, open the Microsoft Entra Connect Configuration wizard. 2. In Optional features, clear the Password writeback check box. 3. Select Next through the remaining dialog pages until the Ready to configure page shows Password writeback as disabled. 4. Select the green Configure button to commit the change. 5. In Finished, clear the Synchronize now option, then select Finish to close the wizard.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
