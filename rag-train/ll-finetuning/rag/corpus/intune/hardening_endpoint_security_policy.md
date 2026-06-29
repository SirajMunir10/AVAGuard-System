# Hardening: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Hardening

## Scenario / Query
How to prevent policy conflicts through strategic planning in Intune endpoint security?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint security policies, security baselines

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Plan policy architecture before implementation
2. Document which policy types manage specific settings
3. Use consistent configuration approaches across policy types
4. Apply security baselines as primary configuration sources where appropriate

## Validation
1. Verify that no conflicting policies exist by running: Get-DeviceCompliancePolicy | Where-Object {$_.SettingStateDeviceSummary -match 'conflict'} 2. Confirm that each setting is managed by only one policy type using: Get-ManagementCondition | Select-Object -Property DisplayName, SettingName 3. Validate that security baselines are applied as primary sources: Get-SecurityBaselineTemplate | Where-Object {$_.IsDefault -eq $true} 4. Check policy assignment reports for overlapping assignments: Get-DeviceConfigurationPolicyAssignment | Group-Object -Property DeviceId | Where-Object {$_.Count -gt 1}

## Rollback
1. Remove conflicting policy assignments: Remove-DeviceConfigurationPolicyAssignment -PolicyId <PolicyId> -DeviceId <DeviceId> 2. Revert to previous policy architecture by restoring documented policy hierarchy: Set-DeviceCompliancePolicy -Id <PolicyId> -Priority <OriginalPriority> 3. Disable security baseline if causing conflicts: Set-SecurityBaselineTemplate -Id <TemplateId> -IsDefault $false 4. Reapply original configuration approaches: New-DeviceConfigurationPolicy -Name 'OriginalPolicy' -Settings <OriginalSettings>

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
