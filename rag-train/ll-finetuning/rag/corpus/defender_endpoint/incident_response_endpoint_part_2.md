# Incident Response: Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How to stop and quarantine a file on Microsoft Defender for Endpoint devices?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** N/A

## Symptoms
- File identified as malicious or suspicious in an alert
- File needs to be stopped and quarantined on devices

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the file you want to stop and quarantine from Alerts (select corresponding links from Description or Details in Alert Story timeline) or Search box (select File from drop-down menu and enter file name).
2. Go to the top bar and select Stop and Quarantine File.
3. Specify a reason, then select Confirm.
4. The Action center shows submission information: Submission time, Success (number of devices where file was stopped and quarantined), Failed (number of devices where action failed and details about failure), Pending (number of devices where file is yet to be stopped and quarantined).
5. Select any status indicator to view more information about the action (e.g., select Failed to see where the action failed).

## Validation
1. Navigate to the Action center in Microsoft Defender for Endpoint (https://security.microsoft.com/action-center).
2. Verify that the 'Stop and Quarantine File' action appears in the history with a status of 'Completed' or 'Success' for the target devices.
3. On an affected device, run the following PowerShell command as Administrator to confirm the file is no longer present in its original location and is quarantined:
   Get-MpThreatDetection | Where-Object {$_.Resources -like '*<filename>*'}
   (Replace <filename> with the actual file name.)
4. Check that the file is listed in the quarantine folder (typically C:\ProgramData\Microsoft\Windows Defender\Quarantine) or via the Windows Security app under 'Protection history'.

## Rollback
1. In Microsoft Defender for Endpoint, go to the Action center and locate the 'Stop and Quarantine File' action.
2. If the action failed or caused issues, select the action and choose 'Undo' or 'Allow' to restore the file from quarantine (if available).
3. Alternatively, on an affected device, open Windows Security > Virus & threat protection > Protection history, find the quarantined file, and select 'Restore'.
4. Use the following PowerShell command as Administrator to restore the file from quarantine:
   Restore-MpThreatDetection -ThreatID <ThreatID>
   (Obtain the ThreatID from Get-MpThreatDetection output.)
5. Verify the file is restored to its original location and is accessible.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
