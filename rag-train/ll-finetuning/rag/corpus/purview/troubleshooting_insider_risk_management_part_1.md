# Troubleshooting: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to filter cases in the Insider Risk Management Cases dashboard when reviewing a large queue of cases?

## Environment Context
- **Tenant Type:** Purview
- **Configuration:** Insider Risk Management policies

## Symptoms
- Large number of active cases in the Cases dashboard
- Difficulty sorting or reviewing cases by specific attributes

## Error Codes
N/A

## Root Causes
1. No filters applied to the case list

## Remediation Steps
1. Navigate to the Cases dashboard in Insider Risk Management
2. Select the Filter control
3. Filter cases by one or more attributes: Status (Active or Closed), Time case opened (start and end dates), Last updated (start and end dates)

## Validation
Case list is filtered by selected attributes

## Rollback
Clear all filter selections to return to unfiltered view

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
