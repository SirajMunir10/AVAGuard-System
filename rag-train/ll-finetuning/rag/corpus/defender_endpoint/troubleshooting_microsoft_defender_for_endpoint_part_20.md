# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to run the XMDE Client Analyzer via Live Response to collect support logs?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Live Response session enabled; XMDE Client Analyzer installed in default location /tmp/XMDEClientAnalyzerBinary/ClientAnalyzer or /tmp/XMDEClientAnalyzer

## Symptoms
- Need to collect support logs from a machine using Live Response
- XMDE Client Analyzer or Python cannot be run directly in Live Response

## Error Codes
N/A

## Root Causes
1. Live Response does not support running the XMDE Client Analyzer or Python directly

## Remediation Steps
1. Create a bash file named MDESupportTool.sh with the following content for the Binary Client Analyzer: #! /usr/bin/bash
echo "cd /tmp/XMDEClientAnalyzerBinary/ClientAnalyzer"
cd /tmp/XMDEClientAnalyzerBinary/ClientAnalyzer
echo "Running MDESupportTool"
./MDESupportTool $@
2. Alternatively, create a bash file named MDESupportTool.sh with the following content for the Python Client Analyzer: #! /usr/bin/bash
echo "cd /tmp/XMDEClientAnalyzer"
cd /tmp/XMDEClientAnalyzer
echo "Running mde_support_tool"
./mde_support_tool.sh $@
3. Initiate a Live Response session on the machine you need to investigate.
4. Select Upload file to library.
5. Select Choose file.
6. Select the downloaded file named MDESupportTool.sh, and then select Confirm.
7. While still in the Live Response session, use the following commands to run the analyzer and collect the resulting file.

## Validation
1. Initiate a Live Response session on the target machine. 2. Run the command: `run MDESupportTool.sh` and verify that the script executes without errors and displays the expected output (e.g., 'Running MDESupportTool' or 'Running mde_support_tool'). 3. Check that the support log archive (e.g., `MDESupportToolResult.zip` or similar) is created in the current directory by running `ls -la *.zip`. 4. Download the generated archive using the `getfile` command in Live Response and confirm the file is retrievable.

## Rollback
1. If the script fails to execute or causes unexpected behavior, terminate the Live Response session by closing the session in the Microsoft Defender portal. 2. Delete the uploaded `MDESupportTool.sh` file from the Live Response library by navigating to the library, selecting the file, and choosing 'Delete'. 3. If the script created any partial output files on the machine, remove them by running `rm -f /tmp/XMDEClientAnalyzerBinary/ClientAnalyzer/*.zip` or `rm -f /tmp/XMDEClientAnalyzer/*.zip` (depending on the analyzer type) via a new Live Response session. 4. Revert to the original state by ensuring no residual processes from the script remain (e.g., `pkill -f MDESupportTool` if needed).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-collect-support-log>
