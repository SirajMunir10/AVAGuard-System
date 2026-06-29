# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to deploy certificates using trusted certificate profiles, SCEP, PKCS, and PKCS imported certificate profiles in Intune?

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
1. Deploy certificates by using the following mechanisms: Trusted certificate profiles to deploy the Trusted Root CA certificate from your root or intermediate (issuing) CA to devices
2. SCEP certificate profiles
3. PKCS certificate profiles
4. PKCS imported certificate profiles

## Validation
1. Confirm that the trusted root CA certificate profile is assigned and applied: In the Intune admin center, navigate to Devices > Configuration profiles, select the trusted certificate profile, and verify its assignment status shows 'Succeeded' for targeted devices. On a test device, open the certificate store (certlm.msc) and confirm the root CA certificate appears under 'Trusted Root Certification Authorities'. 2. For SCEP profiles: In Intune, go to Devices > Configuration profiles, select the SCEP profile, and check the device status. On a test device, run 'certutil -store My' and verify a certificate issued by the CA is present with the correct template. 3. For PKCS profiles: In Intune, verify the PKCS profile status shows 'Succeeded'. On a test device, run 'certlm.msc' and confirm the certificate appears under 'Personal' with the expected issuer. 4. For PKCS imported profiles: In Intune, confirm the imported certificate profile status. On a test device, run 'certutil -store My' and verify the imported certificate is present.

## Rollback
1. Remove or unassign the trusted certificate profile: In Intune admin center, go to Devices > Configuration profiles, select the trusted certificate profile, click 'Properties', and change the assignment to 'Not assigned' or delete the profile. On affected devices, manually delete the root CA certificate from the Trusted Root Certification Authorities store using certlm.msc. 2. For SCEP profiles: Unassign or delete the SCEP profile in Intune. On devices, delete any certificates issued via SCEP from the Personal store using certlm.msc. 3. For PKCS profiles: Unassign or delete the PKCS profile in Intune. On devices, delete the PKCS-issued certificates from the Personal store. 4. For PKCS imported profiles: Unassign or delete the imported certificate profile in Intune. On devices, delete the imported certificate from the Personal store using certlm.msc.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
