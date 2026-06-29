# Incident Response: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Incident Response

## Scenario / Query
How to resolve an insider risk management case after review and investigation?

## Environment Context
- **Tenant Type:** Microsoft 365 organization
- **Configuration:** Insider Risk Management solution enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal with credentials for an admin account in your Microsoft 365 organization.
2. Go to the Insider Risk Management solution.
3. Select Cases in the left navigation.
4. Select a case, and then select Resolve case on the case action toolbar.
5. In the Resolve case dialog box, select the Resolve as dropdown control to select the resolution classification for the case. The options are Benign or Confirmed policy violation.
6. In the Resolve case dialog box, enter the reasons for the resolution classification in the Action taken text field.
7. Select Resolve to close the case.

## Validation
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com) with an admin account. 2. Navigate to Insider Risk Management > Cases. 3. Locate the resolved case and verify its status shows 'Resolved' and the resolution classification (Benign or Confirmed policy violation) is displayed. 4. Open the case details to confirm the 'Action taken' text is present and matches the expected reason. 5. Optionally, use the audit log to search for 'CaseResolved' activity by the resolving admin to confirm the action was recorded.

## Rollback
1. Sign in to the Microsoft Purview portal with an admin account. 2. Go to Insider Risk Management > Cases. 3. Select the resolved case. 4. On the case action toolbar, select 'Reopen case'. 5. In the confirmation dialog, select 'Reopen' to restore the case to an active state. 6. If the resolution classification was incorrect, update the case details as needed after reopening.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
