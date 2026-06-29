# Troubleshooting: iOS/iPadOS Enrollment (APNSCertificateNotValid)

**Domain:** Intune
**Subdomain:** iOS/iPadOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve iOS/iPadOS enrollment error: APNSCertificateNotValid - There's a problem with the certificate that lets the mobile device communicate with your company's network

## Environment Context
- **Tenant Type:** Intune standalone or Microsoft 365
- **Configuration:** Apple Push Notification Service (APNs) certificate

## Symptoms
- Enrollment fails with APNSCertificateNotValid error

## Error Codes
- `APNSCertificateNotValid`

## Root Causes
1. The steps to get an APNs certificate weren't completed
2. The APNs certificate has expired

## Remediation Steps
1. Renew the APNs certificate
2. Re-enroll the device
3. Important: Make sure that you renew the APNs certificate. Don't replace the APNs certificate. If you replace the certificate, you have to re-enroll all iOS/iPadOS devices in Intune.
4. For Intune standalone, see Renew Apple MDM push certificate
5. For Microsoft 365, see Create an APNs Certificate for iOS devices

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
