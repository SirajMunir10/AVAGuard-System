# Implementation: Certificate Profiles

**Domain:** Intune
**Subdomain:** Certificate Profiles
**Incident Type:** Implementation

## Scenario / Query
How to choose the correct certificate profile type (Trusted, SCEP, PKCS, PKCS imported) for different deployment scenarios in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Certificate profile configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Trusted certificate profile to deploy the public key (certificate) from a root CA or intermediary CA to users and devices to establish a trust back to the source CA.
2. Use SCEP certificate profile to deploy a template for a certificate request to users and devices, where each certificate provisioned is unique and tied to the user or device that requests it. SCEP can deploy certificates to devices that lack user affinity, including KIOSK or user-less devices.
3. Use PKCS certificate profile to deploy a template for a certificate request that specifies a certificate type of either user or device. Requests for a certificate type of user always require user affinity. When deployed to a user, each of the user's devices receives a unique certificate. When deployed to a device with a user, that user is associated with the certificate for that device. When deployed to a userless device, no certificate is provisioned. Templates with a certificate type of device don't require user affinity to provision a certificate. Deployment to a device provisions the device. Deployment to a user provisions the device the user is signed into with a certificate.
4. Use PKCS imported certificate profile to deploy a single certificate to multiple devices and users, which supports scenarios like S/MIME signing and encryption. For example, by deploying the same certificate to each device, each device can decrypt email received from that same email server.

## Validation
1. Verify that the Trusted certificate profile is assigned to the correct groups and that devices report 'Succeeded' status in the Intune console under Devices > Configuration profiles > profile name > Device status.
2. For SCEP profiles, confirm that a valid SCEP server URL is configured and that devices show 'Succeeded' status; test certificate issuance by enrolling a test device and checking the local certificate store for a unique certificate matching the template.
3. For PKCS profiles, ensure the certificate type (user or device) matches the deployment target; verify that user-affinity devices receive unique certificates and that userless devices show 'Not applicable' or 'Error' for user-type templates.
4. For PKCS imported profiles, confirm that the same certificate is deployed to multiple devices by checking the certificate thumbprint on each device matches the imported certificate.

## Rollback
1. Remove the assignment of the problematic certificate profile from the affected groups in Intune (Devices > Configuration profiles > select profile > Assignments > Remove groups).
2. If certificates were already issued, revoke them from the issuing CA or use Intune's 'Retire' or 'Wipe' action on devices to remove the profile and its certificates.
3. For SCEP profiles, delete the SCEP server configuration in Intune (Tenant administration > Connectors and tokens > SCEP certificate) if the server is no longer needed.
4. For PKCS imported profiles, delete the imported certificate from Intune (Devices > Configuration profiles > PKCS imported certificate > Delete) and re-issue a new certificate if necessary.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
