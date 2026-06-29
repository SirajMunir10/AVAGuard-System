# Troubleshooting: Microsoft Entra Connect

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Connect
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot an attribute that is not syncing from on-premises Active Directory to Microsoft Entra ID via Microsoft Entra Connect?

## Environment Context
- **Tenant Type:** hybrid
- **Configuration:** Microsoft Entra Connect with on-premises Active Directory

## Symptoms
- An attribute from on-premises Active Directory is not appearing in Microsoft Entra ID after synchronization

## Error Codes
N/A

## Root Causes
1. Attribute may not be mapped in the synchronization rules
2. Attribute may be filtered out by scoping filters
3. Attribute may not be flowing through the Connector Space (CS) to Metaverse (MV) pipeline

## Remediation Steps
1. Check the synchronization rules in the Microsoft Entra Connect Synchronization Rules Editor to verify the attribute mapping
2. Verify that the attribute is present in the Connector Space (CS) for the on-premises Active Directory connector
3. Check the Metaverse (MV) to see if the attribute is being projected or joined correctly
4. Review the export attribute flow to Microsoft Entra ID

## Validation
1. Open the Synchronization Service Manager on the Microsoft Entra Connect server. 2. Go to the 'Connectors' tab, select the on-premises Active Directory connector, and click 'Search Connector Space'. 3. Search for a test user and verify the attribute appears in the 'Connector Space Object Properties' under the correct attribute name. 4. Go to the 'Metaverse Search' tab, search for the same user, and confirm the attribute is present in the 'Metaverse Object Properties'. 5. Open the Synchronization Rules Editor, locate the inbound and outbound rules for the attribute, and verify the mapping expression and scoping filters are correct. 6. Run a preview of the synchronization step for the user and confirm the attribute flows from CS to MV and then to the Microsoft Entra ID connector space.

## Rollback
1. Open the Synchronization Rules Editor. 2. Locate the synchronization rule that was modified for the attribute mapping. 3. If a new rule was created, disable or delete it. 4. If an existing rule was edited, revert the mapping expression or scoping filter to its original state (use a backup or previous configuration if available). 5. Run a full synchronization cycle: Start-ADSyncSyncCycle -PolicyType Initial. 6. Verify the attribute behavior returns to the previous state using the validation steps above.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-attribute-not-syncing>
