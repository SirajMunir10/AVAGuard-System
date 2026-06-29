# Troubleshooting: iOS/iPadOS Enrollment (NoEnrollmentPolicy)

**Domain:** Intune
**Subdomain:** iOS/iPadOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve iOS/iPadOS enrollment error: NoEnrollmentPolicy - No enrollment policy found

## Environment Context
- **Tenant Type:** Intune standalone or Microsoft 365
- **Configuration:** Apple Push Notification Service (APNs) certificate

## Symptoms
- No enrollment policy found error during iOS/iPadOS enrollment

## Error Codes
- `NoEnrollmentPolicy`

## Root Causes
1. The Apple Push Notification Service (APNs) certificate is missing, invalid, or expired

## Remediation Steps
1. Check that enrollment has been set up correctly and that iOS/iPadOS as a platform is enabled
2. For instructions, see Set up iOS/iPadOS and Mac device management
3. Get an Apple MDM push certificate
4. Renew Apple MDM push certificate

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
