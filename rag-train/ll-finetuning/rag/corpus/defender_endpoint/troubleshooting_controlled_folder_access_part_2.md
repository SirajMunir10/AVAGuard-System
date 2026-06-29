# Troubleshooting: Controlled Folder Access (ID 1124)

**Domain:** Defender for Endpoint
**Subdomain:** Controlled Folder Access
**Incident Type:** Troubleshooting

## Scenario / Query
Which event log and event ID records attempts to write to protected disk sectors?

## Environment Context
- **Tenant Type:** Any
- **Configuration:** Audit disk modification only

## Symptoms
N/A

## Error Codes
- `ID 1124`

## Root Causes
N/A

## Remediation Steps
N/A

## Validation
Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. Verify that event ID 1124 is logged when an attempt to write to a protected disk sector occurs. Confirm that the event source is 'Microsoft-Windows-Windows Defender' and the event message indicates a blocked write to a protected sector.

## Rollback
If validation fails or the event ID 1124 is not being generated as expected, ensure that Controlled Folder Access is enabled via Windows Security or Group Policy. Navigate to Windows Security > Virus & threat protection > Manage ransomware protection and confirm Controlled Folder Access is turned on. If it is off, enable it. Alternatively, use PowerShell: Set-MpPreference -EnableControlledFolderAccess Enabled. Then re-test the write attempt to a protected disk sector and re-check event ID 1124.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/enable-controlled-folders>
