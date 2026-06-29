# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How to configure Windows OS version compliance rules in Intune to enforce minimum and maximum OS versions?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** Compliance policy for Windows OS version settings

## Symptoms
- Device with OS version earlier than specified minimum is reported as noncompliant
- Device with OS version later than specified maximum is blocked from accessing organization resources

## Error Codes
N/A

## Root Causes
1. OS version does not meet the minimum or maximum requirements defined in the compliance policy

## Remediation Steps
1. Enter the minimum allowed OS version in major.minor.build number format
2. Enter the maximum allowed OS version in major.minor.build number format for mobile devices
3. End user can upgrade their device if below minimum version to regain access
4. End user must contact IT administrator if device exceeds maximum version until rule is changed

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy that was modified. Under Compliance settings > Device Health, verify that 'Minimum OS version' and 'Maximum OS version' are set to the intended values (e.g., 10.0.19041.0 for minimum, 10.0.22621.0 for maximum). 2. On a test Windows device that is enrolled in Intune and has an OS version below the minimum, confirm that the device is reported as noncompliant in the Intune admin center under Devices > All devices > select the device > Device compliance. 3. On a test device with an OS version above the maximum, confirm that the device is blocked from accessing organization resources (e.g., cannot access Microsoft 365 apps or company portal). 4. On a test device with an OS version within the allowed range, confirm that the device is reported as compliant and can access resources.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy that was modified. Under Compliance settings > Device Health, set 'Minimum OS version' and 'Maximum OS version' to 'Not configured' or to the previous values that were in effect before the change. 2. If the policy was newly created, delete the policy by selecting it and clicking Delete. 3. Instruct end users whose devices were blocked due to the maximum OS version rule to retry accessing resources after the policy change (may require syncing the device from Company Portal or Settings > Accounts > Access work or school > Sync). 4. Monitor the Intune admin center under Devices > All devices for any devices that remain noncompliant and manually remediate if necessary.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
