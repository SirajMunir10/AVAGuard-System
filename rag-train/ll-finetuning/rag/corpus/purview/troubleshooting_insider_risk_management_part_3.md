# Troubleshooting: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to search for alerts in Insider Risk Management cases using user principal name, assigned admin name, or Alert ID?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5 or Insider Risk Management add-on
- **Configuration:** Insider Risk Management enabled and configured

## Symptoms
- Unable to locate specific alerts in the Insider Risk Management case list

## Error Codes
N/A

## Root Causes
1. Large volume of alerts making manual search difficult

## Remediation Steps
1. Use the Search control to search for a user principal name (UPN)
2. Use the Search control to search for an assigned admin name
3. Use the Search control to search for an Alert ID

## Validation
1. Navigate to Microsoft Purview compliance portal > Insider Risk Management > Cases. 2. In the Search control on the Cases page, enter a known user principal name (UPN) from a case and verify the case list filters to show only matching cases. 3. Clear the search, then enter an assigned admin name and confirm the list updates accordingly. 4. Clear the search, then enter a known Alert ID and verify the specific case appears. 5. Repeat with multiple UPNs, admin names, and Alert IDs to ensure consistent filtering.

## Rollback
1. Clear the Search control by deleting any text entered. 2. Refresh the Cases page to restore the full list of cases. 3. If the search feature is unresponsive, close and reopen the Insider Risk Management section in the Purview portal. 4. If issues persist, verify that the user has the necessary permissions (Insider Risk Management Admin role) and that the tenant is properly licensed (Microsoft 365 E5/A5/G5 or add-on). 5. As a last resort, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
