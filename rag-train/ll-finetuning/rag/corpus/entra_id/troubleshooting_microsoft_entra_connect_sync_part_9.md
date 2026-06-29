# Troubleshooting: Microsoft Entra Connect Sync

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Connect Sync
**Incident Type:** Troubleshooting

## Scenario / Query
Why is an attribute not syncing between Active Directory and Microsoft Entra ID via Microsoft Entra Connect?

## Environment Context
- **Tenant Type:** hybrid
- **Configuration:** Microsoft Entra Connect with Active Directory

## Symptoms
- Attribute values are not appearing in Microsoft Entra ID as expected after synchronization

## Error Codes
N/A

## Root Causes
1. Synchronization Rules (Inbound or Outbound) may not be processing the attribute correctly
2. Attribute may be missing from the connector space (CS) or metaverse (MV) due to import or synchronization issues

## Remediation Steps
1. Review the Synchronization Steps: Import from AD, Import from Microsoft Entra ID, Synchronization (Inbound and Outbound Rules), Export to AD, Export to Microsoft Entra ID
2. Open the Synchronization Rules Editor from the desktop applications to view the Synchronization Rules
3. Check the Inbound Synchronization Rules to ensure data is brought from CS to MV
4. Check the Outbound Synchronization Rules to ensure data is moved from MV to CS
5. Verify the order of precedence number from lower to higher for the Synchronization Rules

## Validation
1. Open the Synchronization Service Manager on the Microsoft Entra Connect server. 2. Select the 'Connectors' tab, choose the Active Directory connector, and click 'Search Connector Space'. 3. Search for a test user and verify the attribute value appears in the connector space object. 4. Select the 'Metaverse Search' tab, search for the same user, and confirm the attribute value is present in the metaverse. 5. Open the Synchronization Rules Editor, review the inbound rules for the attribute, and ensure the precedence order is correct. 6. Run a full synchronization cycle (Import from AD, Synchronization, Export to Microsoft Entra ID) and verify the attribute appears in Microsoft Entra ID.

## Rollback
1. Open the Synchronization Rules Editor. 2. If a synchronization rule was modified, restore the original rule by reverting to the default rule or reimporting the original rule from backup. 3. If a custom rule was added, delete the custom rule. 4. Run a full synchronization cycle (Import from AD, Synchronization, Export to Microsoft Entra ID). 5. Verify the attribute behavior returns to the previous state. 6. If the issue persists, restore the Microsoft Entra Connect configuration from a recent backup using the 'Restore from backup' option in the configuration wizard.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-attribute-not-syncing>
