# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret the Device State section of dsregcmd output to determine if a device is Microsoft Entra joined, domain joined, or hybrid joined?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Device join state parameters

## Symptoms
- Device state shows AzureAdJoined: NO when expected YES
- Device state shows EnterpriseJoined: YES when AzureAdJoined is also YES
- Device state shows DomainJoined: NO when device is domain-joined

## Error Codes
N/A

## Root Causes
1. Device is not joined to Microsoft Entra ID
2. Device is joined to on-premises Active Directory (EnterpriseJoined) and cannot be both EnterpriseJoined and AzureAdJoined
3. Device is not joined to a domain

## Remediation Steps
1. Check the AzureAdJoined field: Set the state to YES if the device is joined to Microsoft Entra ID. Otherwise, set the state to NO.
2. Check the EnterpriseJoined field: Set the state to YES if the device is joined to an on-premises Active Directory (AD). A device can't be both EnterpriseJoined and AzureAdJoined.
3. Check the DomainJoined field: Set the state to YES if the device is joined to a domain (Active Directory).
4. Check the DomainName field: Set the state to the name of the domain if the device is joined to a domain.

## Validation
1. Open Command Prompt as Administrator and run 'dsregcmd /status'. 2. In the output, locate the 'Device State' section. 3. Verify that 'AzureAdJoined' is set to 'YES' if the device is expected to be Microsoft Entra joined; otherwise, confirm it is 'NO'. 4. Verify that 'EnterpriseJoined' is set to 'YES' only if the device is joined to an on-premises Active Directory; ensure it is not 'YES' when 'AzureAdJoined' is also 'YES'. 5. Verify that 'DomainJoined' is set to 'YES' if the device is joined to a domain (Active Directory); otherwise, confirm it is 'NO'. 6. Verify that 'DomainName' displays the correct domain name if the device is domain-joined.

## Rollback
1. If validation reveals incorrect join states, re-run 'dsregcmd /status' to confirm current state. 2. For incorrect 'AzureAdJoined' state, ensure the device is properly joined to Microsoft Entra ID by following official join procedures; if not intended, leave as 'NO'. 3. For incorrect 'EnterpriseJoined' state, verify the device's on-premises AD join status; if both 'EnterpriseJoined' and 'AzureAdJoined' are 'YES', this is unsupported and must be corrected by removing one join (e.g., unjoin from on-premises AD or Microsoft Entra ID). 4. For incorrect 'DomainJoined' state, join the device to the appropriate domain if needed, or leave as 'NO' if not domain-joined. 5. For incorrect 'DomainName', update the domain membership or correct the domain name via domain join procedures.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
