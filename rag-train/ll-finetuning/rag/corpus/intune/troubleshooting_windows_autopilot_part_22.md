# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix hash import failures due to invalid base64 padding in Windows Autopilot device hashes?

## Environment Context
- **Tenant Type:** Any
- **Configuration:** Windows Autopilot device hash import

## Symptoms
- Hash import fails due to invalid padding

## Error Codes
N/A

## Root Causes
1. Invalid base64 padding in device hash

## Remediation Steps
1. Replace both '=' with a single 'A' character, then try again
2. Add another '=' character at the end, then try again
3. If the hash is valid, replace the collected hash with the new padded hash then try to import again

## Validation
1. Verify the corrected hash has valid base64 padding by running: `echo '<corrected_hash>' | base64 --decode 2>&1` and confirming no 'invalid padding' error. 2. Attempt to import the corrected hash using the Windows Autopilot deployment program or PowerShell cmdlet `Import-AutopilotDevice` and confirm no 'invalid padding' error. 3. Check the Autopilot device import history in the Microsoft Intune admin center (Devices > Enroll devices > Windows enrollment > Devices) to ensure the device appears without errors.

## Rollback
1. If the corrected hash still fails, revert to the original hash by replacing the added 'A' or extra '=' with the original padding. 2. Re-import the original hash to confirm the failure reproduces. 3. If the import succeeds unexpectedly, remove the device from Autopilot using `Remove-AutopilotDevice` and re-import the original hash to restore the previous state.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
