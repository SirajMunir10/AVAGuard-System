# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve configuration and connectivity issues between Microsoft Entra ID and local Active Directory Domain Services for SSPR writeback by reinstalling Microsoft Entra Connect?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Configuration and connectivity issues between Microsoft Entra ID and local Active Directory Domain Services environment

## Error Codes
N/A

## Root Causes
1. Outdated or misconfigured Microsoft Entra Connect installation

## Remediation Steps
1. Back up any customized out-of-the-box sync rules before proceeding with the upgrade.
2. Download the latest version of Microsoft Entra Connect from the Microsoft Entra Admin Center under the Manage tab of the Microsoft Entra Connect | Get started page.
3. Perform an in-place upgrade by running the downloaded package and following the on-screen instructions to update Microsoft Entra Connect.
4. If the issue persists, after installing the latest version, disable and then re-enable password writeback as a final step.

## Validation
N/A

## Rollback
Manually redeploy any customized out-of-the-box sync rules after the upgrade.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
