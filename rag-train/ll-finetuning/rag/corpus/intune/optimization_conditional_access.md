# Optimization: Conditional Access

**Domain:** Intune
**Subdomain:** Conditional Access
**Incident Type:** Optimization

## Scenario / Query
How to clean up classic Conditional Access policies for Defender for Endpoint?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Classic Conditional Access policies for Defender for Endpoint

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. As of August 2023, Intune no longer creates classic Conditional Access policies for Defender for Endpoint.
2. If your tenant has legacy policies from previous integrations, you can safely delete them.
3. To check: Azure portal > Entra ID > Conditional Access > Classic policies .

## Validation
1. Navigate to Azure portal > Microsoft Entra ID > Conditional Access > Classic policies. 2. Confirm no classic policies with names containing 'Microsoft Defender for Endpoint' or 'Windows Defender ATP' are listed. 3. If any such policies exist, verify they are in a disabled or inactive state before proceeding.

## Rollback
1. If a classic policy was deleted and needs recovery, use Azure PowerShell: Connect-MgGraph -Scopes 'Policy.ReadWrite.ConditionalAccess'; New-MgIdentityConditionalAccessPolicy -BodyParameter @{displayName='Restored Classic Policy'; state='disabled'; conditions=@{...}; grantControls=@{builtInControls='mfa'}}. 2. Alternatively, recreate the policy manually in Azure portal > Microsoft Entra ID > Conditional Access > Classic policies using the original settings from backup or documentation.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
