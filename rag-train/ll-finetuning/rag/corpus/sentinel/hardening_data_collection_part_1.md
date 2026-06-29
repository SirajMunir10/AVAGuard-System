# Hardening: Data Collection (Schannel event ID 36874 (TLS handshake completed with a lower protocol))

**Domain:** Sentinel
**Subdomain:** Data Collection
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that Microsoft Sentinel is ingesting logs from a legacy non-Azure source via a Log Analytics agent that is not configured to use TLS 1.2. The administrator wants to ensure all log ingestion to the Sentinel workspace uses encrypted channels and that the agent is hardened per Microsoft best practices. How can the administrator verify and enforce TLS 1.2 for the Log Analytics agent, and what are the documented steps to remediate if the agent is using an older TLS version?

## Environment Context
- **Tenant Type:** Enterprise (hybrid, with on-premises Windows servers sending logs to Sentinel)
- **Configuration:** Log Analytics agent (Windows) version 10.20.18053 or earlier, with default TLS settings

## Symptoms
- Log Analytics agent reports successful connection but uses TLS 1.0 or 1.1
- Security event logs on the agent show Schannel event ID 36874 or 36880 indicating a lower TLS protocol was negotiated
- Sentinel data connectors show no errors, but the connection is not using the recommended TLS 1.2

## Error Codes
- `Schannel event ID 36874 (TLS handshake completed with a lower protocol)`
- `Schannel event ID 36880 (TLS version mismatch warning)`

## Root Causes
1. The Log Analytics agent is not explicitly configured to require TLS 1.2
2. The underlying Windows operating system may have TLS 1.0 or 1.1 enabled and preferred
3. The agent version may be older than the minimum that supports enforced TLS 1.2

## Remediation Steps
1. Ensure the Log Analytics agent is updated to version 10.20.18053 or later (the first version that supports TLS 1.2 enforcement).
2. On the agent machine, set the registry key HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client to enable TLS 1.2 and disable older protocols per Microsoft guidance.
3. Configure the Log Analytics agent to use TLS 1.2 by setting the environment variable 'AZURE_LOG_ANALYTICS_TLS_VERSION' to '1.2' or by using the agent's configuration file (if documented).
4. Restart the Log Analytics service (HealthService) after making registry changes.
5. Verify the change by checking that Schannel event IDs 36874/36880 no longer appear and that the agent connects using TLS 1.2.

## Validation
Run the following PowerShell command on the agent machine to confirm TLS 1.2 is enabled and used: [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; $tlsTest = [Net.ServicePointManager]::SecurityProtocol; Write-Host 'Current TLS protocol: ' $tlsTest. Additionally, check the Log Analytics agent logs (C:\Program Files\Microsoft Monitoring Agent\Agent\Health Service State\*.log) for 'TLS 1.2' entries.

## Rollback
Revert the registry changes by setting the DisabledByDefault value for TLS 1.2 Client back to 0 (or deleting the key) and restarting the HealthService. If the environment variable was set, remove it and restart the service.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/agents/agent-windows-tls>
- <https://learn.microsoft.com/en-us/azure/sentinel/best-practices-data>
