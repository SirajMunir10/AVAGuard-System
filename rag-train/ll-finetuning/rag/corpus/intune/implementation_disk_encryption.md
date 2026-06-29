# Implementation: Disk Encryption

**Domain:** Intune
**Subdomain:** Disk Encryption
**Incident Type:** Implementation

## Scenario / Query
How to manage built-in encryption methods for data protection using Intune disk encryption policies?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Disk encryption policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Disk encryption policy type to manage built-in encryption methods for data protection.
2. Platform support: Windows, macOS.
3. Available profiles: BitLocker, Personal Data Encryption (PDE), macOS FileVault.
4. Use case: Ensure data-at-rest protection with native encryption technologies.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Disk encryption and confirm the policy is assigned to the intended groups. 2. On a Windows device, run 'manage-bde -status' to verify BitLocker protection is On and encryption method matches the policy. 3. On a macOS device, run 'fdesetup status' to confirm FileVault is enabled. 4. For Personal Data Encryption (PDE), check the event log or use 'pde -status' to confirm PDE is active.

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint security > Disk encryption, select the policy, and choose 'Delete' to remove it. 2. Alternatively, modify the policy assignment to remove the affected groups. 3. On Windows devices, use 'manage-bde -off <drive_letter>:' to disable BitLocker if needed. 4. On macOS, run 'sudo fdesetup disable' to turn off FileVault. 5. For PDE, use 'pde -disable' to revert the encryption.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
