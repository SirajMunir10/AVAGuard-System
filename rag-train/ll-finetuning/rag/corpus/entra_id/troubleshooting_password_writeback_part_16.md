# Troubleshooting: Password Writeback (33001)

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
Password writeback fails due to reserved characters in on-premises organizational unit (OU) structure

## Environment Context
- **Tenant Type:** Entra ID tenant with password writeback enabled
- **Configuration:** On-premises Active Directory OU structure

## Symptoms
- Password writeback fails

## Error Codes
- `33001`

## Root Causes
1. Reserved characters in on-premises organizational unit (OU) structure: space or # character at the beginning of a string, space character at the end of a string, quotation mark, left angle bracket, right angle bracket, carriage return, forward slash

## Remediation Steps
1. Remove reserved characters from the on-premises organizational unit (OU) structure

## Validation
1. Open Active Directory Users and Computers (dsa.msc).
2. Navigate to the OU that was previously causing the writeback failure.
3. Right-click the OU, select Properties, then the Attribute Editor tab.
4. Verify that the 'distinguishedName' attribute no longer contains any of the following reserved characters at the beginning or end of any string: space (# at start), quotation mark ("), left angle bracket (<), right angle bracket (>), carriage return (\r), forward slash (/).
5. Confirm that no OU name begins with a space or ends with a space.
6. Trigger a password writeback test by resetting a user password in the Entra admin center for a user in the affected OU.
7. Check the Entra ID audit logs for event ID 33001; it should no longer appear.
8. Verify the password change is reflected in on-premises AD within the expected replication time.

## Rollback
1. If the remediation causes issues (e.g., users cannot authenticate or OUs are missing), restore the original OU names from backup using Active Directory Recycle Bin or authoritative restore.
2. To restore an OU name, open Active Directory Administrative Center, locate the OU, right-click, select Properties, and revert the 'Name' field to its original value (including any reserved characters).
3. Alternatively, use PowerShell: Get-ADOrganizationalUnit -Filter {Name -eq 'OriginalName'} | Rename-ADObject -NewName 'OriginalNameWithReservedChars'.
4. After restoration, verify that password writeback resumes failing with error 33001, confirming the rollback is complete.
5. Monitor the Entra ID audit logs for the return of event ID 33001.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
