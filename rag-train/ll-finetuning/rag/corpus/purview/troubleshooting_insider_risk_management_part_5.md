# Troubleshooting: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to review case details and alerts in Insider Risk Management cases?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Insider Risk Management enabled, appropriate permissions (Insider Risk Management Analyst or Investigator)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Case overview tab for the case.
2. Review the About this case area for Case ID, Status, Case created on, User's risk score, Email, Organization or department, Manager name, and Manager email.
3. Review the Alerts section for policy matches, status, severity, and time detected.

## Validation
1. Navigate to Microsoft Purview compliance portal > Insider Risk Management > Cases. 2. Open the specific case and verify the Case overview tab displays: Case ID, Status, Case created on, User's risk score, Email, Organization/department, Manager name, and Manager email. 3. In the Alerts section, confirm that policy matches, status, severity, and time detected are listed for each alert.

## Rollback
1. If the case details or alerts are not visible, verify the user has the Insider Risk Management Analyst or Investigator role assigned. 2. Ensure Insider Risk Management is enabled in the tenant. 3. Check that the case was not deleted or archived; if needed, re-create the case from the alert. 4. If alerts are missing, confirm the alert was not dismissed or resolved; use the Alerts tab to filter by status and time range.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
