# Hardening: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that the 'Endpoint protection' recommendation in Microsoft Defender for Cloud shows a 'Unhealthy' status for several Azure VMs. How should the administrator investigate and remediate this hardening gap?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender for Cloud is enabled with the 'Endpoint protection' recommendation (CIS Benchmark control 7.1). The affected VMs are running Windows Server 2019 and have Microsoft Defender Antivirus installed but not properly configured.

## Symptoms
- Microsoft Defender for Cloud dashboard shows 'Endpoint protection' recommendation with 'Unhealthy' status for multiple VMs
- Security alerts related to missing or misconfigured antimalware solutions
- Compliance dashboard indicates failure for CIS Benchmark control 7.1

## Error Codes
N/A

## Root Causes
1. Microsoft Defender Antivirus is not installed or is disabled on the affected VMs
2. The antimalware extension is not deployed or is not reporting health status to Azure
3. Group Policy or local policy disables real-time protection or signature updates

## Remediation Steps
1. 1. In the Azure portal, navigate to Microsoft Defender for Cloud > Recommendations > 'Endpoint protection' and identify the unhealthy resources.
2. 2. For each unhealthy VM, verify that the Microsoft Antimalware extension is installed. If not, install it using the Azure portal or PowerShell: Set-AzVMExtension -Publisher Microsoft.Azure.Security -ExtensionType IaaSAntimalware -Name AntimalwareExtension -VMName <VMName> -ResourceGroupName <RGName> -Settings @{"AntimalwareEnabled"=true}
3. 3. Ensure that Microsoft Defender Antivirus is enabled and running with real-time protection active. On Windows, run: Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
4. 4. If real-time protection is disabled, enable it via Group Policy or locally: Set-MpPreference -DisableRealtimeMonitoring $false
5. 5. Verify that signature updates are current. Run: Update-MpSignature
6. 6. After remediation, wait up to 24 hours for Defender for Cloud to reassess the recommendation, or manually trigger a scan using the 'Refresh' button on the recommendation page.

## Validation
After remediation, the 'Endpoint protection' recommendation should show 'Healthy' status for the affected VMs within 24 hours. You can also run 'Get-AzSecurityAssessment -Name 'Endpoint protection' | Select-Object Status' to verify the assessment status programmatically.

## Rollback
To roll back, uninstall the antimalware extension via Azure portal or PowerShell: Remove-AzVMExtension -ResourceGroupName <RGName> -VMName <VMName> -Name AntimalwareExtension. Reapply any previous Group Policy settings that disabled real-time protection.

## References
- Microsoft Learn: 'Endpoint protection recommendation in Microsoft Defender for Cloud' â€” https://learn.microsoft.com/en-us/azure/defender-for-cloud/endpoint-protection-recommendations-technical
- Microsoft Learn: 'Install and configure Microsoft Antimalware for Azure' â€” https://learn.microsoft.com/en-us/azure/security/fundamentals/antimalware
