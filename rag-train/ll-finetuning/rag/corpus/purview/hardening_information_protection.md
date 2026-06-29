# Hardening: Information Protection

**Domain:** Purview
**Subdomain:** Information Protection
**Incident Type:** Hardening

## Scenario / Query
How do I identify and remediate sensitivity labels that are not published to any user or group, leaving them orphaned and ineffective for data classification?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Purview Information Protection
- **Configuration:** Sensitivity labels configured in Microsoft Purview compliance portal but not assigned to any publish policy

## Symptoms
- Sensitivity labels appear in the Microsoft Purview compliance portal but are not available to users in Office apps
- Users cannot apply certain sensitivity labels to documents or emails
- Audit logs show no label application events for specific labels

## Error Codes
N/A

## Root Causes
1. Sensitivity label was created but never added to a label policy
2. Label policy was deleted or disabled after the label was created
3. Label policy scope excludes all users and groups

## Remediation Steps
1. In the Microsoft Purview compliance portal, navigate to Information Protection > Label policies
2. Create a new label policy or edit an existing one to include the orphaned label
3. Assign the policy to the appropriate users, groups, or entire tenant
4. Publish the policy and verify the label appears in supported Office apps

## Validation
Confirm the label is listed in the 'Published labels' section of a label policy and that users in the assigned scope can see and apply the label in Word, Excel, or Outlook.

## Rollback
Remove the label from the policy or delete the policy to unpublish the label again.

## References
- Microsoft Learn: 'Create and publish sensitivity labels' - https://learn.microsoft.com/en-us/purview/create-sensitivity-labels
