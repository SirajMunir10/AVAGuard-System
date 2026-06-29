# Troubleshooting: Hybrid Join (0x801c001d)

**Domain:** Entra ID
**Subdomain:** Hybrid Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve DSREG_AUTOJOIN_ADCONFIG_READ_FAILED (0x801c001d/-2145648611) error during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** N/A

## Symptoms
- DSREG_AUTOJOIN_ADCONFIG_READ_FAILED (0x801c001d/-2145648611) error
- Event ID 220 is present in User Device Registration event logs

## Error Codes
- `0x801c001d`
- `-2145648611`

## Root Causes
1. Windows can't access the computer object in Active Directory
2. Error codes ERROR_NO_SUCH_LOGON_SESSION (1312) and ERROR_NO_SUCH_USER (1317) are related to replication issues in on-premises Active Directory

## Remediation Steps
1. Troubleshoot replication issues in Active Directory. These replication issues might be transient, and they might go away after a while.

## Validation
1. Check User Device Registration event logs for Event ID 220: Run 'Get-WinEvent -LogName Microsoft-Windows-User Device Registration/Admin | Where-Object { $_.Id -eq 220 }' and verify no DSREG_AUTOJOIN_ADCONFIG_READ_FAILED errors are present. 2. Confirm AD replication is healthy: Run 'repadmin /replsummary' and ensure no replication failures. 3. Test device registration: Run 'dsregcmd /status' and verify the AzureAdJoined and DomainJoined fields show 'YES'.

## Rollback
1. If replication issues persist, restore AD replication using 'repadmin /syncall /AdeP' to force replication between domain controllers. 2. If the error continues, verify the computer object exists in AD: Run 'Get-ADComputer -Identity <ComputerName>' and ensure it is not disabled or missing. 3. As a last resort, rejoin the device to the domain: Disjoin from domain, reboot, then rejoin using 'Add-Computer -DomainName <DomainName> -Credential (Get-Credential)'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
