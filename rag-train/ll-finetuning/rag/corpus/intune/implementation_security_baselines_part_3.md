# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How do I migrate an existing security baseline profile to a newer baseline version in Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** New security baseline format introduced in May 2023

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the new process introduced in May 2023 to migrate an existing security baseline profile to the newer baseline version.
2. This is a one-time process that replaces the normal update behavior when moving from the most recent version of an older profile to a newer version that became available in May 2023 or later.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Security baselines. 2. Select the migrated profile and verify that the 'Baseline type' field shows the new baseline version (e.g., 'MDM Security Baseline for Windows 10 and later (May 2023)'). 3. Confirm that all settings from the original profile are present and correctly applied by reviewing the 'Settings' tab. 4. Check the 'Device status' tab to ensure that at least one test device reports 'Succeeded' after the migration. 5. Run the following PowerShell command to confirm the profile version: Get-IntuneSecurityBaseline -ProfileId <profile-id> | Select-Object -Property Version, BaselineType.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Security baselines. 2. Select the migrated profile and choose 'Delete' to remove the new baseline profile. 3. Recreate the original security baseline profile using the previous baseline version (e.g., the version available before May 2023) and reapply all custom settings from the original profile. 4. Assign the recreated profile to the same device groups as before. 5. Monitor device status to ensure the original baseline is reapplied successfully. 6. If the original profile was deleted during migration, restore it from backup or recreate it manually using the same settings.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
