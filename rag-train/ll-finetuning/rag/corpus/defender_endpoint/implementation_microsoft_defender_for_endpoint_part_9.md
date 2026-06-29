# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to respond to detected attacks by isolating devices or collecting an investigation package in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** Subscription must include Defender for Endpoint Plan 2 to have all response actions described in the article.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to a specific device page from any of the following views: Alerts queue (select the device name beside the device icon), Devices list (select the heading of the device name), or Search box (select Device from the drop-down menu and enter the device name).
2. Use response actions available along the top of the device page: Manage tags, Initiate automated investigation, Initiate live response Session, Collect investigation package, Run antivirus scan, Restrict app execution, Isolate device, Contain device, Consult a threat expert.
3. For Defender for Endpoint Plan 1, only the following manual response actions are included: Run antivirus scan, Isolate device, Stop and quarantine a file, Add an indicator to block or allow a file.
4. Note: Microsoft Defender for Business does not include the 'Stop and quarantine a file' action at this time.
5. After taking action on devices, check activity details on the Action center.

## Validation
1. Confirm the device is isolated: Run 'Get-MpPreference' on the device and verify 'DisableRealtimeMonitoring' is false and network connectivity is blocked. 2. Check Action center in Microsoft Defender for Endpoint (https://security.microsoft.com/action-center) to see the action status as 'Completed'. 3. For investigation package, verify the package was downloaded successfully by checking the file location specified in the Action center details.

## Rollback
1. Release isolation: On the device page, select 'Release from isolation' from the response actions menu. 2. For investigation package, no rollback is needed; delete the downloaded package if desired. 3. If isolation fails, restart the device and retry isolation from the portal.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
