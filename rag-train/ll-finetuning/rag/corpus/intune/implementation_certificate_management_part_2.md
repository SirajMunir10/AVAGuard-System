# Implementation: Certificate Management

**Domain:** Intune
**Subdomain:** Certificate Management
**Incident Type:** Implementation

## Scenario / Query
How to deploy a shared certificate using imported PKCS in Intune for email decryption?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Imported PKCS certificate profile, email server certificate

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Export the certificate from a source (e.g., email server).
2. Use Imported PKCS in Intune to deploy the same certificate to multiple recipients.
3. Ensure all users or devices can decrypt emails encrypted by that certificate.

## Validation
1. On a test device, verify the certificate is installed: run 'certlm.msc' (Local Machine) or 'certmgr.msc' (Current User) and confirm the certificate appears under 'Personal' with the expected subject and issuer. 2. Send an encrypted test email to a user who received the certificate and confirm the user can decrypt it using Outlook or another email client. 3. In the Microsoft Intune admin center, navigate to 'Devices' > 'Configuration profiles', select the imported PKCS certificate profile, and check the 'Device status' or 'User status' to ensure the profile is successfully assigned and applied.

## Rollback
1. In the Microsoft Intune admin center, go to 'Devices' > 'Configuration profiles', select the imported PKCS certificate profile, and change the assignment to 'Unassign' or remove the targeted groups. 2. On affected devices, manually delete the certificate from the 'Personal' store using 'certlm.msc' or 'certmgr.msc'. 3. If the certificate was used for email decryption, reconfigure the email client to use a different certificate or revert to previous encryption settings.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/certificates-configure>
