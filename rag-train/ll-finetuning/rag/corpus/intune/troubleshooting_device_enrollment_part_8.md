# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How can managed device users collect enrollment and diagnostic logs for IT admin review?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Device enrollment

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Your managed device users can collect enrollment and diagnostic logs for you to review.
2. User instructions for collecting logs are provided in: Send Android enrollment errors to your IT admin
3. User instructions for collecting logs are provided in: Send iOS/iPadOS errors to your IT admin

## Validation
1. On an Android device, navigate to Settings > Accounts > Company Portal > Device enrollment logs and tap 'Send logs' to email the logs to IT. 2. On an iOS/iPadOS device, open the Company Portal app, tap the menu icon, tap 'Send Diagnostic Report', and email the report to IT. 3. Confirm that the IT admin receives the email with the enrollment logs attached.

## Rollback
1. If logs are not received, instruct the user to retry the log collection steps. 2. If the issue persists, verify that the Company Portal app is installed and updated to the latest version. 3. If necessary, reinstall the Company Portal app and repeat the log collection process.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
