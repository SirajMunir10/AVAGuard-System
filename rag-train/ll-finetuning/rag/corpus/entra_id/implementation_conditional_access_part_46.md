# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to require a Microsoft Entra hybrid joined device in a Conditional Access policy?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with hybrid identity
- **Configuration:** Devices must already be Microsoft Entra hybrid joined

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Requiring a Microsoft Entra hybrid joined device is dependent on your devices already being Microsoft Entra hybrid joined.
2. For more information, see the article Configure Microsoft Entra hybrid join.

## Validation
1. Confirm that the Conditional Access policy is assigned to the correct users/groups and cloud apps. Use: Get-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "<PolicyId>" | Select-Object -ExpandProperty Conditions. 2. Verify the policy grants block access or require hybrid joined device: (Get-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "<PolicyId>").GrantControls.BuiltInControls -contains "domainJoined". 3. Test sign-in from a hybrid joined device: Sign in as a test user from a device that is Microsoft Entra hybrid joined and confirm access is granted. 4. Test sign-in from a non-hybrid joined device: Sign in from a device that is not hybrid joined and confirm access is blocked. 5. Check device registration status: dsregcmd /status on a Windows device should show "AzureAdJoined : YES" and "DomainJoined : YES".

## Rollback
1. Disable the Conditional Access policy: Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "<PolicyId>" -State "disabled". 2. If the policy was created new, delete it: Remove-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "<PolicyId>". 3. If the policy was modified, revert to previous settings using a backup or documented configuration. 4. Notify affected users that the policy has been rolled back and access restrictions are removed. 5. Monitor sign-in logs for any residual blocks: Get-MgAuditLogSignIn -Filter "status/errorCode eq 53003" -Top 10.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
- <https://learn.microsoft.com/en-us/entra/identity/devices/hybrid-join-plan>
