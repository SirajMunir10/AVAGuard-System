# Implementation: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Implementation

## Scenario / Query
How to configure a Windows compliance policy in Intune to require BitLocker encryption?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** Compliance policy creation

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set the 'Require BitLocker' setting to 'Require' in the Windows compliance policy.
2. Note: The Device HealthAttestation CSP - BitLockerStatus is used for evaluation.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy that was configured. Under 'Properties', confirm that 'Require BitLocker' is set to 'Require'. 2. On a targeted Windows device, run 'msinfo32.exe' and verify that 'Device Encryption Support' shows 'BitLocker Enabled'. Alternatively, run 'manage-bde -status' from an elevated command prompt and confirm that the protection status is 'On'. 3. In the Intune admin center, go to Devices > Monitor > Device compliance. Select the device and verify that the compliance status shows 'Compliant' for the BitLocker requirement.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy. Under 'Properties', click 'Edit' for 'Compliance settings'. Change the 'Require BitLocker' setting from 'Require' to 'Not configured'. Click 'Review + save' and then 'Save'. 2. On a targeted Windows device, run 'gpupdate /force' from an elevated command prompt to force a policy refresh. 3. In the Intune admin center, go to Devices > Monitor > Device compliance. Select the device and confirm that the BitLocker requirement is no longer evaluated (the device may show 'Not evaluated' or 'Compliant' based on other settings).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
