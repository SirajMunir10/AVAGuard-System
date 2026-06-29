# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose Primary Refresh Token (PRT) acquisition or refresh failures using dsregcmd output?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows 10 May 2021 update (version 21H1) or later

## Symptoms
- AzureAdPrt field is not set to YES
- AcquirePrtDiagnostics or RefreshPrtDiagnostics field shows PRESENT

## Error Codes
N/A

## Root Causes
1. Failed PRT acquisition or refresh after the last successful PRT update time (AzureAdPrtUpdateTime/EnterprisePrtUpdateTime)

## Remediation Steps
1. Run dsregcmd in a user context to retrieve the user's valid status
2. Check the AcquirePrtDiagnostics field for PRESENT state to identify failed PRT attempt
3. Review the Previous Prt Attempt field for the local time in UTC of the failed attempt
4. Review the Attempt Status field for the client error code (HRESULT)
5. Review the User Identity field for the UPN of the user for whom the PRT attempt happened
6. Review the Credential Type field (e.g., Password or Next Generation Credential (NGC) for Windows Hello)
7. Review the Correlation ID field for the server correlation ID
8. Review the Endpoint URI field for the last endpoint accessed before failure
9. Review the HTTP Method field
10. Review the HTTP Error field for WinHttp transport error code
11. Review the HTTP Status field for the HTTP status returned by the endpoint
12. Review the Server Error Code field
13. Review the Server Error Description field for the error message from the server

## Validation
1. Open a command prompt as the currently signed-in user (not elevated).
2. Run: dsregcmd /status
3. Verify that the 'AzureAdPrt' field is set to 'YES'.
4. Verify that the 'AcquirePrtDiagnostics' and 'RefreshPrtDiagnostics' fields are not present (i.e., no 'PRESENT' value).
5. Check that 'AzureAdPrtUpdateTime' and 'EnterprisePrtUpdateTime' show a recent timestamp.
6. If any of these checks fail, the remediation has not succeeded.

## Rollback
1. If the remediation introduced issues, restore the previous device state by re-running the original troubleshooting steps:
   - Run: dsregcmd /status
   - Confirm the 'AzureAdPrt' field is 'NO' and 'AcquirePrtDiagnostics' or 'RefreshPrtDiagnostics' shows 'PRESENT'.
2. If the device was recently joined or re-joined, consider re-joining the device to Microsoft Entra ID:
   - Open an elevated command prompt.
   - Run: dsregcmd /leave
   - Restart the device.
   - Run: dsregcmd /join
3. If the issue persists, refer to the official documentation at https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd for further diagnostics.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
