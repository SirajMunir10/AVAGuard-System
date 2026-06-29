# Troubleshooting: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Troubleshooting

## Scenario / Query
How to query ASR rule events in Advanced Hunting using KQL?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 2
- **Configuration:** Advanced hunting enabled

## Symptoms
- Need to extract ASR rule information from DeviceEvents table
- Need to create reports on ASR rule audit or block events

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to Advanced hunting page at https://security.microsoft.com/v2/advanced-hunting
2. Use the DeviceEvents table to query ASR rule events
3. Run sample query: DeviceEvents | where Timestamp > ago(30d) | where ActionType startswith "Asr" | summarize EventCount=count() by ActionType
4. To focus on a specific rule, change the filter for ActionType and replace the summarize line with a project line containing desired fields
5. Example for Office child process rule: DeviceEvents | where (ActionType startswith "AsrOfficechild") | extend RuleId=extractjson("$Ruleid", AdditionalFields, typeof(string)) | project DeviceName, FileName, FolderPath, ProcessCommandLine, InitiatingProcessFileName, InitiatingProcessCommandLine

## Validation
Query returns ASR rule events from the last 30 days with ActionType starting with 'Asr'

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-asr-rules>
