# Implementation: Firewall

**Domain:** Intune
**Subdomain:** Firewall
**Incident Type:** Implementation

## Scenario / Query
How to configure built-in firewall protection and network segmentation using Intune firewall policies?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Firewall policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Firewall policy type to configure built-in firewall protection.
2. Platform support: Windows, macOS.
3. Available profiles: Windows Firewall, Windows Firewall rules, macOS Firewall.
4. Use case: Control network access and implement network segmentation.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Firewall and confirm that the firewall policy is listed with a status of 'Succeeded' for the assigned groups.
2. On a target Windows device, open PowerShell as administrator and run 'Get-NetFirewallProfile | Select-Object Name, Enabled' to verify that the firewall profile is enabled.
3. On a target macOS device, run 'sudo /usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate' to confirm the firewall is enabled.
4. Test network segmentation by attempting to connect to a blocked port or IP from a managed device and verify the connection is denied.

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint security > Firewall, select the firewall policy, and choose 'Delete' to remove the policy.
2. On Windows devices, run 'Set-NetFirewallProfile -All -Enabled False' in PowerShell to disable the firewall if needed.
3. On macOS devices, run 'sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate off' to disable the firewall.
4. Monitor device compliance and connectivity to ensure the rollback is effective.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
