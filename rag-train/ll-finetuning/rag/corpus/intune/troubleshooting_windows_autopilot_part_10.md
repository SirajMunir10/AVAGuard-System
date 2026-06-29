# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Kiosk device profile not auto logging in after Windows Autopilot provisioning

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Kiosk device profile with auto logon enabled

## Symptoms
- After Windows Autopilot completes provisioning, the device stays on the sign-in screen prompting for credentials

## Error Codes
N/A

## Root Causes
1. Known issue in Windows Updates released in January 2023: Windows 11 version 22H2 KB5022303, Windows 11 version 21H2 KB5022287, Windows 10 version 22H2 KB5022282

## Remediation Steps
1. Manually enter the kiosk user credentials with the username kioskUser0 and no password
2. After the username is entered with no password, it should go to the desktop
3. Install cumulative updates released for Windows 11 in April 2023 (KB5025239 or later for version 22H2, KB5025224 or later for version 21H2) and Windows 10 in March 2023 (KB5023773 or later for version 22H2)

## Validation
This issue is fixed. For more information, see Auto logon for Kiosk device profile only partially fixed.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
