# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix 'The service is stopped' error?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The service is stopped. Service name: %1

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Start the mentioned service
2. Contact support if the issue persists

## Validation
Run the following PowerShell command to verify the service status: Get-Service -Name <ServiceName> | Select-Object Status,Name. Confirm the Status is 'Running'. If the service name is unknown, run Get-Service | Where-Object {$_.DisplayName -like '*Microsoft Defender*'} to list relevant services.

## Rollback
If the service fails to start or causes issues, run Stop-Service -Name <ServiceName> -Force to stop the service, then set it back to its original startup type using Set-Service -Name <ServiceName> -StartupType <OriginalStartupType>. If the original startup type is unknown, set it to 'Manual' as a safe default. Contact Microsoft support if the problem persists.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
