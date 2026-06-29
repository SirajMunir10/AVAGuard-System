# Troubleshooting: Certificate Profiles

**Domain:** Intune
**Subdomain:** Certificate Profiles
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify problems in the communication and certificate provisioning workflow for SCEP certificate profiles?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** SCEP certificate profiles

## Symptoms
- Certificate provisioning failures
- Communication issues between devices and server infrastructure

## Error Codes
N/A

## Root Causes
1. Problems in the communication and certificate provisioning workflow

## Remediation Steps
1. Review log files from both the Server infrastructure and from devices
2. Refer to log files referenced in the 'Log files' section of the documentation for troubleshooting SCEP certificate profiles

## Validation
1. On a test device, trigger a manual sync of Intune policies and check the CertificateConnector.ps1 script output for 'Successfully processed request' messages. 2. On the NDES server, open Event Viewer > Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin and verify no Error events with ID 1000 or 1001. 3. From a device, run 'certlm.msc' and confirm the SCEP-issued certificate is present under Personal > Certificates with an Intune-issued issuer. 4. Use the SCEP reporting in Intune admin center: Devices > Monitor > Certificate Connector status to confirm the connector shows 'Active' and no pending requests.

## Rollback
1. If validation fails, revert any recent changes to the NDES server by restoring the web.config file from backup (located at %ProgramFiles%\Microsoft Intune\NDESConnector\NDESConnector.ps1.config). 2. On the NDES server, run 'iisreset' to restart IIS and clear any stuck SCEP requests. 3. In Intune admin center, navigate to Devices > Configuration profiles > SCEP profile, set 'Renewal threshold (%)' to a higher value (e.g., 20%) to reduce immediate renewal attempts. 4. If devices still fail, temporarily assign a different SCEP profile (with a different trusted CA) to affected device groups to isolate the issue.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-scep-certificate-profiles>
