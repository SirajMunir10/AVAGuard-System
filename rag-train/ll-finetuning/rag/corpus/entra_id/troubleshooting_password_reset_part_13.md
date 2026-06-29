# Troubleshooting: Password Reset

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot 'Object could not be found' error during password reset operations in Microsoft Entra Connect?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Error in event logs from Microsoft Entra Connect service indicating 'Object could not be found'
- Password reset operations fail

## Error Codes
N/A

## Root Causes
1. Sync engine is unable to find the user object in the Microsoft Entra connector space
2. Sync engine is unable to find the linked metaverse (MV) or Microsoft Entra connector space object

## Remediation Steps
1. Make sure that the user is synchronized from on-premises to Microsoft Entra ID via the current instance of Microsoft Entra Connect
2. Inspect the state of the objects in the connector spaces and MV
3. Confirm that the Active Directory Certificate Services (AD CS) object is connected to the MV object via the 'Microsoft.InfromADUserAccountEnabled.xxx' rule

## Validation
1. Open Synchronization Service Manager on the Microsoft Entra Connect server. 2. Go to the 'Connectors' tab and select the Active Directory connector. 3. Click 'Search Connector Space' and search for the affected user by name or DN. 4. Verify the user object exists in the on-premises AD connector space. 5. Switch to the Microsoft Entra connector, search for the same user, and confirm the object exists. 6. In the 'Metaverse Search' tab, search for the user and ensure it has a linked object to both the AD and Microsoft Entra connector spaces. 7. Check that the synchronization rule 'Microsoft.InfromADUserAccountEnabled.xxx' is applied and the user object is connected to the MV object. 8. Run a full synchronization cycle and verify no 'Object could not be found' errors appear in the event logs.

## Rollback
1. If the user object is missing from the on-premises AD connector space, restore the user from Active Directory Recycle Bin or re-create the user object in on-premises AD. 2. If the user object is missing from the Microsoft Entra connector space, run a full import and synchronization to re-populate the object. 3. If the MV object is missing or disconnected, use the 'Connector Space Object Properties' to re-connect the AD object to the MV object by re-applying the appropriate synchronization rules. 4. If the synchronization rule 'Microsoft.InfromADUserAccountEnabled.xxx' is missing or corrupted, re-import the default synchronization rules from Microsoft Entra Connect or run the 'Set-ADSyncScheduler -FullSyncStep $true' command to force a full sync. 5. After any corrective action, re-run the validation steps to confirm the error is resolved.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
