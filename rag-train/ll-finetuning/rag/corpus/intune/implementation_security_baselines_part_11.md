# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How to change the version of a security baseline profile in Microsoft Intune without creating a new profile?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint security > Security baselines

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select a baseline profile in the Microsoft Intune admin center.
2. Use the built-in option to change the instance version for that profile to a new one.
3. You do not have to create a new baseline profile to take advantage of updated versions.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Security baselines. 2. Select the baseline profile you modified. 3. Confirm that the 'Version' field displays the new version number (e.g., 'September 2024' or 'Version 24H2'). 4. Review the profile's settings to ensure they match the new baseline version's default values. 5. Check the profile's assignment status to verify it is still applied to the intended groups. 6. Optionally, run the following PowerShell command to confirm the version: Get-IntuneSecurityBaselineProfile -ProfileId <ProfileId> | Select-Object -Property Id, DisplayName, Version.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Security baselines. 2. Select the baseline profile you changed. 3. Use the 'Change version' option to revert to the previous version (e.g., select the earlier version from the dropdown). 4. Confirm the version change and review the settings to ensure they revert to the previous baseline's defaults. 5. Monitor the profile's assignment status to ensure it is still applied correctly. 6. If the profile becomes corrupted or unresponsive, consider creating a new profile with the previous version and reassigning it to the same groups, then delete the problematic profile.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
