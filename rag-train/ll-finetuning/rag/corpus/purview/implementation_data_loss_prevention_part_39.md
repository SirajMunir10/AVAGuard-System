# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure a DLP rule to block uploads of sensitive data to GitHub URLs that do not contain my organization's name?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with URL contains text condition

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a DLP rule that uses the 'URL contains text' condition to detect when the URL of an unmanaged cloud app contains specified text strings.
2. Use the condition to scope DLP rules to specific URLs, or as an exception to exclude specific URLs from policy enforcement.
3. For example, create a rule that blocks uploading sensitive data to any GitHub URL that doesn't contain your organization's name while allowing uploads to your organization's GitHub repositories.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy you created. 3. Under 'Rules', click on the rule that blocks uploads to GitHub URLs not containing your organization's name. 4. Verify the rule's conditions: a. Confirm 'Content contains' is set to the sensitive info types you want to protect. b. Confirm 'URL contains text' condition is configured with a list of GitHub URLs that do NOT include your organization's name (e.g., 'github.com/' but not 'github.com/yourorg'). 5. Use the DLP test feature (if available) or simulate a file upload to a GitHub URL without your org name to ensure the action is blocked. 6. Check DLP activity reports for any alerts or matches for this rule.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the DLP policy you created. 2. Under 'Rules', locate the rule that blocks uploads to GitHub URLs not containing your organization's name. 3. Edit the rule: a. Remove or modify the 'URL contains text' condition to either remove the restriction or change it to allow all GitHub URLs. b. Alternatively, set the rule action to 'Audit only' instead of 'Block'. 4. Save the policy. 5. If the rule is no longer needed, delete the rule entirely from the policy. 6. Monitor DLP activity reports to confirm the change took effect and no unintended blocks occur.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
