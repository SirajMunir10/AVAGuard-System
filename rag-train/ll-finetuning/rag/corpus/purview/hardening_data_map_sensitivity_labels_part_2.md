# Hardening: Data Map / Sensitivity Labels

**Domain:** Purview
**Subdomain:** Data Map / Sensitivity Labels
**Incident Type:** Hardening

## Scenario / Query
A Microsoft Purview administrator notices that sensitivity labels are not being applied to assets in the Purview Data Map, even though the labels are published and the scanning rule set includes the auto-labeling policy. What configuration step is likely missing?

## Environment Context
- **Tenant Type:** Enterprise (E5 or A5 with Purview)
- **Configuration:** Sensitivity labels published in Microsoft 365 Compliance Center, but not yet registered in the Purview Data Map via the 'Manage sensitivity labels' option in the Data Map management settings.

## Symptoms
- Sensitivity labels appear in the Microsoft 365 Compliance Center but are not visible or applied to assets in the Purview Data Map.
- Auto-labeling policies do not trigger on scanned data assets.
- No errors are reported during scanning or labeling policy execution.

## Error Codes
N/A

## Root Causes
1. Sensitivity labels must be explicitly registered in the Purview Data Map before they can be applied to assets. This is a separate step from publishing labels in the Compliance Center.
2. The Purview Data Map does not automatically synchronize labels from the Microsoft 365 Compliance Center.

## Remediation Steps
1. In the Microsoft Purview governance portal, navigate to Data Map > Sensitivity labels.
2. Select 'Manage sensitivity labels' and then choose the labels to register from the Microsoft 365 Compliance Center.
3. Confirm the registration and allow up to 24 hours for the labels to propagate to the Data Map.
4. Re-run the scan or trigger a new scan to apply the labels to assets.

## Validation
After registering the labels, verify that assets in the Data Map display the correct sensitivity label in their properties. You can also run a test scan on a small dataset to confirm auto-labeling works.

## Rollback
To remove a registered sensitivity label from the Data Map, go to Data Map > Sensitivity labels, select the label, and choose 'Unregister'. This will not delete the label from the Compliance Center.

## References
- <https://learn.microsoft.com/en-us/purview/how-to-enable-sensitivity-labels>
