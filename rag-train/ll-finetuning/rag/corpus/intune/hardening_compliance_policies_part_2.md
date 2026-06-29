# Hardening: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Hardening

## Scenario / Query
How to enforce BitLocker encryption on Windows devices using Intune compliance policy?

## Environment Context
- **Tenant Type:** Intune managed
- **Configuration:** Windows compliance policy with Require BitLocker

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Require BitLocker setting which leverages Windows Device Health Attestation to validate BitLocker status at the TPM level.
2. Note that a reboot may be required before the device will reflect as compliant.

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > Compliance policies > Policies and select the policy that includes the 'Require BitLocker' setting. 2. Under 'Settings', confirm that 'Require BitLocker' is set to 'Require'. 3. On a targeted Windows device, run 'msinfo32.exe' and verify that 'Device Encryption Support' shows 'Meets prerequisites'. 4. Run 'manage-bde -status' to confirm that BitLocker protection is 'On' for the OS drive. 5. In the Intune admin center, go to Devices > Compliance > Device compliance and select the device; verify that the compliance status for 'Require BitLocker' shows 'Compliant'.

## Rollback
1. In the Microsoft Intune admin center, navigate to Devices > Compliance policies > Policies and select the policy that includes the 'Require BitLocker' setting. 2. Under 'Settings', change 'Require BitLocker' to 'Not configured' or 'Audit only'. 3. Save the policy and wait for the next check-in or manually sync the device from the device's Access Work or School settings. 4. On the affected device, run 'manage-bde -off C:' to decrypt the drive if BitLocker was enabled solely due to the policy and needs to be removed. 5. Verify the device compliance status updates to reflect the change.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
