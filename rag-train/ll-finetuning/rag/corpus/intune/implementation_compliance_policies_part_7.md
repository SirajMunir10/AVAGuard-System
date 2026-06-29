# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How to configure encryption compliance policy for Windows devices in Intune?

## Environment Context
- **Tenant Type:** Intune managed
- **Configuration:** Windows compliance policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set Encryption of data storage on a device to Require to encrypt data storage on your devices.
2. For a more robust encryption setting, consider using Require BitLocker, which leverages Windows Device Health Attestation to validate BitLocker status at the TPM level.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy you configured. Under 'Properties', verify that 'Encryption of data storage on a device' is set to 'Require'. If you enabled BitLocker, confirm that 'Require BitLocker' is also set to 'Require'. 2. On a Windows device enrolled in Intune, open the Settings app, go to System > About, and confirm that 'Device encryption' or 'BitLocker' is turned on. 3. In the Intune admin center, go to Devices > All devices, select the target device, and under 'Device compliance', verify the compliance status shows 'Compliant' for the encryption policy.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy you modified. Under 'Properties', change 'Encryption of data storage on a device' from 'Require' to 'Not configured'. If you enabled 'Require BitLocker', set it back to 'Not configured'. 2. Save the policy changes. 3. On the affected Windows device, open the Settings app, go to System > About, and if needed, turn off 'Device encryption' or 'BitLocker' by selecting 'Turn off' (this may require administrative privileges). 4. In the Intune admin center, go to Devices > All devices, select the device, and under 'Device compliance', confirm the compliance status updates to reflect the removed encryption requirement.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
