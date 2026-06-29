# Implementation: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Implementation

## Scenario / Query
How to enable Microsoft Teams integration for Insider Risk Management cases so that a Teams team is automatically created when an alert is confirmed and a case is created?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Insider Risk Management settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Microsoft Teams integration for Insider Risk Management in settings.
2. When you confirm an alert and create a case, the solution automatically creates a Microsoft Teams team.
3. Risk investigators and analysts can open Microsoft Teams and navigate directly to the team for a case by selecting 'View Microsoft Teams team' on the case action toolbar.
4. For cases opened before enabling Microsoft Teams integration, select 'Create Microsoft Teams team' on the case action toolbar to create a new team.
5. When you resolve a case, the solution automatically archives the associated Microsoft Team (hides it and turns it to read-only).

## Validation
1. Navigate to Microsoft Purview compliance portal > Insider Risk Management > Settings > General > Microsoft Teams integration. Verify the toggle is enabled. 2. Confirm an alert and create a case. 3. Open the case and verify that 'View Microsoft Teams team' appears on the case action toolbar. 4. Click 'View Microsoft Teams team' and confirm it opens the correct team in Microsoft Teams. 5. For a case created before enabling the integration, select 'Create Microsoft Teams team' on the case action toolbar and verify a new team is created. 6. Resolve the case and confirm the associated team is archived (hidden and read-only) in Microsoft Teams.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Insider Risk Management > Settings > General > Microsoft Teams integration. 2. Disable the toggle to turn off Microsoft Teams integration. 3. For any teams automatically created after enabling integration, manually delete or archive them via Microsoft Teams admin center or PowerShell. 4. For cases where 'View Microsoft Teams team' or 'Create Microsoft Teams team' was used, remove the team association by deleting the team in Microsoft Teams. 5. Notify risk investigators and analysts that the integration is disabled and they must manually create teams if needed.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
