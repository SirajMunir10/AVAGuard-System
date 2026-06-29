# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to deploy PKCS and SCEP certificates to devices using Intune certificate profiles?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Certificate profiles for PKCS and SCEP

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create and assign certificate profiles to devices.
2. For PKCS certificates, create a PKCS certificate profile for Android and a separate PKCS certificate profile for iOS/iPadOS.
3. For SCEP certificates, create a SCEP certificate profile for Android and another for iOS/iPadOS.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Devices > Configuration profiles > Profiles.
3. Verify that the PKCS certificate profiles for Android and iOS/iPadOS are listed with a status of 'Succeeded' or 'Assigned'.
4. Verify that the SCEP certificate profiles for Android and iOS/iPadOS are listed with a status of 'Succeeded' or 'Assigned'.
5. On a test device enrolled in Intune, open the Company Portal app and confirm the certificate is installed under Device details > Certificates.
6. On the test device, run 'certlm.msc' (Windows) or check Settings > General > Profiles & Device Management (iOS/iPadOS) or Settings > Security > Trusted credentials (Android) to confirm the certificate is present and trusted.

## Rollback
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Devices > Configuration profiles > Profiles.
3. Select each PKCS certificate profile (Android and iOS/iPadOS) and choose 'Delete' to remove the profile assignment.
4. Select each SCEP certificate profile (Android and iOS/iPadOS) and choose 'Delete' to remove the profile assignment.
5. On affected devices, manually remove the certificates installed by the profiles via device settings (e.g., Settings > General > Profiles & Device Management on iOS/iPadOS, or Settings > Security > User credentials on Android).
6. If needed, reassign any previously used certificate profiles by re-creating them from backup or documentation.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
