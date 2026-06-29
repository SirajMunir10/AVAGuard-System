# Implementation: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Implementation

## Scenario / Query
How to create retention labels to supplement retention policies for exceptions in SharePoint, OneDrive, or Exchange?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Retention labels for data lifecycle management

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure you understand the principles of retention before using retention labels to supplement a retention policy for specific SharePoint, OneDrive, or Exchange items.
2. Typically, use retention labels to retain specific items longer than an applied retention policy, override automatic deletion at the end of the retention period, or apply a different deletion period.
3. As a typical example: The majority of content on your SharePoint sites need to be retained for three years, which is covered with a retention policy. But you have some contract documents that must be retained for seven years. These exceptions can be addressed with retention labels.
4. After assigning the retention policy to all SharePoint sites, apply the retention labels to the contract documents. All SharePoint items will be retained for three years, and just the contract documents will be retained for seven years.
5. For more examples of how retention labels can be used as exceptions to retention policies, see Combining retention policies and retention labels.
6. Retention labels also support more capabilities than retention policies. For more information, see Compare capabilities for retention policies and retention labels.
7. Create retention labels from the Records management solution rather than Data lifecycle management if you need to use retention labels to manage high-value items for business, legal, or regulatory record-keeping requirements. For example, you want to use event-based retention or disposition review. For instructions, see Use file plan to create and manage retention labels.

## Validation
1. Verify that the retention label is published and visible in the Microsoft Purview compliance portal under Data Lifecycle Management > Labels > Retention labels. 2. Confirm the label can be applied manually to a test document in SharePoint or OneDrive, or to an email in Exchange Online. 3. Use the Get-RetentionComplianceLabel PowerShell cmdlet to list the label and its retention settings. 4. Check that the label's retention period matches the intended exception (e.g., 7 years for contract documents). 5. Validate that the label overrides the broader retention policy by reviewing the effective retention period for the labeled item using the Get-RetentionCompliancePolicy cmdlet or the compliance portal's label analytics.

## Rollback
1. Remove the retention label from any test items by applying a different label or clearing the label if allowed. 2. Delete the retention label from the Microsoft Purview compliance portal under Data Lifecycle Management > Labels > Retention labels. 3. If the label was published, remove the label policy under Label policies > Publish labels. 4. Use the Remove-RetentionComplianceLabel PowerShell cmdlet to delete the label programmatically. 5. Confirm that the original retention policy (e.g., 3-year retention) is now the only retention rule applied to the affected items.

## References
- <https://learn.microsoft.com/en-us/purview/create-retention-labels-data-lifecycle-management>
