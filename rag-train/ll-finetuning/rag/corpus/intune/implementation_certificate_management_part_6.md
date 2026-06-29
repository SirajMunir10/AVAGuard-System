# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to configure SCEP certificate profiles with a Microsoft Certification Authority in Intune?

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
1. Setup a Network Device Enrollment Service (NDES) server for use with Intune.
2. Install the Certificate Connector for Microsoft Intune.

## Validation
1. On the NDES server, open the Certificate Connector UI from the system tray and verify the connector status shows 'Connected' and 'Active'.
2. In the Intune admin center, navigate to Tenant administration > Connectors and tokens > Certificate connectors and confirm the connector appears with a green checkmark and 'Active' status.
3. Create a test SCEP certificate profile (Devices > Configuration profiles > Create profile > Windows 10 and later > Templates > SCEP certificate) and assign it to a test device.
4. On the test device, run 'certlm.msc' and verify a certificate issued by your Microsoft CA appears under 'Personal' with the expected template name.
5. Check the NDES server's Application and Services Logs > Microsoft > Windows > ActiveDirectory-CertificateServices-Client-Lifecycle-System for successful enrollment events (Event ID 1006).

## Rollback
1. In the Intune admin center, go to Tenant administration > Connectors and tokens > Certificate connectors, select the connector, and click 'Delete' to remove the connector registration.
2. On the NDES server, open Control Panel > Programs and Features, uninstall 'Microsoft Intune Certificate Connector'.
3. If NDES was newly installed, uninstall the NDES role via Server Manager > Manage > Remove Roles and Features, deselecting 'Network Device Enrollment Service' under Active Directory Certificate Services.
4. Delete any SCEP certificate profiles created during testing from Intune (Devices > Configuration profiles > select profile > Delete).
5. On the CA, revoke any test certificates issued during validation using the Certification Authority snap-in (right-click certificate > All Tasks > Revoke Certificate).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
