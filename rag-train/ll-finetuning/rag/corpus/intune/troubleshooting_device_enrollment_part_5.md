# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to run diagnostics for a user whose device fails to enroll in Intune?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft 365 admin center

## Symptoms
- Device fails to enroll in Intune

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Microsoft 365 admin center.
2. In the navigation pane, select Show all > Support > Help & support.
3. Alternatively, select Help & support on the bottom right side of the page.
4. Briefly describe your issue (for example, 'I need help enrolling Windows devices').
5. The system determines whether a diagnostic scenario matches your issue.
6. For the user having a device that fails to enroll in Intune, type their email address and then select Run tests.
7. After the diagnostic checks finish and a configuration issue is found, the system provides steps to resolve the issue.
8. If a diagnostic detects an issue and you implement a fix based on the results, consider rerunning the diagnostic to ensure the issue is completely resolved.

## Validation
1. In the Microsoft 365 admin center, navigate to Support > Help & support. 2. Describe the issue (e.g., 'I need help enrolling Windows devices'). 3. For the affected user, type their email address and select Run tests. 4. Confirm the diagnostic completes without errors and no configuration issues are reported. 5. Optionally, attempt to enroll the device again and verify successful enrollment in Intune.

## Rollback
1. If the diagnostic or remediation steps cause issues, revert any configuration changes made based on the diagnostic results. 2. Re-run the diagnostic in the Microsoft 365 admin center (Support > Help & support) for the same user to identify any new issues. 3. If enrollment still fails, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
