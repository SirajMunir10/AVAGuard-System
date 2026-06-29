# Troubleshooting: Password Reset (SSPR_0029)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve SSPR_0029 error due to on-premises configuration issue?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Password writeback enabled

## Symptoms
- Error SSPR_0029: We are unable to reset your password due to an error in your on-premises configuration. Please contact your admin and ask them to investigate.
- Error SSPR_0029: Your organization hasn't properly set up the on-premises configuration for password reset.
- Event logs on Microsoft Entra Connect system show that the management agent credential was denied access

## Error Codes
- `SSPR_0029`

## Root Causes
1. Policy 'Network access: Restrict clients allowed to make remote calls to SAM' is enabled

## Remediation Steps
1. Use RSOP on the Microsoft Entra Connect system and your domain controllers to see if the policy 'Network access: Restrict clients allowed to make remote calls to SAM' found under Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options is enabled

## Validation
1. On the Microsoft Entra Connect server, open an elevated PowerShell session and run: Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Lsa' -Name 'RestrictRemoteSAM' to confirm the registry value is absent or set to 0. 2. On each domain controller, run: Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Lsa' -Name 'RestrictRemoteSAM' to verify the same. 3. Use RSOP.msc on the Entra Connect server and domain controllers to check that the policy 'Network access: Restrict clients allowed to make remote calls to SAM' is set to 'Not Defined' or disabled. 4. Trigger a test password reset from the Azure portal for a synchronized user and confirm no SSPR_0029 error appears.

## Rollback
1. On the Microsoft Entra Connect server and all domain controllers, re-enable the policy by setting the registry key: Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Lsa' -Name 'RestrictRemoteSAM' -Value 'O:BAG:BAD:(A;;RC;;;BA)' (or the original SDDL string from your environment). 2. Alternatively, use Group Policy Management Console to reapply the policy 'Network access: Restrict clients allowed to make remote calls to SAM' with its original setting. 3. Run gpupdate /force on all affected systems. 4. Verify the error SSPR_0029 returns by attempting a password reset.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
