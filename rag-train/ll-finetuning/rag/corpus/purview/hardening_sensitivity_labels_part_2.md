# Hardening: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Hardening

## Scenario / Query
How do I lock the privacy setting for a Microsoft 365 group or team using a sensitivity label?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels with scope including groups and sites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Private or Public for the Privacy setting when configuring the label.
2. The settings of Public or Private set and lock the privacy setting when you apply this label to the container.
3. Your chosen setting replaces any previous privacy setting that might be configured for the container, and locks the privacy value so it can be changed only by first removing the sensitivity label from the container.
4. After you remove the sensitivity label, the privacy setting from the label remains and users can now change it again.

## Validation
1. Verify that the sensitivity label has been published and applied to the target Microsoft 365 group or team. Use the Microsoft Purview compliance portal to confirm the label is assigned. 2. Check the privacy setting of the group or team (e.g., via Azure AD or Teams admin center) to ensure it matches the setting configured in the label (Private or Public). 3. Attempt to change the privacy setting directly (e.g., via Teams or SharePoint) and confirm that the change is blocked, indicating the setting is locked by the label. 4. Remove the sensitivity label from the container and verify that the privacy setting remains as set by the label, and that users can now modify it.

## Rollback
1. Remove the sensitivity label from the affected Microsoft 365 group or team. 2. Manually set the privacy setting to the desired value (Private or Public) using the Teams admin center, Azure AD, or SharePoint admin center. 3. If the label was intended to enforce a specific privacy setting but caused issues, consider editing the label to remove the privacy setting lock (set to 'None') and republish it. 4. Reapply the updated label to the container to restore the previous behavior without locking privacy.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
