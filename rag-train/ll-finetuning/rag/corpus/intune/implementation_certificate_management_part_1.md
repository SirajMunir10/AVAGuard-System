# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to configure certificate profiles in Intune for SCEP, PKCS, and imported PKCS certificates?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Certificate profiles, trusted root certificate, Certification Authority

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Provision a trusted root certificate from a trusted Certification Authority (CA) using the trusted certificate profile.
2. Deploy the trusted certificate profile to the same devices and users that receive the certificate profiles for SCEP, PKCS, and imported PKCS.
3. For SCEP: Provision certificates that are unique to each request for the certificate.
4. For PKCS: Provision each device with a unique certificate.
5. For Imported PKCS: Deploy the same certificate exported from a source (e.g., email server) to multiple recipients.

## Validation
1. Confirm that the trusted root certificate profile is assigned to the correct groups and devices: In the Intune portal, go to Devices > Configuration profiles, select the trusted certificate profile, and verify the assignments under the 'Assignments' tab. 2. Verify that the trusted root certificate is installed on target devices: On a Windows device, run 'certlm.msc' and check that the root certificate appears under 'Trusted Root Certification Authorities > Certificates'. 3. For SCEP certificate profiles: In Intune, go to Devices > Configuration profiles, select the SCEP profile, and confirm that the 'Subject name format' and 'Key usage' settings match the CA template. 4. For PKCS certificate profiles: In Intune, go to Devices > Configuration profiles, select the PKCS profile, and verify that the 'Certificate authority' and 'Certificate template name' are correctly configured. 5. For imported PKCS certificates: In Intune, go to Devices > Configuration profiles, select the imported PKCS profile, and confirm that the certificate file (.pfx) is uploaded and assigned to the intended users or devices. 6. On a test device, check that the certificate is present: Run 'certlm.msc' and navigate to 'Personal > Certificates' to see the issued certificate. 7. Validate that the certificate is trusted: On the device, run 'certutil -verifystore My' and ensure no chain errors are reported.

## Rollback
1. Remove the trusted root certificate profile assignment: In Intune, go to Devices > Configuration profiles, select the trusted certificate profile, click on 'Assignments', and remove the assigned groups. 2. Delete the SCEP certificate profile: In Intune, go to Devices > Configuration profiles, select the SCEP profile, and click 'Delete'. 3. Delete the PKCS certificate profile: In Intune, go to Devices > Configuration profiles, select the PKCS profile, and click 'Delete'. 4. Delete the imported PKCS certificate profile: In Intune, go to Devices > Configuration profiles, select the imported PKCS profile, and click 'Delete'. 5. On devices, remove the certificates: Run 'certlm.msc', locate the certificates under 'Personal > Certificates' and 'Trusted Root Certification Authorities > Certificates', right-click each, and select 'Delete'. 6. If the CA issued certificates for SCEP or PKCS, revoke them using the CA management console (e.g., Certification Authority snap-in, right-click the certificate, select All Tasks > Revoke).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
