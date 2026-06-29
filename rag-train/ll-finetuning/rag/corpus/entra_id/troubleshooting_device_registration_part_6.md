# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to check Windows Hello for Business prerequisites using dsregcmd /status?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Hello for Business policy enabled

## Symptoms
- Windows Hello for Business enrollment not triggering
- WHFB setup issues

## Error Codes
N/A

## Root Causes
1. Device not joined to Microsoft Entra ID
2. User not present in Microsoft Entra ID
3. WHFB policy not enabled on device
4. WHFB enrollment triggered by custom mechanism instead of platform
5. Device does not meet hardware requirements for WHFB
6. User logged in remotely instead of directly
7. Certificate enrollment authority not configured
8. No enterprise PRT for user
9. AD FS not supporting WHFB or logon certificate template not available
10. Login certificate template state invalid

## Remediation Steps
1. Run dsregcmd /status to check NGC prerequisites section
2. Verify IsDeviceJoined is set to YES
3. Verify IsUserAzureAD is set to YES
4. Verify PolicyEnabled is set to YES
5. Verify PostLogonEnabled is set to YES (if NO, WHFB enrollment is triggered by custom mechanism)
6. Verify DeviceEligible is set to YES
7. Verify SessionIsNotRemote is set to YES
8. For Certificate Trust deployment: check CertEnrollment state (enrollment authority or mobile device management)
9. For Certificate Trust deployment: check AdfsRefreshToken state
10. For Certificate Trust deployment: check AdfsRaIsReady state
11. For Certificate Trust deployment: check LogonCertTemplateReady state
12. Check PreReqResult state (Will Provision if enrollment will launch on next sign-in)

## Validation
PreReqResult set to Will Provision indicates successful prerequisites evaluation

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
