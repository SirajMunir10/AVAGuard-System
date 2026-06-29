# Implementation: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Implementation

## Scenario / Query
How to add a case note in an insider risk management case in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
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
4. Select a case, then select the Case notes tab.
5. Select Add case note.
6. In the Add case note dialog box, type the note.
7. Select Save to add the note to the case.

## Validation
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com) with an admin account. 2. Navigate to Insider Risk Management > Cases. 3. Select the specific case where the note was added. 4. Click the 'Case notes' tab. 5. Verify that the note text, timestamp, and author are displayed correctly in the case notes list. 6. Optionally, use the 'Export' feature to confirm the note is included in the case export.

## Rollback
1. Sign in to the Microsoft Purview portal with an admin account. 2. Go to Insider Risk Management > Cases. 3. Select the case containing the note to be removed. 4. Click the 'Case notes' tab. 5. Locate the note and select 'Delete' (or the ellipsis menu > 'Delete'). 6. Confirm deletion when prompted. 7. Verify the note no longer appears in the case notes list.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
