# Implementation: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Implementation

## Scenario / Query
How to filter and view threat reports by category in Microsoft Defender Threat Analytics?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Threat Analytics dashboard

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. To add report filter types in your dashboard, select Filters, choose from the list, and select Add.
2. To set the types of reports you want in the list based on the available filters, select a filter type (for example, Threat tags), choose from the list, and select Apply.

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Threat Analytics under the Reports section.
3. On the Threat Analytics dashboard, click the 'Filters' button.
4. In the filter pane, select a filter type (e.g., 'Threat tags') from the dropdown.
5. Choose one or more values from the list (e.g., 'Ransomware', 'Phishing').
6. Click 'Apply' to filter the reports.
7. Confirm that the displayed threat reports are now limited to the selected category.
8. Verify that the filter badge appears on the dashboard and that the URL reflects the applied filter parameters.

## Rollback
1. On the Threat Analytics dashboard, click the 'Filters' button to open the filter pane.
2. Click 'Clear filters' or remove each applied filter by clicking the 'X' next to the filter badge.
3. Confirm that all filters are removed and the dashboard returns to showing all threat reports.
4. If the dashboard fails to load or shows incorrect data, refresh the page or navigate away and back to Threat Analytics.
5. If issues persist, clear browser cache and cookies, then re-access the Microsoft 365 Defender portal.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
