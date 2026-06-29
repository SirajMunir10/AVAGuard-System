# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How to configure minimum and maximum OS version compliance rules for Windows devices in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows compliance policy settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enter the minimum allowed version in the major.minor.build.revision number format. To get the correct value, open a command prompt, and type ver. The ver command returns the version in the following format: Microsoft Windows [Version 10.0.17134.1]
2. Enter the maximum allowed version in the major.minor.build.revision number format. To get the correct value, open a command prompt, and type ver. The ver command returns the version in the following format: Microsoft Windows [Version 10.0.17134.1]

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Devices > Compliance policies > Policies.
3. Select the Windows compliance policy that was configured.
4. Under Compliance settings > System Security, verify that 'Minimum OS version' and 'Maximum OS version' are set to the intended values (e.g., 10.0.17134.1).
5. On a Windows device enrolled in Intune, open Settings > Accounts > Access work or school > click the connected account > Info. Confirm the compliance status shows 'Compliant'.
6. Alternatively, on the device, open a command prompt and run 'ver' to confirm the OS version falls within the configured range.

## Rollback
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Devices > Compliance policies > Policies.
3. Select the Windows compliance policy that was modified.
4. Under Compliance settings > System Security, clear the values for 'Minimum OS version' and/or 'Maximum OS version' to remove the restrictions, or set them to the previous values.
5. Select Review + save, then select Save.
6. On a test device, force a compliance check by going to Settings > Accounts > Access work or school > click the connected account > Sync. Confirm the device returns to the expected compliance state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
