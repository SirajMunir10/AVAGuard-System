# Troubleshooting: Exchange On-Premises Policy

**Domain:** Intune
**Subdomain:** Exchange On-Premises Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the 'Saving of Access Rules to Exchange has Failed' alert in the Intune admin console when using Microsoft 365?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange On-Premises Policy workspace

## Symptoms
- Alert: 'Saving of Access Rules to Exchange has Failed' in the admin console
- Configured policy settings are not enforced by Intune

## Error Codes
N/A

## Root Causes
1. Policies created in the Exchange On-Premises Policy workspace (Admin console) while using Microsoft 365

## Remediation Steps
1. Note the policy source in the alert
2. Under the Exchange On-premises Policy workspace, delete the legacy rules (Global Exchange rules within Intune for on-premises Exchange, not relevant to Microsoft 365)
3. Create new policy for Microsoft 365

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Devices > Configuration profiles > Policies.
3. Confirm that no policies remain under the 'Exchange On-premises Policy' workspace.
4. Verify that a new policy has been created under the appropriate Microsoft 365 policy section (e.g., 'Devices > Configuration profiles > Create profile' with platform 'Windows 10 and later' or 'iOS/iPadOS' as applicable).
5. Wait 10–15 minutes, then check that the alert 'Saving of Access Rules to Exchange has Failed' no longer appears in the admin console.
6. On a test device enrolled in Intune, confirm that the new policy settings are applied (e.g., via Settings > Accounts > Access work or school > Info > Sync).

## Rollback
1. If the alert persists or new issues arise, sign in to the Microsoft Intune admin center.
2. Navigate to Devices > Configuration profiles > Policies.
3. Delete the newly created Microsoft 365 policy that was added as part of the remediation.
4. Recreate the legacy Exchange on-premises rules by going to the 'Exchange On-premises Policy' workspace and adding the same rules that were previously deleted.
5. Wait 10–15 minutes and confirm that the original alert 'Saving of Access Rules to Exchange has Failed' returns (indicating rollback of the fix).
6. If needed, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
