# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra hybrid join failures related to outbound proxy authentication?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** On-premises environment with outbound proxy

## Symptoms
- Events 1022 in Microsoft Entra analytics logs
- Events 1084 in Microsoft Entra operational logs

## Error Codes
N/A

## Root Causes
1. Computer account of the device cannot discover the outbound proxy
2. Computer account of the device cannot silently authenticate to the outbound proxy

## Remediation Steps
1. Ensure the computer account of the device can discover the outbound proxy
2. Ensure the computer account of the device can silently authenticate to the outbound proxy

## Validation
1. On the affected device, open an elevated PowerShell prompt and run: `netsh winhttp show proxy` to confirm the proxy address is correctly configured. 2. Verify the computer account can reach the proxy by running: `Test-NetConnection -ComputerName <proxy-address> -Port <proxy-port>`. 3. Check Microsoft Entra analytics logs for Event 1022 and operational logs for Event 1084; confirm no new occurrences after remediation. 4. Run `dsregcmd /status` and verify the AzureAdJoined field is YES and the DomainJoined field is YES.

## Rollback
1. If proxy discovery was modified (e.g., via Group Policy or registry), revert to the previous proxy configuration. 2. If proxy authentication settings were changed (e.g., via `netsh winhttp set proxy`), restore the original proxy address and port. 3. Re-enable any disabled firewall rules or network policies that were temporarily adjusted. 4. Restart the device to reapply original settings and re-trigger hybrid join attempt.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
