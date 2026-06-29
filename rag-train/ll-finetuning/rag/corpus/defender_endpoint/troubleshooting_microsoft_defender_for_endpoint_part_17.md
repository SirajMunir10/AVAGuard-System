# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect support logs from a machine that is not communicating with Microsoft Defender for Endpoint cloud services or does not appear in the Microsoft Defender for Endpoint portal?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Machine is not communicating with Microsoft Defender for Endpoint cloud services
- Machine does not appear in Microsoft Defender for Endpoint portal as expected

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Download the latest preview version of MDE Client Analyzer from https://aka.ms/MDEClientAnalyzerPreview
2. Gather data locally on the machine using the MDE Client Analyzer
3. Verify client connectivity to Microsoft Defender for Endpoint service URLs as described in 'Verify client connectivity to Microsoft Defender for Endpoint service URLs'

## Validation
1. On the affected machine, run the MDE Client Analyzer with the command: 'MDEClientAnalyzerPreview.cmd' and confirm that the tool completes without errors and generates a zip file (e.g., MDEClientAnalyzerResult.zip) in the same directory. 2. Open the generated HTML report (MDEClientAnalyzerResult.htm) and verify that the 'Connectivity' section shows 'Pass' for all required Microsoft Defender for Endpoint service URLs (e.g., *.endpoint.microsoft.com, *.events.data.microsoft.com). 3. Check the 'Machine Info' section to confirm the machine's tenant ID matches your organization's tenant. 4. After remediation, verify the machine appears in the Microsoft Defender for Endpoint portal under 'Devices' within 1-2 hours.

## Rollback
1. If the machine still does not communicate after running the analyzer, remove any proxy or firewall changes made during troubleshooting by reverting to the original configuration. 2. Uninstall any MDE Client Analyzer files by deleting the downloaded 'MDEClientAnalyzerPreview' folder from the machine. 3. If the machine was onboarded using a script, re-run the original onboarding script from the Microsoft Defender for Endpoint portal (Settings > Endpoints > Onboarding) to restore the previous state. 4. Restart the Microsoft Defender for Endpoint service with the command: 'net start WinDefend' (if it was stopped) and verify the service status is 'Running'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-collect-support-log>
