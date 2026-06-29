# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How do I run the XMDE Client Analyzer execution script multiple times after a single installation using Live Response?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Due to limited commands available in Live Response, steps must be executed in a bash script, splitting installation and execution portions.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run the install script once to install the XMDE Client Analyzer.
2. Run the execution script multiple times as needed.

## Validation
1. From Live Response, run the execution script (e.g., 'bash XMDE_Client_Analyzer_exec.sh') and confirm it completes without errors. 2. Run the same execution script a second time and verify it also completes successfully. 3. Check that the output files (e.g., MDEClientAnalyzerResult.zip) are generated after each run. 4. Optionally, inspect the script's exit code or log output to ensure no failures.

## Rollback
1. If the execution script fails, re-run the install script from Live Response (e.g., 'bash XMDE_Client_Analyzer_install.sh') to reinstall the analyzer. 2. If issues persist, delete the analyzer directory (e.g., 'rm -rf /tmp/MDEClientAnalyzer') and reinstall. 3. If the machine becomes unresponsive, restart the device and reattempt the installation and execution steps.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-collect-support-log>
