# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to deploy certificates using trusted certificate profiles, SCEP certificate profiles, PKCS certificate profiles, and PKCS imported certificate profiles?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Intune
- **Configuration:** Certificate deployment mechanisms

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Deploy Trusted Root CA certificate from your root or intermediate (issuing) CA to devices using trusted certificate profiles.
2. Deploy certificates using SCEP certificate profiles.
3. Deploy certificates using PKCS certificate profiles (only supported with the Digicert PKI Platform).
4. Deploy certificates using PKCS imported certificate profiles.

## Validation
1. Verify that the trusted root CA certificate profile is assigned and applied: In Intune, navigate to Devices > Configuration profiles, select the trusted certificate profile, and check the 'Device status' and 'User status' for 'Succeeded' status. 2. Confirm SCEP certificate profile deployment: In Intune, go to Devices > Configuration profiles, select the SCEP profile, and verify that devices report 'Succeeded' status. 3. Validate PKCS certificate profile (Digicert PKI Platform): In Intune, under Devices > Configuration profiles, select the PKCS profile and confirm 'Succeeded' status on target devices. 4. Check PKCS imported certificate profile: In Intune, navigate to Devices > Configuration profiles, select the imported PKCS profile, and ensure devices show 'Succeeded' status. 5. On a test device, run 'certlm.msc' and confirm the trusted root CA certificate appears under 'Trusted Root Certification Authorities' and the issued certificate appears under 'Personal'.

## Rollback
1. Remove or unassign the trusted certificate profile: In Intune, go to Devices > Configuration profiles, select the trusted certificate profile, click 'Properties', and under 'Assignments' set 'Included groups' to 'None' or remove the assignment. 2. Remove or unassign the SCEP certificate profile: In Intune, navigate to Devices > Configuration profiles, select the SCEP profile, click 'Properties', and under 'Assignments' remove all group assignments. 3. Remove or unassign the PKCS certificate profile: In Intune, go to Devices > Configuration profiles, select the PKCS profile, click 'Properties', and under 'Assignments' remove all group assignments. 4. Remove or unassign the PKCS imported certificate profile: In Intune, navigate to Devices > Configuration profiles, select the imported PKCS profile, click 'Properties', and under 'Assignments' remove all group assignments. 5. On affected devices, manually delete the certificates: Run 'certlm.msc', expand 'Personal' > 'Certificates', right-click the issued certificate, select 'Delete'. Expand 'Trusted Root Certification Authorities' > 'Certificates', right-click the trusted root CA certificate, select 'Delete'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
