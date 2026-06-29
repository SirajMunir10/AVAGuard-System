# Troubleshooting: Password Reset Writeback (ADMutliMatchError)

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot ADMutliMatchError event in SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback configuration

## Symptoms
- Two users found in on-premises directory with the same cloud anchor attribute

## Error Codes
- `ADMutliMatchError`

## Root Causes
1. Two users in on-premises directory with the same cloud anchor attribute

## Remediation Steps
1. Check sync logs and the last few sync run details for more information

## Validation
1. Open the Microsoft Entra admin center, navigate to Identity > Hybrid management > Microsoft Entra Connect > Connect Sync > View provisioning logs. 2. Filter logs by 'ADMutliMatchError' and review the last few sync run details to confirm no duplicate cloud anchor attributes exist. 3. Run the following PowerShell command on the on-premises server to list users with duplicate msDS-ExternalDirectoryObjectID: Get-ADUser -Filter * -Properties msDS-ExternalDirectoryObjectID | Group-Object msDS-ExternalDirectoryObjectID | Where-Object { $_.Count -gt 1 } | Select-Object Name, Count. 4. Verify that only one user per cloud anchor remains after remediation.

## Rollback
1. If the remediation fails or causes issues, restore the original duplicate user objects from Active Directory Recycle Bin or from a recent backup. 2. Re-run a delta sync from the on-premises server: Start-ADSyncSyncCycle -PolicyType Delta. 3. Monitor the sync logs for any recurrence of ADMutliMatchError. 4. If needed, temporarily disable SSPR writeback by setting the 'Self-service password reset' writeback option to 'No' in the Microsoft Entra admin center under Password reset > On-premises integration.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
