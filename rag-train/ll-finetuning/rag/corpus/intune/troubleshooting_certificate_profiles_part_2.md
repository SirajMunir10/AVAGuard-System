# Troubleshooting: Certificate Profiles

**Domain:** Intune
**Subdomain:** Certificate Profiles
**Incident Type:** Troubleshooting

## Scenario / Query
How to locate and analyze logs for on-premises infrastructure supporting SCEP certificate profiles, including Intune Certificate Connector, NDES, and certification authority?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** SCEP certificate profiles with on-premises infrastructure including Microsoft Intune Certificate Connector, NDES on Windows Server, and certification authority

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the server that hosts NDES, open Event Viewer > Applications and Services Logs > Microsoft > Intune > CertificateConnectors > Admin and Operational to view Intune connector logs.
2. On the server that hosts NDES, navigate to c:\inetpub\logs\LogFiles\W3SVC1 to view IIS logs.

## Validation
1. On the NDES server, open Event Viewer and navigate to Applications and Services Logs > Microsoft > Intune > CertificateConnectors > Admin. Confirm that recent events show successful certificate requests (Event ID 1000 or similar) and no critical errors. 2. In the same Event Viewer path, check the Operational log for detailed request processing entries. 3. On the NDES server, browse to c:\inetpub\logs\LogFiles\W3SVC1 and open the most recent IIS log file. Verify that entries for the /certsrv/mscep/mscep.dll endpoint show HTTP 200 status codes and contain the client certificate request data.

## Rollback
1. If the logs indicate a misconfiguration, restore the original NDES configuration by reverting any changes made to the web.config file in c:\Program Files\Microsoft Intune\Certificate Connector\ or the IIS site bindings. 2. If the Certificate Connector service was restarted, restart it again using Services.msc or the command: net start IntuneCertificateConnector. 3. If the IIS logs were deleted or moved, restore them from backup if available, or reconfigure IIS logging to the original path via IIS Manager > Sites > Default Web Site > Logging.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-scep-certificate-profiles>
