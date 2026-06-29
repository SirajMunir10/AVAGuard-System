# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How to remotely initiate a Microsoft Defender Antivirus scan on a device as part of an investigation or response process?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** macOS and Linux client version 101.98.84 and above

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select 'Run antivirus scan' from the device actions menu.
2. Choose the scan type: quick or full.
3. Add a comment to document the action.
4. Confirm the scan to initiate it.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to 'Assets' > 'Devices' and locate the target device.
3. Click on the device name to open its details page.
4. In the 'Device actions' menu, verify that 'Run antivirus scan' is listed and the scan type (quick or full) was selected.
5. Check the 'Action center' (https://security.microsoft.com/action-center) to confirm the scan action is in 'Completed' status.
6. On the device, verify that Microsoft Defender Antivirus scan logs show the scan was initiated (e.g., event ID 1006 for detections, or scan completion events).

## Rollback
1. If the scan was initiated in error, no direct rollback exists; however, you can stop a running scan by running the following command on the device (requires local admin):
   - On Windows: 'Stop-MpScan' in PowerShell.
   - On macOS/Linux: 'sudo mdatp scan cancel' (for client version 101.98.84 and above).
2. If the scan caused performance issues, wait for it to complete or cancel it as above.
3. If the scan triggered false positive detections, submit the file to Microsoft for analysis and add exclusions if necessary.
4. Document the incident and any actions taken in the incident response notes.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
