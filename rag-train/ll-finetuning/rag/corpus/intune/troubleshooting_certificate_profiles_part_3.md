# Troubleshooting: Certificate Profiles

**Domain:** Intune
**Subdomain:** Certificate Profiles
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect and review logs for SCEP certificate profile issues on Android devices in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** SCEP certificate profiles, Android enrollment types

## Symptoms
- SCEP certificate profile issues on Android devices

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure Verbose Logging is enabled, then reproduce the issue.
2. For personally owned devices with a work profile (BYOD): review the OMADM.log file. To collect the OMADM.log file from a device, see Upload and email logs using a USB cable. You can also upload and email logs to support.
3. For corporate-owned work profile (COPE), fully managed (COBO), or dedicated devices (COSU): review the CloudExtension.log file.

## Validation
1. On the affected Android device, navigate to Settings > About Phone > Build Number and tap 7 times to enable Developer Options. 2. Go to Developer Options and enable 'Verbose logging' for the Company Portal app. 3. Reproduce the SCEP certificate issue (e.g., attempt to enroll or access a resource requiring the certificate). 4. For BYOD devices: Collect the OMADM.log file via USB cable (Settings > Company Portal > Export logs) and verify it contains entries related to SCEP certificate request/response. 5. For COPE/COBO/COSU devices: Collect the CloudExtension.log file from /data/data/com.microsoft.windowsintune.companyportal/files/ using a file manager or ADB, and confirm it includes SCEP-related error or success messages. 6. Check that the logs show the expected certificate template, issuing CA, and any failure codes (e.g., 0x80070057 for invalid parameters).

## Rollback
1. On the device, go to Developer Options and disable 'Verbose logging' for the Company Portal app to reduce log overhead. 2. Delete any collected log files (OMADM.log or CloudExtension.log) from the device storage to free space. 3. If logging was enabled via a configuration profile, remove or disable that profile from the Intune console (Devices > Configuration profiles > select profile > Properties > Disable). 4. Reboot the device to clear any temporary logging buffers. 5. Confirm that no sensitive certificate data remains in the logs by clearing the Company Portal app cache (Settings > Apps > Company Portal > Storage > Clear Cache).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-scep-certificate-profiles>
