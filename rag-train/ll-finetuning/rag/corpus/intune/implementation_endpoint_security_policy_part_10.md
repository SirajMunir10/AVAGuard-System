# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites for integrating Microsoft Defender for Endpoint with Intune endpoint security policies?

## Environment Context
- **Tenant Type:** Microsoft Intune with Defender for Endpoint integration
- **Configuration:** Defender for Endpoint P1 or greater license required; service-to-service connection between Intune and Defender for Endpoint tenants; Defender for Endpoint agent installed on target devices; device access to *.dm.microsoft.com endpoints

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure Microsoft Defender for Endpoint P1 or greater license is assigned.
2. Establish service-to-service connection between Intune and Defender for Endpoint tenants.
3. Deploy Defender for Endpoint agent on target devices (required for some policy types).
4. Configure device network connectivity to allow access to *.dm.microsoft.com endpoints for Defender security settings management and policy communication.

## Validation
1. Verify that the tenant has a Microsoft Defender for Endpoint P1 or greater license assigned by navigating to the Microsoft 365 admin center > Billing > Licenses and confirming the Defender for Endpoint license is active and assigned to the appropriate users. 2. Confirm the service-to-service connection by going to Microsoft Intune admin center > Tenant administration > Connectors and tokens > Microsoft Defender for Endpoint and checking that the status shows 'Connected'. 3. On a test device, verify the Defender for Endpoint agent is installed by running 'Get-MpComputerStatus' in PowerShell and confirming the AMProductVersion and AMEngineVersion are present. 4. Test network connectivity to *.dm.microsoft.com by running 'Test-NetConnection -ComputerName dm.microsoft.com -Port 443' from a target device and ensuring it succeeds.

## Rollback
1. If the service-to-service connection causes issues, disconnect it by going to Microsoft Intune admin center > Tenant administration > Connectors and tokens > Microsoft Defender for Endpoint and selecting 'Disconnect'. 2. If the Defender for Endpoint agent deployment causes problems, uninstall the agent from affected devices via Programs and Features or by running 'MpCmdRun.exe -Uninstall' from an elevated command prompt. 3. If network connectivity changes cause issues, revert any firewall or proxy changes that blocked or allowed *.dm.microsoft.com endpoints by restoring the previous configuration. 4. If license assignment causes issues, remove the Defender for Endpoint license from affected users in the Microsoft 365 admin center > Billing > Licenses > select the license > 'Remove licenses'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
