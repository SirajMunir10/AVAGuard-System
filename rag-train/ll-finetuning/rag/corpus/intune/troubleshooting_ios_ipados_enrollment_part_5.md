# Troubleshooting: iOS/iPadOS Enrollment (DeviceTypeNotSupported)

**Domain:** Intune
**Subdomain:** iOS/iPadOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve iOS/iPadOS enrollment error: DeviceTypeNotSupported - The mobile device type that you're trying to enroll isn't supported

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- DeviceTypeNotSupported error during iOS/iPadOS enrollment

## Error Codes
- `DeviceTypeNotSupported`

## Root Causes
1. The user might have tried to enroll using a non-iOS device
2. Device is not running iOS/iPadOS version 8.0 or later

## Remediation Steps
1. Confirm that device is running iOS/iPadOS version 8.0 or later
2. Make sure that your user's device is running iOS/iPadOS version 8.0 or later

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
