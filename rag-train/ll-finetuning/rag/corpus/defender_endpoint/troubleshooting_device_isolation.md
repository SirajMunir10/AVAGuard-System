# Troubleshooting: Device Isolation

**Domain:** Defender for Endpoint
**Subdomain:** Device Isolation
**Incident Type:** Troubleshooting

## Scenario / Query
How to forcibly release a device from isolation when it becomes unresponsive?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Device must be running Windows with specific versions: Windows 10 21H2 and 22H2 with KB5023773, Windows 11 version 21H2 with KB5023774, Windows 11 version 22H2 with KB5023778

## Symptoms
- Isolated device becomes unresponsive

## Error Codes
N/A

## Root Causes
1. Device isolation may cause unresponsiveness in some cases

## Remediation Steps
1. On the device page, select Download script to force-release a device from isolation from the action menu.
2. In the pane on the right, select Download script.
3. Run the downloaded script on the specific device to forcibly release it from isolation.

## Validation
1. Confirm the device is currently isolated: In Microsoft Defender for Endpoint, navigate to the device page and verify the 'Isolation status' shows 'Isolated'.
2. After running the force-release script, check the device's isolation status again: It should change to 'Not isolated'.
3. Verify the device is responsive: Attempt to ping the device or connect via remote management tools (e.g., WinRM, RDP) to confirm network connectivity is restored.
4. Check the device's event logs for successful isolation release: Look for Event ID 5000 or related entries under 'Microsoft-Windows-Windows Defender/Operational' indicating the isolation policy was removed.

## Rollback
1. If the device remains unresponsive after running the force-release script, attempt a manual reboot of the device via physical access or out-of-band management (e.g., iDRAC, iLO).
2. If the device still does not respond, re-isolate the device from the Microsoft Defender portal to ensure it is protected while troubleshooting: On the device page, select 'Isolate device' and choose the appropriate isolation type.
3. Contact Microsoft Support for further assistance if the device cannot be recovered, providing the script output and device logs.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
