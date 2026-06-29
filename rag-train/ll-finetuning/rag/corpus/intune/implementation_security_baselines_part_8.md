# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
What are the available security baseline versions for Microsoft Edge in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Microsoft Edge security baseline

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Microsoft Edge version 139 - April 2026
2. Microsoft Edge version 128 - January 2025
3. Microsoft Edge version 117 - November 2023
4. Microsoft Edge version 112 and later - May 2023
5. Microsoft Edge version 85 and later - September 2020
6. Microsoft Edge version 80 and later - April 2020
7. Preview: Microsoft Edge version 77 and later - October 2019

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Select 'Microsoft Edge' from the list of available baselines.
4. Verify that the following baseline versions are listed:
   - Microsoft Edge version 139 - April 2026
   - Microsoft Edge version 128 - January 2025
   - Microsoft Edge version 117 - November 2023
   - Microsoft Edge version 112 and later - May 2023
   - Microsoft Edge version 85 and later - September 2020
   - Microsoft Edge version 80 and later - April 2020
   - Preview: Microsoft Edge version 77 and later - October 2019
5. Confirm that each version displays the expected release date and status (e.g., 'Preview' for version 77).
6. Optionally, use the Graph API to list available baselines: GET https://graph.microsoft.com/beta/deviceManagement/templates?$filter=displayName eq 'Microsoft Edge'

## Rollback
1. If a baseline version is missing or incorrect, verify the tenant's licensing and service health at https://admin.microsoft.com/AdminPortal/Home#/servicehealth.
2. If the issue persists, contact Microsoft Support via the Help + support blade in the Intune admin center.
3. No direct rollback is required for viewing baseline versions; the action is read-only. If a baseline was inadvertently assigned, navigate to Endpoint security > Security baselines, select the assigned baseline profile, and change its assignment to 'Not assigned' or delete the profile.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
