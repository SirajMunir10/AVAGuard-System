# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate why an attribute isn't syncing in Microsoft Entra Connect?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect

## Symptoms
- Attribute not syncing between on-premises Active Directory and Microsoft Entra ID

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View the Microsoft Entra Connector Space object
2. Generate the Preview to view attribute flow from Metaverse to the Connector Space and vice versa

## Validation
1. Open Synchronization Service Manager on the Microsoft Entra Connect server. 2. Select the 'Metaverse Search' tab. 3. Search for the user object that is not syncing correctly. 4. Double-click the user object to open its properties. 5. Click the 'Connectors' tab and select the on-premises Active Directory Connector Space. 6. Click 'Properties' to view the Connector Space object and confirm the attribute value is present. 7. Click the 'Preview' button to generate a preview of the attribute flow from the Metaverse to the Microsoft Entra Connector Space. 8. Verify that the attribute appears in the 'Attribute Flow' section with the expected value and direction. 9. Repeat the preview for the reverse direction (Microsoft Entra Connector Space to Metaverse) if applicable.

## Rollback
1. If the attribute is incorrectly mapped or missing, open the Synchronization Rules Editor from the Start menu. 2. Locate the relevant inbound or outbound synchronization rule that controls the attribute flow. 3. Edit the rule to correct the attribute mapping or restore the previous mapping configuration. 4. Save the rule and run a full synchronization cycle: Start-ADSyncSyncCycle -PolicyType Initial. 5. After the sync completes, repeat the validation steps to confirm the attribute now syncs correctly. 6. If the issue persists, restore the original synchronization rule from backup or re-run the Microsoft Entra Connect configuration wizard to reset default rules.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-attribute-not-syncing>
