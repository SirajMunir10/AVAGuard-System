# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How to implement endpoint security policies in Microsoft Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Endpoint security policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Explore the Endpoint security overview
2. Review security baselines for comprehensive security configurations
3. Learn about reusable settings groups
4. Configure Microsoft Defender for Endpoint integration
5. Understand device protection strategies

## Validation
1. Navigate to Microsoft Intune admin center > Endpoint security > Overview. Confirm the dashboard displays security posture summaries and policy compliance status. 2. Go to Endpoint security > Security baselines. Verify at least one baseline (e.g., Microsoft Defender for Endpoint baseline) is assigned and shows a compliance state. 3. Under Endpoint security > Antivirus, ensure a policy exists with a valid assignment to a test group. 4. On a managed Windows device, run 'Get-MpComputerStatus' in PowerShell to confirm real-time protection is enabled and policy settings match the assigned Intune policy. 5. In Endpoint security > Microsoft Defender for Endpoint, confirm integration status shows 'Enabled' and connector health is 'Active'.

## Rollback
1. In Intune admin center, go to Endpoint security > Antivirus, select the newly created policy, and choose 'Delete' to remove it. 2. Navigate to Endpoint security > Security baselines, select the assigned baseline, and click 'Unassign' to remove it from all groups. 3. Under Endpoint security > Microsoft Defender for Endpoint, toggle the integration setting to 'Disabled' and save. 4. If any reusable settings groups were created, go to Tenant administration > Groups > All groups, locate the custom group, and delete it. 5. On affected devices, run 'Set-MpPreference -DisableRealtimeMonitoring $true' in PowerShell to revert real-time protection to default (if needed).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
