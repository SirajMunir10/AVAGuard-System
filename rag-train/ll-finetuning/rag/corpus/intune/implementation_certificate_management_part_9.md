# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to configure SCEP certificate profiles with a third-party Certification Authority without using the Microsoft Intune Certificate Connector?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Intune
- **Configuration:** Third-party CA integration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure integration with a third-party CA from one of our supported partners. Setup includes following the instructions from the third-party CA to complete integration of their CA with Intune.
2. Create an application in Microsoft Entra ID that delegates rights to Intune to do SCEP certificate challenge validation.

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > Configuration profiles > Create profile > Platform: Windows 10 and later > Profile type: SCEP certificate. Verify that the profile can be created and that the SCEP server URL points to the third-party CA endpoint. 2. In Microsoft Entra ID, go to App registrations and confirm the application created for Intune SCEP challenge validation exists with the correct delegated permissions (e.g., 'SCEPChallengeValidation'). 3. Assign the SCEP certificate profile to a test user or device group and check that the device successfully receives a certificate from the third-party CA by reviewing the device's certificate store or using the Certificates snap-in (certlm.msc). 4. On a test device, run 'certutil -store My' to confirm the issued certificate is present and valid.

## Rollback
1. In Intune, delete the SCEP certificate profile by navigating to Devices > Configuration profiles, selecting the profile, and clicking Delete. 2. In Microsoft Entra ID, remove the application created for SCEP challenge validation by going to App registrations, selecting the app, and clicking Delete. 3. If any test certificates were issued, revoke them from the third-party CA management console. 4. On any test devices, remove the issued certificate using 'certutil -delstore My <serialnumber>' or via the Certificates MMC snap-in.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
