# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure a compliance URL for end users to learn about DLP policies in Outlook Win32?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with policy tips in Exchange

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select 'Provide a compliance URL for the end user to learn more about your organization's policies' (only available for Exchange)
2. Configure the site or page that the 'Learn more' link points to from scratch (Microsoft Purview does not provide this functionality out of the box)

## Validation
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the DLP policy that includes policy tips for Exchange. 2. Edit the policy and verify that under 'Policy tips' for Exchange, the checkbox 'Provide a compliance URL for the end user to learn more about your organization's policies' is selected. 3. Confirm that the URL field contains the correct compliance page URL (e.g., https://contoso.com/compliance). 4. Send a test email from Outlook Win32 that triggers the DLP policy tip and verify that the 'Learn more' link in the policy tip points to the configured URL and loads correctly.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies and select the DLP policy that was modified. 2. Edit the policy and under 'Policy tips' for Exchange, uncheck the checkbox 'Provide a compliance URL for the end user to learn more about your organization's policies'. 3. Save the policy. 4. If the URL was configured incorrectly, remove the URL from the field before unchecking the option. 5. Send a test email to confirm that the 'Learn more' link no longer appears in the policy tip.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
