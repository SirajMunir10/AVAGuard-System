# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I connect Microsoft Defender for Identity to sync user entities from on-premises Active Directory to Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace, Microsoft Defender for Identity enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the Go the UEBA configuration page link.
2. In the Entity behavior configuration page, if you didn't enable UEBA, then at the top of the page, move the toggle to On.
3. Mark the Active Directory (Preview) check box and select Apply.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Entity behavior configuration (UEBA settings).
2. Verify the UEBA toggle is set to On.
3. Confirm the Active Directory (Preview) check box is selected and the Apply button was successfully clicked.
4. In Microsoft Sentinel, go to Entity behavior > Entity search and search for a known on-premises Active Directory user. Confirm the user entity appears with expected attributes (e.g., SAM account name, domain).
5. Alternatively, run the following KQL query in the Sentinel Logs workspace:
   ```kusto
   BehaviorAnalytics
   | where TimeGenerated > ago(1h)
   | where Users has "<test_user_UPN>"
   | take 10
   ```
   If results return, the connector is syncing user entities.

## Rollback
1. In the Microsoft Sentinel workspace, navigate to Entity behavior configuration (UEBA settings).
2. If UEBA was enabled solely for this integration, move the UEBA toggle to Off.
3. If UEBA should remain enabled but the Active Directory sync must be removed, clear the Active Directory (Preview) check box and select Apply.
4. Verify the change by repeating the validation steps; the previously synced user entities will no longer appear in new queries (existing data may persist for up to 30 days).

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
