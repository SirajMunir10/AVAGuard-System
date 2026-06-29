# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure File activities for all apps in DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** File activities for all apps option in DLP policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select either Don't restrict file activities or Apply restrictions to specific activities.
2. When you select Apply restrictions to specific activities, the actions that you select are applied when a user has accessed a DLP protected item.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Open the DLP policy that was configured with 'File activities for all apps'. 3. Under 'Location' > 'Devices', confirm that 'File activities for all apps' is set to either 'Don't restrict file activities' or 'Apply restrictions to specific activities' as intended. 4. If 'Apply restrictions to specific activities' was selected, verify that the specific activities (e.g., Copy to clipboard, Print, etc.) are checked. 5. Use a test user account to perform a file activity (e.g., copy a protected file to a USB drive) and confirm that the DLP policy blocks or audits the action as expected.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Open the DLP policy where the change was made. 3. Under 'Location' > 'Devices', set 'File activities for all apps' back to its original configuration (e.g., if you changed to 'Apply restrictions to specific activities', revert to 'Don't restrict file activities' or uncheck the specific activities). 4. Save the policy and allow up to 24 hours for the change to propagate. 5. Verify that the previous behavior is restored by testing with a user account that was previously affected.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
