# Troubleshooting: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Troubleshooting

## Scenario / Query
How do I view and filter active and closed cases in the Insider Risk Management Cases dashboard?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Insider Risk Management enabled, appropriate role group permissions

## Symptoms
- Unable to locate specific cases in the case queue
- Need to sort cases by status, time opened, or last updated

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to the Reports page to see case reports
2. Use the Cases dashboard to view and act on cases
3. Use the Search control to search for a Case ID or specific text in case names
4. Use the case filter to sort cases by: Time case opened, start date, and end date; Last updated, start date, and end date

## Validation
1. Navigate to the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Go to Insider Risk Management > Cases.
3. Confirm the Cases dashboard displays a list of cases.
4. Use the Search control to search for a known Case ID or text in a case name; verify the expected case appears.
5. Use the case filter to sort by 'Time case opened' with a specific start and end date; verify the list updates accordingly.
6. Use the case filter to sort by 'Last updated' with a specific start and end date; verify the list updates accordingly.
7. Confirm you can view both active and closed cases by checking the status column or filter options.

## Rollback
1. If the Cases dashboard does not load or shows no data, verify the user has the necessary role group permissions (e.g., Insider Risk Management Admin, Insider Risk Management Analysts).
2. If search or filter does not work, clear the search box and reset all filters to default.
3. If the issue persists, check the audit log for any recent configuration changes that might affect case visibility.
4. As a last resort, re-enable Insider Risk Management in the Microsoft Purview compliance portal: Settings > Insider Risk Management > Enable Insider Risk Management.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
