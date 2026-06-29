# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to check if Pass-through Authentication is enabled and Authentication Agents are active?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Pass-through Authentication feature

## Symptoms
- Authentication failures or issues with pass-through authentication

## Error Codes
N/A

## Root Causes
1. Pass-through Authentication feature may be disabled
2. Authentication Agents may show Inactive status

## Remediation Steps
1. Go to the Microsoft Entra Connect blade on the Microsoft Entra admin center
2. Check that the Pass-through Authentication feature is still Enabled
3. Verify that the status of Authentication Agents shows Active, not Inactive

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Hybrid Identity Administrator. 2. Navigate to Identity > Hybrid management > Microsoft Entra Connect > Pass-through authentication. 3. Confirm the status shows 'Enabled' for the feature. 4. Under 'Authentication agents', verify that at least one agent displays a status of 'Active'. 5. Optionally, run the PowerShell command `Get-MsolAuthenticationAgent` (requires MSOnline module) to list agents and confirm their status is 'Active'.

## Rollback
1. If the feature is disabled, re-enable it by selecting 'Enable' in the Pass-through authentication blade. 2. If agents show 'Inactive', download and install the latest Authentication Agent from the same blade, or restart the agent service on the server (services.msc -> 'Microsoft Azure AD Connect Authentication Agent' -> Restart). 3. If issues persist, revert to the previous configuration by disabling Pass-through Authentication and enabling Password Hash Synchronization (if it was previously the fallback).

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
