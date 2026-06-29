# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Windows Autopilot device provisioning failures caused by TPM attestation errors or ESP timeouts due to incorrect real-time clock?

## Environment Context
- **Tenant Type:** Any tenant using Windows Autopilot
- **Configuration:** Devices with real-time clock off by several minutes or more

## Symptoms
- Windows Autopilot device provisioning fails
- TPM attestation errors
- ESP timeouts

## Error Codes
N/A

## Root Causes
1. Real-time clock on the device is off by a significant amount of time (several minutes or more)

## Remediation Steps
1. Boot the device to the start of the out-of-box experience (OOBE)
2. Establish a network connection (wired or wireless)
3. Run the command: w32tm /resync /force to sync the time with the default time server (time.windows.com)

## Validation
1. Boot the device to the start of OOBE and establish network connectivity. 2. Open a command prompt (Shift+F10). 3. Run 'w32tm /query /status' and verify the 'Source' shows 'time.windows.com' and the time offset is less than 5 minutes. 4. Run 'w32tm /resync /force' and confirm output 'The command completed successfully.' 5. Re-run 'w32tm /query /status' to confirm time is synchronized. 6. Continue OOBE and monitor Autopilot provisioning to ensure no TPM attestation errors or ESP timeouts occur.

## Rollback
1. If time sync fails or causes issues, boot the device to OOBE and open command prompt (Shift+F10). 2. Run 'w32tm /config /manualpeerlist:pool.ntp.org /syncfromflags:manual /reliable:yes /update' to set an alternate NTP source. 3. Run 'net stop w32time && net start w32time' to restart the time service. 4. Run 'w32tm /resync' to attempt sync again. 5. If still failing, run 'w32tm /unregister' then 'w32tm /register' to re-register the service, then repeat steps 3-4. 6. If time cannot be corrected, proceed with manual time setting via 'date' and 'time' commands as a last resort, then retry Autopilot.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
