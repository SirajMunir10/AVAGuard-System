# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect support logs from a Linux device using MDESupportTool.sh in a Live Response session?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Linux device with MDESupportTool.sh available

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. run MDESupportTool.sh -parameters "--bypass-disclaimer -d"
2. GetFile "/tmp/your_archive_file_name_here.zip"

## Validation
1. In the Live Response session, run: GetFile "/tmp/mde_support_tool_output.zip" (or the exact filename returned by MDESupportTool.sh). 2. Verify the file was downloaded successfully to your local machine. 3. Extract the archive and confirm it contains the expected log files (e.g., mdatp_*.log, diagnostic*.log). 4. Optionally, run: RunShell "ls -la /tmp/mde_support_tool_output.zip" to confirm the file exists on the device.

## Rollback
1. If the support log collection fails or causes issues, delete the generated archive from the device: RunShell "rm -f /tmp/mde_support_tool_output.zip". 2. If the MDESupportTool.sh script was interrupted, ensure no residual processes remain: RunShell "pkill -f MDESupportTool.sh" (if applicable). 3. Verify the device's Defender for Endpoint service is still running: RunShell "systemctl status mdatp" (or equivalent). 4. If the service is stopped, restart it: RunShell "systemctl restart mdatp".

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-collect-support-log>
