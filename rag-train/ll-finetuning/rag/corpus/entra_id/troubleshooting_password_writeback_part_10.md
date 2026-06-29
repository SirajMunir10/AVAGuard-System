# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot password writeback issues using event logs on the Microsoft Entra Connect machine?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Password writeback operations fail or are not working as expected

## Error Codes
N/A

## Root Causes
1. Issues related to password writeback operation
2. Problems setting passwords in Active Directory Domain Services

## Remediation Steps
1. Inspect the Application event log on the Microsoft Entra Connect machine
2. Look for events from the PasswordResetService source for operations and problems related to password writeback
3. Look for events from the ADSync source for operations and problems related to setting passwords in Active Directory Domain Services

## Validation
1. On the Microsoft Entra Connect server, open Event Viewer (eventvwr.msc).
2. Navigate to Windows Logs > Application.
3. Filter the current log by source: 'PasswordResetService' and look for Event ID 31000 (successful writeback) or Event ID 31001 (failure).
4. Also filter by source: 'ADSync' and look for Event ID 6329 (password set failure) or Event ID 6328 (success).
5. Confirm that recent events show successful password writeback operations with no errors.

## Rollback
1. If the remediation fails, revert any configuration changes made during troubleshooting (e.g., restore original Microsoft Entra Connect settings from backup).
2. Re-run the Microsoft Entra Connect configuration wizard and ensure password writeback is enabled.
3. Verify connectivity between Microsoft Entra Connect and the on-premises domain controllers.
4. Restart the Microsoft Entra Connect Sync service (ADSync) from Services.msc.
5. If issues persist, restore the Microsoft Entra Connect server from a recent backup taken before changes.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
