# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
What are the available security baseline versions for HoloLens 2 in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** HoloLens 2 security baseline

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. HoloLens 2 - Advanced security baseline settings: Version 1 - HoloLens 2 advanced security - January 2025
2. HoloLens 2 - Standard security baseline settings: Version 1 - HoloLens 2 standard security - January 2025

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Verify that 'HoloLens 2 - Advanced security baseline settings: Version 1 - HoloLens 2 advanced security - January 2025' and 'HoloLens 2 - Standard security baseline settings: Version 1 - HoloLens 2 standard security - January 2025' are listed.
4. For each baseline, select it and confirm the version is 'Version 1' and the description matches the January 2025 release.
5. Optionally, use the Graph API: GET https://graph.microsoft.com/beta/deviceManagement/intuneSecurityBaselines?$filter=displayName eq 'HoloLens 2 - Advanced security baseline settings' or displayName eq 'HoloLens 2 - Standard security baseline settings' and verify the response includes the correct versions.

## Rollback
1. If a baseline assignment was created and needs to be removed, navigate to Endpoint security > Security baselines, select the assigned baseline profile, and choose 'Delete' to remove the assignment.
2. If the baseline version itself is incorrect or causing issues, ensure no profiles are assigned to that version, then contact Microsoft Support to report the version issue, as baseline versions cannot be deleted or modified by administrators.
3. To revert to a previous baseline version (if available), create a new profile using the older version and assign it to the same groups, then unassign or delete the profile using the problematic version.
4. For rollback via Graph API: Use DELETE https://graph.microsoft.com/beta/deviceManagement/intuneSecurityBaselines/{baselineId} to remove a baseline profile (only if no assignments exist).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
