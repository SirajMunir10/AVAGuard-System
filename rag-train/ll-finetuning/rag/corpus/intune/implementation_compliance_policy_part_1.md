# Implementation: Compliance Policy

**Domain:** Intune
**Subdomain:** Compliance Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure Trusted Platform Module (TPM) compliance check in Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** DeviceStatus CSP - DeviceStatus/TPM/SpecificationVersion

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set TPM to 'Not configured' (default) to skip TPM chip version check
2. Set TPM to 'Require' to check TPM chip version for compliance; device is compliant if TPM chip version is greater than 0, noncompliant if no TPM version exists

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy that was modified. Under 'Properties', verify that the 'Trusted Platform Module (TPM)' setting is set to either 'Not configured' or 'Require' as intended. 2. On a Windows 10/11 device enrolled in Intune, open Settings > Accounts > Access work or school > click the connected account > Info. Under 'Device sync', click 'Sync' to force a compliance check. 3. On the same device, open a command prompt as administrator and run: 'certutil -store -silent Tpm' to confirm the TPM specification version. If TPM is set to 'Require', the device should show compliance in the Intune admin center under Devices > All devices > select the device > Device compliance. 4. Alternatively, use the DeviceStatus CSP by running: 'Get-CimInstance -Namespace root/cimv2/mdm/dmmap -ClassName MDM_DeviceStatus_TPM01' to verify the SpecificationVersion value.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Select the Windows compliance policy that was modified. Under 'Properties', change the 'Trusted Platform Module (TPM)' setting back to 'Not configured' (default). 2. On a Windows 10/11 device enrolled in Intune, open Settings > Accounts > Access work or school > click the connected account > Info. Under 'Device sync', click 'Sync' to force a compliance re-evaluation. 3. Confirm that the device no longer shows noncompliance due to TPM by checking the device's compliance status in the Intune admin center under Devices > All devices > select the device > Device compliance.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
