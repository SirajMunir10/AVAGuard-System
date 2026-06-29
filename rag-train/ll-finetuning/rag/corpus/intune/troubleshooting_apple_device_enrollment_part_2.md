# Troubleshooting: Apple Device Enrollment

**Domain:** Intune
**Subdomain:** Apple Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'Access denied' error when Intune cannot communicate with Apple Business Manager or Apple School Manager?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Apple Business Manager (ABM) or Apple School Manager (ASM) MDM server list

## Symptoms
- Access denied error
- Intune can't talk to Apple anymore

## Error Codes
N/A

## Root Causes
1. Intune has been removed from the MDM server list in Apple Business Manager or Apple School Manager.
2. Token has possibly expired.

## Remediation Steps
1. Verify whether your token has expired, and if a new token was created.
2. Check to see if Intune is in the MDM server list.

## Validation
1. Sign in to Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Tenant administration > Connectors and tokens > Apple MDM push certificate.
3. Check the 'Expiration date' field: if the date is in the past, the token has expired.
4. Navigate to Apple Business Manager (https://business.apple.com) or Apple School Manager (https://school.apple.com) with an account that has the Administrator role.
5. Go to Settings > MDM Servers and verify that the Microsoft Intune server is listed and its status is 'Active'.
6. If the server is missing or inactive, Intune has been removed from the MDM server list.
7. In Intune admin center, go to Tenant administration > Connectors and tokens > Apple MDM push certificate and click 'Review' to confirm the certificate is valid and not expired.

## Rollback
1. If a new token was created but Intune still shows 'Access denied', ensure the new token was uploaded to Intune: In Intune admin center, go to Tenant administration > Connectors and tokens > Apple MDM push certificate, click 'Upload' and select the new .p7m file.
2. If Intune was removed from the MDM server list in Apple Business Manager/Apple School Manager, re-add it: In Apple Business Manager/Apple School Manager, go to Settings > MDM Servers, click 'Add MDM Server', enter a name (e.g., 'Microsoft Intune'), download the server token, and upload it to Intune.
3. If the issue persists, verify that the Apple MDM push certificate has not been revoked: In Apple Business Manager/Apple School Manager, check the MDM server details for any warnings.
4. If the token was renewed but the error continues, wait up to 24 hours for propagation, then retry validation steps.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
