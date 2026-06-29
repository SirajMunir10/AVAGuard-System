# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to set up certificate-based authentication for network or VPN access using Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Device or user certificates, 802.1x, VPN servers

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use SCEP or PKCS to provision device or user certificates.
2. Deploy the certificates to devices for network authentication (e.g., 802.1x) or VPN server authentication.

## Validation
1. Verify that a trusted certificate profile (SCEP or PKCS) is assigned to the correct user or device groups in the Microsoft Intune admin center (Devices > Configuration profiles).
2. On a target device, confirm the certificate is installed by running 'certlm.msc' (Local Machine) or 'certmgr.msc' (Current User) and locating the issued certificate under 'Personal > Certificates'.
3. For 802.1x network authentication, test connectivity to a protected network resource (e.g., internal website) and confirm no certificate errors appear.
4. For VPN authentication, initiate a VPN connection and verify successful authentication using the certificate (check VPN logs or client status).
5. Review Intune reporting (Devices > Monitor > Certificate profiles) to ensure the profile was successfully delivered and installed.

## Rollback
1. In the Microsoft Intune admin center, navigate to Devices > Configuration profiles and locate the SCEP or PKCS certificate profile.
2. Change the assignment of the profile to 'Not assigned' or remove the targeted user/device groups to stop further certificate provisioning.
3. On affected devices, manually delete the issued certificate via 'certlm.msc' or 'certmgr.msc' (right-click the certificate > Delete).
4. If the certificate profile was deployed via a Group Policy or third-party MDM, revoke the certificate from the issuing CA (Certification Authority) to prevent reuse.
5. Revert any network or VPN configuration changes that were made to trust the new certificates (e.g., remove the CA certificate from trusted root stores if added).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
