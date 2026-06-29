# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
How do I access the threat intelligence management interface in the Azure portal or Defender portal?

## Environment Context
- **Tenant Type:** Azure or Defender
- **Configuration:** Threat intelligence management interface

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Defender portal, navigate to Threat intelligence > Intel management.
2. In the Azure portal, navigate to Threat management > Threat intelligence.

## Validation
1. In the Defender portal, go to Threat intelligence > Intel management and confirm the page loads without errors. 2. In the Azure portal, navigate to Threat management > Threat intelligence and verify the interface displays threat indicators. 3. Run the following PowerShell command to list threat intelligence indicators: Get-AzSentinelIndicator -ResourceGroupName <ResourceGroupName> -WorkspaceName <WorkspaceName>. 4. Check that the indicator count matches expected values.

## Rollback
1. If the interface fails to load, clear browser cache and retry. 2. Verify the user has the required permissions (e.g., Security Reader, Security Admin) in Azure RBAC or Azure AD roles. 3. If the issue persists, use the Azure portal's 'Threat intelligence' blade under 'Sentinel' to access the same data. 4. For Defender portal issues, switch to the Azure portal as a fallback.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
