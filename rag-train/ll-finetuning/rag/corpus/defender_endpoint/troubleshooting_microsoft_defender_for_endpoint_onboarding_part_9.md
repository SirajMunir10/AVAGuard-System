# Troubleshooting: Microsoft Defender for Endpoint onboarding (5)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Microsoft Defender for Endpoint onboarding error Event ID 5?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 5: Microsoft Defender for Endpoint service failed to connect to the server at variable

## Error Codes
- `5`

## Root Causes
N/A

## Remediation Steps
1. Ensure the device has Internet access.

## Validation
1. Run `Test-NetConnection -ComputerName <your_defender_server> -Port 443` to verify outbound connectivity to the Defender for Endpoint service. 2. Check Event Viewer > Applications and Services Logs > Microsoft > Windows > SENSE > Operational for Event ID 5. If no new Event ID 5 appears, connectivity is restored. 3. Confirm the device can resolve the server FQDN using `nslookup <your_defender_server>`. 4. Verify the Microsoft Defender for Endpoint service (Sense) is running with `Get-Service -Name Sense`.

## Rollback
1. If the device had a proxy or firewall rule temporarily disabled for testing, re-enable the original rule. 2. Restore any DNS or network configuration changes made during remediation. 3. Restart the Sense service with `Restart-Service -Name Sense` to re-attempt connection with original settings. 4. Re-run validation steps to confirm the original error persists, indicating rollback success.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
