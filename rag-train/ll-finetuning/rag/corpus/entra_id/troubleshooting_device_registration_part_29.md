# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose Microsoft Entra hybrid join failures by examining the 'Previous Registration' subsection in the join status output?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Windows 10 version, domain-joined device

## Symptoms
- Device is domain-joined but unable to Microsoft Entra hybrid join
- The 'Previous Registration' subsection is displayed in the 'Diagnostic Data' section of the join status output

## Error Codes
N/A

## Root Causes
1. Look for the registration type and error code from the following tables, depending on the Windows 10 version you're using

## Remediation Steps
1. Look for the 'Previous Registration' subsection in the 'Diagnostic Data' section of the join status output
2. The 'Registration Type' field denotes the type of join

## Validation
1. On the affected device, open an elevated command prompt and run 'dsregcmd /status'. 2. In the output, locate the 'Diagnostic Data' section and find the 'Previous Registration' subsection. 3. Verify that the 'Registration Type' field shows the expected join type (e.g., 'hybridjoin' or 'azureadjoin') and that no error code is present in the 'Error Code' field. 4. Confirm that the device now appears in the Microsoft Entra admin center under 'Devices' with a status of 'Hybrid Azure AD joined'.

## Rollback
1. If the remediation fails or causes issues, re-run 'dsregcmd /leave' on the device to remove any partial registration. 2. Restart the device to clear any cached state. 3. Re-attempt the hybrid join by running 'dsregcmd /join' from an elevated command prompt. 4. If problems persist, verify that the device can reach the Microsoft Entra endpoints and that the service connection point (SCP) is correctly configured in Active Directory.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
