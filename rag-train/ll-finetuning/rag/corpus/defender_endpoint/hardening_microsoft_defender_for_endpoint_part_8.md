# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
How to add an indicator to block or allow a file in Microsoft Defender for Endpoint to prevent further propagation of an attack?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Microsoft Defender Antivirus with Cloud-delivered protection enabled; Anti-malware client version 4.18.1901.x or later; devices on Windows 10 version 1703 or later, or Windows 11

## Symptoms
- Potentially malicious portable executable (PE) files need to be blocked from being read, written, or executed on devices

## Error Codes
N/A

## Root Causes
1. Suspected malware or potentially malicious files may propagate in the organization

## Remediation Steps
1. Ensure Microsoft Defender Antivirus and Cloud-delivered protection are enabled (see Manage cloud-delivered protection)
2. Ensure Anti-malware client version is 4.18.1901.x or later
3. Ensure devices are on Windows 10 version 1703 or later, or Windows 11
4. Add an indicator to block or allow the file (the PE file must be in the device timeline)
5. Note: The allow or block function cannot be done on files if the file's classification exists on the device's cache prior to the action
6. Note: There may be a couple of minutes of latency between the time the action is taken and the actual file being blocked

## Validation
1. Confirm that Microsoft Defender Antivirus and Cloud-delivered protection are enabled by running the following PowerShell command on a test device: Get-MpPreference | Select-Object -Property CloudBlockLevel, CloudTimeout. Ensure CloudBlockLevel is not '0' (disabled) and CloudTimeout is set appropriately.
2. Verify the anti-malware client version by running: Get-MpComputerStatus | Select-Object AMProductVersion. Confirm the version is 4.18.1901.x or later.
3. Check the Windows version: (Get-CimInstance Win32_OperatingSystem).Version. Ensure it is 10.0.15063 (Windows 10 version 1703) or later, or Windows 11.
4. In Microsoft Defender for Endpoint portal (security.microsoft.com), navigate to Settings > Endpoints > Indicators > File hashes. Confirm the indicator for the target file is listed with the correct action (Block or Allow) and scope.
5. On a test device, attempt to execute the file (if blocking) or verify it is allowed (if allowing). For a block, the file should be prevented from running and an alert should appear in the device timeline. For an allow, the file should run without being blocked.
6. Check the device timeline in the portal for the test device to confirm the indicator action was applied (look for 'File blocked' or 'File allowed' events).

## Rollback
1. In Microsoft Defender for Endpoint portal, go to Settings > Endpoints > Indicators > File hashes.
2. Locate the indicator you added for the file.
3. Select the indicator and choose 'Remove' or 'Delete' to delete the indicator entirely.
4. Alternatively, if you need to change the action (e.g., from Block to Allow), edit the indicator and update the Action field accordingly.
5. Wait a few minutes for the change to propagate (as noted, there may be latency).
6. On a test device, attempt to execute the file to confirm the rollback is effective: the file should no longer be blocked (if removed) or should now be blocked (if changed to Block).
7. Verify in the device timeline that the indicator action has been updated or removed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
