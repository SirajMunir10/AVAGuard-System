# Implementation: Compliance Policy

**Domain:** Intune
**Subdomain:** Compliance Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure a compliance policy for Windows Holographic for Business to require encryption of data storage on device?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Windows Holographic for Business uses the Windows 10 and later platform

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to System Security > Encryption > Encryption of data storage on device
2. To verify device encryption on the Microsoft HoloLens, see Verify device encryption

## Validation
1. In the Microsoft Intune admin center, go to Endpoint security > Device compliance > Policies and select the policy you configured for Windows Holographic for Business. 2. Under 'Compliance policy settings', expand 'System Security' and then 'Encryption'. Confirm that 'Encryption of data storage on device' is set to 'Require'. 3. On a Microsoft HoloLens device enrolled in Intune, go to Settings > System > About, and verify that 'Device encryption' shows as 'On'. Alternatively, run the command 'manage-bde -status' in an elevated command prompt on the device and confirm that the status for the OS drive is 'Protection On'.

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint security > Device compliance > Policies and select the policy you configured for Windows Holographic for Business. 2. Under 'Compliance policy settings', expand 'System Security' and then 'Encryption'. Change 'Encryption of data storage on device' from 'Require' to 'Not configured'. 3. Select 'Review + save' and then 'Save' to apply the change. 4. On the Microsoft HoloLens device, if encryption was enabled by the policy and you need to disable it, go to Settings > System > About and select 'Turn off device encryption' (note: this may require administrative privileges and could trigger a device reset).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
