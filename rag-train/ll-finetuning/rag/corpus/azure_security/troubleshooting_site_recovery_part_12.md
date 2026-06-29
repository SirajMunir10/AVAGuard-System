# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect logs for advanced troubleshooting of Azure Site Recovery for Hyper-V to Azure replication?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Hyper-V Site Protection with Azure Site Recovery

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For VMM, perform Site Recovery log collection using the Support Diagnostics Platform (SDP) tool.
2. Enable logging for the Azure Site Recovery in Hyper-V Site Protection.

## Validation
1. Verify that the SDP tool has been executed on the VMM server and confirm the output log file (e.g., a .cab or .zip file) is generated in the specified output directory.
2. Check that the Azure Site Recovery Provider log (located at %ProgramData%\Microsoft Azure Site Recovery\Logs) contains entries with timestamps matching the troubleshooting period.
3. For Hyper-V hosts, confirm that the 'Enable-AzureSiteRecoveryProviderLogging' cmdlet has been run and that the log files are present in the default path: %SystemRoot%\System32\LogFiles\ASR.

## Rollback
1. If the SDP tool was run and caused performance issues, stop any related processes (e.g., SDP.exe) and delete the generated log files from the output directory.
2. To disable verbose logging on the Hyper-V host, run the cmdlet: Disable-AzureSiteRecoveryProviderLogging.
3. If the Azure Site Recovery Provider log collection is no longer needed, delete or archive the log files from %ProgramData%\Microsoft Azure Site Recovery\Logs to free disk space.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
