# Troubleshooting: Windows Enrollment (OOBEIDPS)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the 'Something went wrong. OOBEIDPS' error during Windows Autopilot enrollment?

## Environment Context
- **Tenant Type:** Any
- **Configuration:** Windows Autopilot deployment

## Symptoms
- Error message: 'Something went wrong. OOBEIDPS' appears during Windows Autopilot enrollment

## Error Codes
- `OOBEIDPS`

## Root Causes
1. A proxy, firewall, or other network device is blocking access to the Identity Provider (IdP)

## Remediation Steps
1. Make sure that the required access to internet-based services for Autopilot isn't blocked. For more information, see Windows Autopilot networking requirements.

## Validation
1. On a test device that previously encountered the OOBEIDPS error, initiate a fresh Windows Autopilot reset or redeployment. 2. During the out-of-box experience, confirm that the device reaches the sign-in page for the organization's Identity Provider (e.g., Azure AD or Microsoft Entra ID) without displaying the 'Something went wrong. OOBEIDPS' error. 3. From a management console (e.g., Microsoft Intune admin center), verify that the device appears as an Autopilot-enrolled device and that its enrollment status shows as 'Enrolled' or 'Assigned'. 4. Optionally, run a network connectivity test from the device (e.g., using Test-NetConnection or a browser) to confirm that endpoints listed in Windows Autopilot networking requirements (such as login.microsoftonline.com, aadcdn.msauth.net, etc.) are reachable and not blocked.

## Rollback
1. If the remediation fails and the OOBEIDPS error persists, revert any recent changes made to proxy, firewall, or network device rules that were intended to unblock access to the Identity Provider. 2. Restore the original network configuration (e.g., reapply previous firewall rules or proxy exceptions) to ensure other services are not inadvertently affected. 3. If the device is stuck in the error state, perform a hard reset (press and hold the power button) to restart the out-of-box experience, then attempt enrollment again after confirming network access is restored to its prior state. 4. Document the failure and escalate to network or security teams for further analysis of traffic logs to identify remaining blocks.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
