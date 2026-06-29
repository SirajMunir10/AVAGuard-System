# Implementation: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Implementation

## Scenario / Query
A customer enabled the 'Defender for Cloud security posture management (CSPM) plan' on their Azure subscription but cannot see any recommendations for their Azure SQL databases. What is the most likely cause and how should they enable the necessary Defender plan?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Subscription has Azure SQL databases deployed; only the foundational CSPM plan (formerly 'Defender for Cloud free tier') is enabled.

## Symptoms
- No security recommendations appear for Azure SQL databases in Defender for Cloud
- The 'Defender for Cloud | Recommendations' blade is empty for SQL resources
- The 'Defender for Cloud | Workload protections' dashboard shows no SQL-specific alerts

## Error Codes
N/A

## Root Causes
1. The 'Defender for Cloud CSPM' plan provides only foundational posture assessments and does not include SQL-specific threat detection or advanced recommendations.
2. To receive SQL-specific recommendations and alerts, the 'Defender for SQL' plan must be enabled on the subscription or the individual SQL servers/databases.

## Remediation Steps
1. Navigate to Microsoft Defender for Cloud > Environment settings > Select the subscription.
2. Under 'Defender plans', locate 'Defender for SQL' and set the toggle to 'On'.
3. Alternatively, use the Azure CLI: az security pricing create --name 'SqlServers' --pricing-tier 'Standard'
4. Wait up to 24 hours for the initial assessment to complete and recommendations to appear.

## Validation
After enabling Defender for SQL, verify that recommendations such as 'Vulnerability assessment should be enabled on your SQL servers' appear under the 'Recommendations' blade. Also confirm that the 'Workload protections' dashboard shows SQL-specific alerts.

## Rollback
Set the 'Defender for SQL' plan toggle to 'Off' in the subscription's Defender plans blade, or run: az security pricing create --name 'SqlServers' --pricing-tier 'Free'

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security>
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-sql-introduction>
