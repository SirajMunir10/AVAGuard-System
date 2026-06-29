# Troubleshooting: Device Identity (0xc000006d)

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to find the error code from dsregcmd output for a failed PRT acquisition on a Windows device?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows 10 May 2021 update (version 21H1) or later

## Symptoms
- AzureAdPrt field shows NO
- Attempt Status shows 0xc000006d
- Server Error Code shows invalid_grant
- Server Error Description shows AADSTS50126: Error validating credentials due to invalid username or password

## Error Codes
- `0xc000006d`
- `AADSTS50126`

## Root Causes
1. Invalid username or password during PRT acquisition

## Remediation Steps
N/A

## Validation
1. Open Command Prompt as Administrator and run 'dsregcmd /status'. 2. Verify that the 'AzureAdPrt' field shows 'YES'. 3. Confirm that 'Attempt Status' is not '0xc000006d' and 'Server Error Code' is not 'invalid_grant'. 4. Check that 'Server Error Description' does not contain 'AADSTS50126'. 5. Optionally, run 'dsregcmd /status' again after a user sign-out/sign-in to ensure PRT acquisition succeeds.

## Rollback
1. If the remediation fails, revert any changes made to the user's password or account credentials. 2. If a password reset was performed, restore the previous password or re-enable the original account. 3. If conditional access policies were modified, revert to the previous policy configuration. 4. Run 'dsregcmd /status' to confirm the error codes (0xc000006d, AADSTS50126) reappear, indicating rollback to the original state.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
