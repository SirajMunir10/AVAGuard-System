# Troubleshooting: Azure AD Connect

**Domain:** Entra ID
**Subdomain:** Azure AD Connect
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate why an attribute is not syncing from Active Directory to Microsoft Entra ID using Synchronization Service Manager?

## Environment Context
- **Tenant Type:** hybrid
- **Configuration:** Azure AD Connect with Active Directory Connector

## Symptoms
- Attribute not appearing in Microsoft Entra ID after synchronization

## Error Codes
N/A

## Root Causes
1. Attribute not mapped in Synchronization Rules
2. Custom Synchronization Rule needed

## Remediation Steps
1. Launch Synchronization Service Manager from the desktop applications.
2. Select the Metaverse Search, select Scope by Object Type, select the object using an attribute, and click Search button.
3. Double click the object found in the Metaverse search to view all its attributes.
4. Click on the Connectors tab to look at corresponding object in all the Connector Spaces.
5. Double click on the Active Directory Connector to view the Connector Space attributes.
6. Click on the Preview button, on the following dialog click on the Generate Preview button.
7. Click on the Import Attribute Flow, this shows flow of attributes from Active Directory Connector Space to the Metaverse. Sync Rule column shows which Synchronization Rule contributed to that attribute. Data Source column shows you the attributes from the Connector Space. Metaverse Attribute column shows you the attributes in the Metaverse. Look for the attribute not syncing here. If you don't find the attribute here, then this isn't mapped and you have to create new custom Synchronization Rule to map the attribute.
8. Click on the Export Attribute Flow in the left pane to view the attribute flow from Metaverse back to Active Directory Connector Space using Outbound Synchronization Rules.

## Validation
1. Launch Synchronization Service Manager. 2. Select Metaverse Search, set Scope by Object Type, search for the object using an attribute, and click Search. 3. Double-click the object to view all attributes. 4. Click the Connectors tab and double-click the Active Directory Connector to view Connector Space attributes. 5. Click Preview, then Generate Preview. 6. Click Import Attribute Flow and verify the missing attribute appears in the list with a Sync Rule and Data Source value. 7. Click Export Attribute Flow and confirm the attribute flows via an Outbound Synchronization Rule.

## Rollback
1. If a custom Synchronization Rule was created, open Synchronization Rules Editor. 2. Locate the custom rule, set its status to Disabled, and save. 3. Run a full synchronization cycle: Start-ADSyncSyncCycle -PolicyType Initial. 4. Verify the attribute is no longer synced or returns to previous behavior. 5. If needed, delete the custom rule after disabling and confirming no adverse effects.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-attribute-not-syncing>
