# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
DFCI enrollment fails for Professional editions of Windows 11, version 24H2 during OOBE

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows Autopilot deployment with DFCI enabled

## Symptoms
- DFCI can't be configured during the out-of-box experience (OOBE) on devices with Professional editions of Windows 11, version 24H2

## Error Codes
N/A

## Root Causes
1. DFCI enrollment fails for Professional editions of Windows 11, version 24H2

## Remediation Steps
1. For devices that have already been provisioned and have Professional editions of Windows 11, version 24H2, install KB5046740 or later to enroll in DFCI.
2. Devices with Professional editions of Windows 11, version 24H2 that have KB5046740 or later installed are automatically enrolled in DFCI after a reboot.
3. If DFCI needs to be configured during OOBE provisioning on 24H2 devices: During OOBE onboarding, ensure the device is upgraded to the Enterprise edition of Windows 11, version 24H2. After upgrading to the Enterprise edition of Windows 11, version 24H2, sync the device. Once the device is synced, reboot it to get it enrolled in DFCI.

## Validation
1. Verify the device is running Windows 11, version 24H2 Professional edition. Open Settings > System > About and confirm Edition and Version. Alternatively, run 'winver' from command prompt. 2. Check that KB5046740 or later is installed: Go to Settings > Windows Update > Update history, or run 'wmic qfe list brief /format:table' and look for KB5046740. 3. Reboot the device. 4. After reboot, confirm DFCI enrollment: In Intune, navigate to Devices > Windows > Windows enrollment > DFCI, and verify the device is listed as enrolled. Alternatively, on the device, run 'msinfo32' and check under 'BIOS Mode' for DFCI status. 5. If DFCI enrollment is still not shown, ensure the device has synced with Intune: In Intune, select the device and check 'Last check-in' is recent. On the device, go to Settings > Accounts > Access work or school > click the account > Info > Sync.

## Rollback
1. If DFCI enrollment fails after installing KB5046740, uninstall the update: Go to Settings > Windows Update > Update history > Uninstall updates, select KB5046740, and click Uninstall. Reboot the device. 2. If the device was upgraded to Enterprise edition during OOBE and DFCI enrollment fails, downgrade back to Professional edition: Reinstall Windows 11, version 24H2 Professional edition using installation media. 3. After rollback, verify the device returns to its previous state: Confirm edition and version via Settings > System > About, and check that DFCI is not enrolled (msinfo32 should show DFCI as 'Not supported' or 'Disabled'). 4. If the device was synced and rebooted after upgrade, and DFCI enrollment fails, perform a factory reset: Go to Settings > System > Recovery > Reset this PC, choose 'Remove everything', and reinstall Windows 11, version 24H2 Professional edition.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
