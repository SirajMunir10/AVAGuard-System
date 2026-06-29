# Troubleshooting: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Troubleshooting

## Scenario / Query
How to view ASR events in the device timeline for a specific device in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 2 or Microsoft Defender for Business
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open the Device Inventory page at https://security.microsoft.com/machines.
2. On the appropriate tab of the Device Inventory page (for example, All devices or Computers & mobile), select a device by selecting the device name link.
3. In the details page that opens, select the Timeline tab.
4. On the Timeline tab, select Filter.
5. In the Filter flyout that opens, select ASR events from the Event group section, and then select Apply.
6. The default timeframe is 1 week, but you can also select 1 day, 3 days, 30 days, or a custom date range within 30 days.

## Validation
1. Navigate to https://security.microsoft.com/machines and open the Device Inventory page.
2. Select the specific device by clicking its name link.
3. On the device details page, click the Timeline tab.
4. Click Filter, then under Event group select 'ASR events' and click Apply.
5. Verify that ASR events are displayed in the timeline for the selected device.
6. Confirm the default timeframe is 1 week, and optionally test other timeframes (1 day, 3 days, 30 days, or a custom range within 30 days) to ensure events appear correctly.

## Rollback
1. If the timeline does not display ASR events, verify that the device is running a supported operating system (Windows 10, Windows 11, Windows Server 2016 or later) and has the required Microsoft Defender for Endpoint Plan 2 or Microsoft Defender for Business license.
2. Ensure the device is properly onboarded to Microsoft Defender for Endpoint and is actively reporting.
3. Check that ASR rules are enabled and configured via Group Policy, Intune, or Microsoft Defender for Cloud Apps.
4. If events still do not appear, review the device's event logs for ASR-related events (Event ID 1121 for block, 5007 for configuration changes) to confirm ASR is functioning.
5. If the issue persists, contact Microsoft Support with the device name and timeframe for further investigation.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-asr-rules>
