# Troubleshooting: Windows Autopilot (0x80070774)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why are Windows Autopilot Hybrid deployments failing during ESP with error code 0x80070774?

## Environment Context
- **Tenant Type:** Hybrid Azure AD joined
- **Configuration:** Intune Connector for Active Directory

## Symptoms
- Windows Autopilot Hybrid deployments fail during ESP

## Error Codes
- `0x80070774`

## Root Causes
1. Domain mismatch between where the Intune Connector for Active Directory is installed and where device configurations are targeted

## Remediation Steps
1. Configure the Intune Connector for Active Directory in the matching domain

## Validation
1. Verify that the Intune Connector for Active Directory is installed in the domain that matches the target domain for device configurations. Run 'Get-ADSite' or check the connector server's domain membership via 'System Properties > Computer Name/Domain Changes'. 2. In the Microsoft Intune admin center, navigate to 'Devices > Windows > Windows enrollment > Intune Connector for Active Directory' and confirm the connector status shows 'Active' and the domain name matches the target domain. 3. Trigger a new Autopilot deployment for a test device and monitor the Enrollment Status Page (ESP) to ensure it completes without error 0x80070774.

## Rollback
1. If the remediation fails or causes issues, reinstall the Intune Connector for Active Directory in the original domain by running the connector installer and selecting the previous domain during setup. 2. In the Intune admin center, remove the misconfigured connector entry under 'Devices > Windows > Windows enrollment > Intune Connector for Active Directory' and wait for the new connector to appear. 3. Revert any Autopilot profile changes that were made to target the new domain, and test a deployment to confirm the original error reappears or the system returns to the previous state.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
