# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
What are the available security baseline versions for Microsoft 365 Apps for Enterprise in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Microsoft 365 Apps for Enterprise security baseline

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Version 2306 (Office baseline) - Released in November 2023
2. May 2023 (Office baseline)

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Select 'Microsoft 365 Apps for Enterprise' from the list of available baselines.
4. Verify that the baseline versions listed include 'Version 2306 (Office baseline) - Released in November 2023' and 'May 2023 (Office baseline)'.
5. Optionally, use the Microsoft Graph API to confirm: GET https://graph.microsoft.com/beta/deviceManagement/templates?$filter=displayName eq 'Microsoft 365 Apps for Enterprise'&$select=id,displayName,versionInfo,description

## Rollback
1. If the remediation introduced unintended changes, navigate to Endpoint security > Security baselines in the Intune admin center.
2. Select the 'Microsoft 365 Apps for Enterprise' baseline profile that was assigned.
3. Choose 'Properties' and then 'Settings' to review the configuration.
4. Revert any modified settings to their previous values or reassign a previously known good baseline version (e.g., switch from 'Version 2306' to 'May 2023' or vice versa).
5. Save the changes and allow the policy to propagate to devices.
6. Monitor device compliance and user-reported issues to confirm rollback success.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
