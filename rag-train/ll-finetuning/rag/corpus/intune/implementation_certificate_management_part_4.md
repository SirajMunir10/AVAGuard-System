# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites for using certificates with Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Certificate profiles (SCEP, PKCS, Imported PKCS)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure a Certification Authority (CA) is available, either Microsoft CA or third-party CA.
2. Deploy the trusted root certificate from your CA using a trusted certificate profile before deploying SCEP or PKCS certificate profiles.
3. Deploy certificate profiles to provision users and devices with certificates for authentication.

## Validation
1. Confirm that a Certification Authority (CA) is reachable and operational by running 'certutil -ping' on a domain-joined device. 2. Verify the trusted root certificate profile is deployed and installed on target devices by checking 'certlm.msc' under 'Trusted Root Certification Authorities' for the CA's root certificate. 3. Validate that SCEP or PKCS certificate profiles are assigned to the correct groups and that devices report a successful certificate enrollment status in the Intune admin center under 'Devices' > 'Monitor' > 'Certificate enrollment'.

## Rollback
1. Remove any newly created certificate profiles (SCEP, PKCS, or trusted root) from Intune by navigating to 'Devices' > 'Configuration profiles' and deleting the profiles. 2. If a new CA was introduced, revert to the previous CA configuration and ensure the old CA is still trusted. 3. For devices that received certificates, revoke those certificates from the CA using the CA management console or 'certutil -revoke <serial_number>'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
