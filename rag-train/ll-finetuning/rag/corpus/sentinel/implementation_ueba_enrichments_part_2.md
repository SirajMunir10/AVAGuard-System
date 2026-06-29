# Implementation: UEBA Enrichments

**Domain:** Sentinel
**Subdomain:** UEBA Enrichments
**Incident Type:** Implementation

## Scenario / Query
How to interpret and use the UsersInsights, DevicesInsights, and ActivityInsights dynamic fields in the BehaviorAnalytics table for UEBA enrichment in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel UEBA enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the BehaviorAnalytics table in Microsoft Sentinel logs.
2. Review the UsersInsights dynamic field for user-related enrichments such as AccountDisplayName, AccountDomain, AccountObjectID, BlastRadius, IsDormantAccount, IsLocalAdmin, IsNewAccount, and OnPremisesSID.
3. Review the DevicesInsights dynamic field for device-related enrichments such as Browser, DeviceFamily, DeviceType, OperatingSystem, ThreatIntelIndicatorDescription, ThreatIntelIndicatorType, UserAgent, and UserAgentFamily.
4. Review the ActivityInsights dynamic field for activity-related enrichments such as FirstTimeUserPerformedAction and ActionUncommonlyPerformedByUser.
5. Ensure the Manager property is populated in Microsoft Entra ID for BlastRadius to be calculated.

## Validation
1. Run the following KQL query in Microsoft Sentinel Logs to confirm the BehaviorAnalytics table contains the expected dynamic fields:
  BehaviorAnalytics
  | take 10
  | project UsersInsights, DevicesInsights, ActivityInsights
2. Verify that UsersInsights includes fields such as AccountDisplayName, AccountDomain, AccountObjectID, BlastRadius, IsDormantAccount, IsLocalAdmin, IsNewAccount, and OnPremisesSID.
3. Verify that DevicesInsights includes fields such as Browser, DeviceFamily, DeviceType, OperatingSystem, ThreatIntelIndicatorDescription, ThreatIntelIndicatorType, UserAgent, and UserAgentFamily.
4. Verify that ActivityInsights includes fields such as FirstTimeUserPerformedAction and ActionUncommonlyPerformedByUser.
5. Check that the Manager property is populated in Microsoft Entra ID for users to ensure BlastRadius is calculated.

## Rollback
1. If UEBA enrichment data is incorrect or missing, disable and re-enable UEBA in Microsoft Sentinel:
   - Navigate to Microsoft Sentinel > Entity behavior configuration > Set UEBA to Off, then back to On.
2. If the Manager property was incorrectly modified in Microsoft Entra ID, restore the previous Manager value using Microsoft Entra admin center or PowerShell.
3. If custom enrichment fields were added incorrectly, remove them from the BehaviorAnalytics table schema by reverting any manual schema changes.
4. If the issue persists, contact Microsoft Support for assistance with UEBA data pipeline.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/ueba-enrichments>
