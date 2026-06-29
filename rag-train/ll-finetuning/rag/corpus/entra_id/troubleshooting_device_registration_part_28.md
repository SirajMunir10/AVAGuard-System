# Troubleshooting: Device Registration (0xcaa1002d)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Entra hybrid join failure due to general ADAL failure error ERROR_ADAL_OPERATION_PENDING (0xcaa1002d/-895418323)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Authentication logs

## Symptoms
- Device fails to join Microsoft Entra hybrid
- Error code 0xcaa1002d/-895418323 appears

## Error Codes
- `0xcaa1002d`
- `-895418323`

## Root Causes
1. General ADAL failure

## Remediation Steps
1. Look for the suberror code or server error code from the authentication logs

## Validation
1. On the affected device, open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > User Device Registration > Admin. Look for events with ID 304 or 305 that indicate successful hybrid join. 2. Run 'dsregcmd /status' from an elevated command prompt and verify that 'AzureAdJoined' is set to 'YES' and 'DomainJoined' is set to 'YES'. 3. In the Microsoft Entra admin center, go to Identity > Devices > All devices and confirm the device appears with a status of 'Hybrid Azure AD joined'. 4. Check the authentication logs in the Entra admin center (Identity > Monitoring & health > Sign-in logs) for the device's sign-in activity with a status of 'Success'.

## Rollback
1. If the remediation fails, revert any changes made to the device's configuration by restoring the previous state of the scheduled task 'CreateJoinTask' under Microsoft > Windows > Workplace Join. 2. On the device, run 'dsregcmd /leave' to remove the device from Microsoft Entra, then re-attempt the hybrid join process using the original configuration. 3. In the Microsoft Entra admin center, navigate to Identity > Devices > All devices, locate the device entry, and delete it if it was partially created. 4. Review the authentication logs again to identify the suberror code or server error code from the original failure and consult the troubleshooting guide for that specific code.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
