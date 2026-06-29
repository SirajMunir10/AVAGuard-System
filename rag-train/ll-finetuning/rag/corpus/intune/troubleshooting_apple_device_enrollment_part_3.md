# Troubleshooting: Apple Device Enrollment

**Domain:** Intune
**Subdomain:** Apple Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'Terms and conditions not accepted' error in Apple Business Manager or Apple School Manager?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Apple Business Manager (ABM) or Apple School Manager (ASM) terms and conditions

## Symptoms
- Terms and conditions not accepted error

## Error Codes
N/A

## Root Causes
1. New terms and conditions (T&C) need to be accepted in Apple Business Manager or Apple School Manager.

## Remediation Steps
1. Accept the new T&C in Apple Business Manager or Apple School Manager Portal.
2. Note: This must be done by a user with the Administrator role in Apple Business Manager or Apple School Manager.

## Validation
1. Sign in to the Apple Business Manager (ABM) or Apple School Manager (ASM) portal with an Administrator account. 2. Navigate to the 'Settings' or 'Account' section and verify that no pending terms and conditions acceptance prompt is displayed. 3. In the Microsoft Intune admin center, go to 'Tenant administration' > 'Connectors and tokens' > 'Apple Business Manager' (or 'Apple School Manager') and confirm the connection status shows as 'Active' with no errors. 4. Attempt to enroll a test iOS/iPadOS device via Automated Device Enrollment (ADE) and confirm no 'Terms and conditions not accepted' error appears.

## Rollback
1. If the new terms and conditions were accepted in error or cause unexpected issues, contact Apple Support to request a rollback of the terms acceptance (note: this may not be possible and could require waiting for the next terms update). 2. In the Microsoft Intune admin center, temporarily disable the Apple Business Manager or Apple School Manager token by navigating to 'Tenant administration' > 'Connectors and tokens' > 'Apple Business Manager' (or 'Apple School Manager') and selecting 'Disable' to stop enrollment until the issue is resolved. 3. Revert any changes made to enrollment profiles or device groups that were modified during the troubleshooting process.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
