# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How to update an existing security baseline profile to the latest version in Microsoft Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Security baseline profiles

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When a new version for a profile becomes available, settings in profiles based on the older versions become read-only.
2. You can continue to use those older profiles.
3. You can also edit the profile names, description, and assignments, but they don't support a change to their settings configuration and you can't create new profiles based on the older versions.
4. When you're ready to use the more recent baseline version, you can create new profiles or update your existing profiles to the new version.
5. See Update a baseline profile to the latest version in the Manage security baseline profiles article.

## Validation
1. Navigate to Microsoft Intune admin center > Endpoint security > Security baselines. 2. Select the profile you updated. 3. Verify the 'Baseline version' field shows the latest version (e.g., 'May 2023' or '22H2'). 4. Review the 'Settings' tab to confirm all settings are editable and reflect the new baseline version. 5. Check 'Assignments' to ensure the profile is still assigned to the correct groups. 6. On a test device assigned to the profile, open the Microsoft Intune Company Portal and sync. 7. On the device, run 'dsregcmd /status' and confirm the MDM URL points to your tenant. 8. Verify the device reports compliance with the new baseline by checking the device's 'Compliance' status in Intune.

## Rollback
1. In Microsoft Intune admin center > Endpoint security > Security baselines, select the updated profile. 2. Click 'Properties' and note the current baseline version. 3. If the update caused issues, create a new profile using the previous baseline version (e.g., 'April 2023' or '21H2') with the same settings. 4. Assign the new profile to the same groups as the updated profile. 5. Remove the assignment of the updated profile from those groups. 6. On affected devices, sync via Company Portal or run 'SyncML' command to force policy refresh. 7. Verify devices revert to the previous baseline by checking compliance status. 8. If needed, delete the updated profile after confirming rollback is successful.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
