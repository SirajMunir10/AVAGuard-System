# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the Download file button disabled when trying to collect a file from a Defender for Endpoint alert?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** RBAC permissions for file collection

## Symptoms
- Download file button is grayed out or disabled during an active collection attempt

## Error Codes
N/A

## Root Causes
1. Insufficient RBAC permissions to collect files

## Remediation Steps
1. For Microsoft Defender Unified role-based access control (RBAC): Add file collection permission in Microsoft Defender Unified (RBAC)
2. For Microsoft Defender for Endpoint role-based access control (RBAC): For Portable Executable files (.exe, .sys, .dll, and others): ensure user has Security Administrator or Advanced live response or Alerts permissions
3. For Microsoft Defender for Endpoint role-based access control (RBAC): For Non-Portable Executable file (.txt, .docx, and others): ensure user has Security Administrator or Advanced live response permissions

## Validation
1. Confirm the user's assigned RBAC role in Microsoft Defender for Endpoint: navigate to Microsoft 365 Defender > Permissions > Endpoint roles > select the role assigned to the user. 2. Verify the role includes 'Advanced live response' permission for non-PE files, or 'Advanced live response' and 'Alerts' permissions for PE files. 3. For Unified RBAC, navigate to Microsoft 365 Defender > Permissions > Microsoft Defender Unified > select the role and confirm 'File collection' permission is enabled. 4. Attempt to collect a file from an alert: open an alert, click 'Collect file', and verify the 'Download file' button is enabled.

## Rollback
1. Remove the 'File collection' permission from the user's Unified RBAC role: navigate to Microsoft 365 Defender > Permissions > Microsoft Defender Unified > edit the role > uncheck 'File collection'. 2. For Endpoint RBAC, remove 'Advanced live response' and/or 'Alerts' permissions from the user's role: navigate to Microsoft 365 Defender > Permissions > Endpoint roles > edit the role > uncheck the relevant permissions. 3. If the user was assigned a custom role, revert to the previous role assignment by reassigning the original role.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
