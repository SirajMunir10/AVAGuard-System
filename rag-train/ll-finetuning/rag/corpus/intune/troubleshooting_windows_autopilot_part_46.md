# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the error 'That username looks like it belongs to another organization' during Windows Autopilot deployment?

## Environment Context
- **Tenant Type:** Azure AD/Entra ID tenant
- **Configuration:** Windows Autopilot deployment profile

## Symptoms
- Error message: 'That username looks like it belongs to another organization. Try signing in again or start over with a different account'

## Error Codes
N/A

## Root Causes
1. Incorrect or conflicting information in the registry key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot

## Remediation Steps
1. Confirm that all of the information is correct in the registry key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot
2. For more information, see 'Where are the Windows Autopilot profile settings received from the Windows Autopilot deployment service stored?'

## Validation
1. Open Registry Editor (regedit) as Administrator. 2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot. 3. Verify that the values for 'CloudAssignedTenantId', 'CloudAssignedTenantDomain', and 'CloudAssignedTenantName' match your Azure AD/Entra ID tenant ID, domain, and tenant name exactly. 4. Confirm there are no extra spaces or characters in any value. 5. Restart the device and attempt the Autopilot deployment again; the error should no longer appear.

## Rollback
1. Open Registry Editor (regedit) as Administrator. 2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot. 3. If you modified any values, restore them to their original state (if known) or delete the registry key entirely (note: this may require re-enrollment). 4. Alternatively, perform a full device reset to clear all provisioning data and start fresh. 5. After rollback, the original error may reappear; proceed with alternative troubleshooting steps as documented in the source reference.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
