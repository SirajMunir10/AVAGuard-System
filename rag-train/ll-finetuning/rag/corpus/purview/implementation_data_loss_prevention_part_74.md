# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to block access for specific external domains or users in SharePoint and OneDrive DLP policies?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with 'Block access for specific external domains or users' (public preview, SPO/ODB only)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure the DLP policy to block access for specific external domains or users
2. Access is denied when a configured external user or domain attempts to open, preview, or download the file
3. An audit record is generated per blocked access attempt (subject to preview limitations)
4. Events can be reviewed in DLP Alerts, Activity Explorer, and Audit logs; the event contains the blocked user's email

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user with DLP compliance management permissions.
2. Navigate to Data Loss Prevention > Policies and select the DLP policy that was configured to block access for specific external domains or users.
3. In the policy details, verify that under 'Actions' the setting 'Block access for specific external domains or users' is enabled and that the correct external domains or user email addresses are listed.
4. As a test, attempt to access (open, preview, or download) a protected file in SharePoint Online or OneDrive for Business from an external user account that belongs to one of the blocked domains or is one of the blocked users. Confirm that access is denied and an error message is displayed.
5. Check that an audit record is generated for the blocked access attempt by searching the Audit log in the compliance portal (Audit > Search) for the user's email and the activity 'File accessed by external user' or similar DLP-related event. Alternatively, review DLP Alerts or Activity Explorer for the corresponding event.

## Rollback
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user with DLP compliance management permissions.
2. Navigate to Data Loss Prevention > Policies and select the DLP policy that was configured to block access for specific external domains or users.
3. In the policy, edit the action 'Block access for specific external domains or users' by either:
   - Removing the specific external domains or user email addresses from the list, or
   - Disabling the action entirely (set to 'Off' or remove the block condition).
4. Save the policy changes and allow time for the update to propagate (typically up to 1 hour).
5. Verify that external users from previously blocked domains or the previously blocked users can now access the protected files in SharePoint Online or OneDrive for Business as expected.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
