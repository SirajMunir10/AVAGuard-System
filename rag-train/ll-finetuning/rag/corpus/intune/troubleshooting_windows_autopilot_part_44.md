# Troubleshooting: Windows Autopilot (0x81039023)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve TPM attestation failure on Windows 11 with error code 0x81039023 during pre-provisioning technician flow or self-deployment mode?

## Environment Context
- **Tenant Type:** Windows Autopilot
- **Configuration:** Windows 11 devices with TPM attestation

## Symptoms
- TPM attestation failure on Windows 11 during pre-provisioning technician flow or self-deployment mode

## Error Codes
- `0x81039023`

## Root Causes
1. Missing cumulative update KB5013943 or later on Windows 11 version 21H2

## Remediation Steps
1. Apply the May 2022 cumulative update for Windows 11, version 21H2 KB5013943 or later to the device

## Validation
1. Verify the installed OS build: run 'winver' or 'Get-ComputerInfo | Select-Object WindowsVersion, WindowsBuildLabEx'. Confirm the build is 22000.708 or later (KB5013943).
2. Check installed updates: run 'Get-HotFix | Where-Object {$_.HotFixID -eq "KB5013943"}' or check Settings > Windows Update > Update history.
3. Reattempt Autopilot pre-provisioning or self-deployment and confirm TPM attestation succeeds without error 0x81039023.
4. Optionally, run 'Get-Tpm' in PowerShell to verify TPM is ready and attestation status is successful.

## Rollback
1. If the update causes issues, uninstall KB5013943: go to Settings > Windows Update > Update history > Uninstall updates, select KB5013943, and click Uninstall.
2. Alternatively, run 'wusa /uninstall /kb:5013943' from an elevated command prompt and restart the device.
3. After rollback, confirm the device returns to its previous build (e.g., 22000.675 or earlier) via 'winver'.
4. Re-test Autopilot scenario; expect TPM attestation failure 0x81039023 to reappear, confirming rollback success.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
