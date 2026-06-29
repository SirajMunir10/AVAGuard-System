# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How do I install the XMDE Client Analyzer on a Linux machine using a bash script when the machine has direct internet access?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Machine must have direct internet access to download from https://go.microsoft.com/fwlink/?linkid=2297517

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a bash file named InstallXMDEClientAnalyzer.sh and paste the following content: #! /usr/bin/bash
2. echo 'Starting Client Analyzer Script. Running As:'
3. whoami
4. echo 'Getting XMDEClientAnalyzerBinary'
5. wget --quiet -O /tmp/XMDEClientAnalyzerBinary.zip https://go.microsoft.com/fwlink/?linkid=2297517
6. echo 'C65A4E4C6851D130942BFACD147A9D18B8A92B4F50FACF519477FD1C41A1C323 /tmp/XMDEClientAnalyzerBinary.zip' | sha256sum -c
7. echo 'Unzipping XMDEClientAnalyzerBinary.zip'
8. unzip -q /tmp/XMDEClientAnalyzerBinary.zip -d /tmp/XMDEClientAnalyzerBinary
9. echo 'Unzipping SupportToolLinuxBinary.zip'
10. unzip -q /tmp/XMDEClientAnalyzerBinary/XMDEClientAnalyzer/SupportToolLinuxBinary.zip -d /tmp/XMDEClientAnalyzerBinary/ClientAnalyzer
11. echo 'MDESupportTool installed at /tmp/XMDEClientAnalyzerBinary/ClientAnalyzer'

## Validation
1. Verify the script file exists: ls -l InstallXMDEClientAnalyzer.sh
2. Check script permissions: stat -c '%a' InstallXMDEClientAnalyzer.sh (should be 755 or executable)
3. Run the script: bash InstallXMDEClientAnalyzer.sh
4. Confirm the binary was downloaded: ls -l /tmp/XMDEClientAnalyzerBinary.zip
5. Validate the SHA256 hash matches: sha256sum /tmp/XMDEClientAnalyzerBinary.zip | grep -q 'C65A4E4C6851D130942BFACD147A9D18B8A92B4F50FACF519477FD1C41A1C323' && echo 'Hash match' || echo 'Hash mismatch'
6. Verify extraction: ls /tmp/XMDEClientAnalyzerBinary/ClientAnalyzer/MDESupportTool
7. Confirm the tool is executable: test -x /tmp/XMDEClientAnalyzerBinary/ClientAnalyzer/MDESupportTool && echo 'Tool is executable'

## Rollback
1. Remove the downloaded zip file: rm -f /tmp/XMDEClientAnalyzerBinary.zip
2. Remove the extracted directory: rm -rf /tmp/XMDEClientAnalyzerBinary
3. Remove the script file: rm -f InstallXMDEClientAnalyzer.sh
4. Verify cleanup: ls -l /tmp/XMDEClientAnalyzerBinary.zip /tmp/XMDEClientAnalyzerBinary InstallXMDEClientAnalyzer.sh 2>&1 | grep -q 'No such file' && echo 'Cleanup successful'

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-collect-support-log>
