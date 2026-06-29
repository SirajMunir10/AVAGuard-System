# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to configure PKCS imported certificates with a Microsoft Certification Authority in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Microsoft Certification Authority

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Install the Certificate Connector for Microsoft Intune.
2. Export certificates from the certification authority and then import them to Microsoft Intune.
3. See the PFXImport PowerShell project.

## Validation
1. Verify that the Certificate Connector for Microsoft Intune is installed and running: Check the Windows Services console for 'Intune Certificate Connector' service status as 'Running'. 2. Confirm the connector is registered in the Intune admin center: Navigate to Tenant administration > Connectors and tokens > Certificate connectors and verify the connector appears with a status of 'Active'. 3. Validate that PKCS imported certificates are available: In the Intune admin center, go to Devices > Configuration profiles > Create profile > Windows 10 and later > Templates > PKCS imported certificate. Ensure the profile creation wizard lists the imported certificates from the certification authority. 4. Test certificate deployment: Assign the PKCS imported certificate profile to a test device and verify the certificate is installed by running 'certlm.msc' on the device and checking the Personal store for the expected certificate.

## Rollback
1. Remove the PKCS imported certificate profile: In the Intune admin center, navigate to Devices > Configuration profiles, select the PKCS imported certificate profile, and click 'Delete'. 2. Uninstall the Certificate Connector: On the server running the connector, open Control Panel > Programs and Features, select 'Intune Certificate Connector', and click 'Uninstall'. 3. Remove imported certificates from Intune: If certificates were imported via the PFXImport PowerShell project, use the Remove-PfxImportCertificate cmdlet to delete them. 4. Revert to previous certificate management method: If a different certificate solution was previously used, reapply the original configuration profiles and connectors.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
