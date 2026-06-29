# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to enable user overrides for DLP policy blocking actions in Exchange, SharePoint, OneDrive, or Teams?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with 'Notify users in Office 365 services with a policy tip' enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable 'Notify users in Office 365 services with a policy tip' to allow user overrides
2. User overrides are enabled only when this notification setting is enabled
3. User overrides are not available for the On-premises repositories location

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was modified. 3. Under 'Actions', confirm that 'Notify users in Office 365 services with a policy tip' is enabled. 4. Under 'User overrides', verify that 'Allow users to override the policy' is set to 'Yes' (or 'Allow override without justification' or 'Allow override with justification' as appropriate). 5. Send a test email containing sensitive information to a user in the policy scope and confirm that a Policy Tip appears with an override option. 6. For SharePoint/OneDrive, upload a sensitive document and verify the Policy Tip and override option appear. 7. For Teams, send a sensitive message and confirm the Policy Tip and override option appear.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was modified. 3. Under 'User overrides', set the override option to 'No' (or 'Do not allow users to override'). 4. If the 'Notify users in Office 365 services with a policy tip' setting was not previously enabled, disable it. 5. Save the policy. 6. Confirm that users no longer see an override option in Policy Tips for the affected locations (Exchange, SharePoint, OneDrive, Teams).

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
