# Incident Response: Device Compliance and Conditional Access

**Domain:** Intune
**Subdomain:** Device Compliance and Conditional Access
**Incident Type:** Incident Response

## Scenario / Query
A user reports that their corporate device is unexpectedly blocked from accessing Microsoft 365 resources. The Intune portal shows the device as 'Noncompliant' with a compliance policy that requires BitLocker encryption. How do I investigate and remediate this incident?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Intune and Conditional Access
- **Configuration:** Device compliance policy requiring BitLocker Drive Encryption on Windows 10/11 devices; Conditional Access policy blocking noncompliant devices

## Symptoms
- User cannot access Exchange Online, SharePoint, or Teams from their corporate device
- Device status in Intune shows 'Noncompliant' with reason 'BitLocker not enabled'
- User sees a 'Device not compliant' message when trying to access company resources

## Error Codes
N/A

## Root Causes
1. BitLocker was disabled or suspended on the device (e.g., after a BIOS update or maintenance)
2. Device is not properly enrolled in Intune or has lost its compliance status
3. TPM (Trusted Platform Module) is not initialized or is malfunctioning

## Remediation Steps
1. 1. Verify the device is enrolled in Intune and check the compliance policy details in the Microsoft Intune admin center under Devices > Compliance policies.
2. 2. On the affected device, open an elevated PowerShell prompt and run: 'Manage-bde -status' to check BitLocker status.
3. 3. If BitLocker is suspended, resume protection using: 'Manage-bde -protectors -enable C:'.
4. 4. If BitLocker is off, enable it via: 'Manage-bde -on C:' (ensure TPM is initialized first).
5. 5. Force a compliance check from the device by going to Settings > Accounts > Access work or school > click 'Sync'.
6. 6. In Intune, manually sync the device by selecting it and clicking 'Sync' to trigger a new compliance evaluation.
7. 7. If the issue persists, check the device's TPM status with: 'Get-Tpm' and initialize if needed using the TPM Management console (tpm.msc).

## Validation
After remediation, the device should show 'Compliant' in Intune, and the user should regain access to Microsoft 365 resources. Confirm by checking the device status in Intune and asking the user to access a previously blocked resource.

## Rollback
If the remediation causes issues, disable the BitLocker requirement in the compliance policy temporarily (not recommended for security) or exclude the device from the Conditional Access policy while troubleshooting.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows#bitlocker>
- <https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview>
