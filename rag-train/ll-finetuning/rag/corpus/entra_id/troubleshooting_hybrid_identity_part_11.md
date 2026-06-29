# Troubleshooting: Hybrid Identity (IdentityDataValidationFailed)

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve IdentityDataValidationFailed error during Microsoft Entra Connect sync due to invalid userPrincipalName?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect sync

## Symptoms
- IdentityDataValidationFailed error during synchronization
- userPrincipalName attribute value has invalid or unsupported characters
- userPrincipalName attribute doesn't follow the required format

## Error Codes
- `IdentityDataValidationFailed`

## Root Causes
1. userPrincipalName attribute value has invalid or unsupported characters
2. userPrincipalName attribute doesn't follow the required format

## Remediation Steps
1. Ensure that the userPrincipalName attribute has supported characters and the required format

## Validation
1. Run the Microsoft Entra Connect Synchronization Service Manager. 2. Go to the 'Connectors' tab and select the Active Directory Connector. 3. Click 'Search Connector Space' and search for the user object that had the error. 4. In the connector space object properties, verify that the 'userPrincipalName' attribute contains only supported characters (letters, numbers, periods, hyphens, underscores, and @) and follows the required format (e.g., user@domain.com). 5. Run a delta sync: Start-ADSyncSyncCycle -PolicyType Delta. 6. Check the Synchronization Service Manager 'Operations' tab to confirm no new IdentityDataValidationFailed errors appear.

## Rollback
1. If the remediation causes issues, restore the original userPrincipalName value from backup or from the on-premises Active Directory attribute. 2. Run a delta sync: Start-ADSyncSyncCycle -PolicyType Delta. 3. Verify that the original error does not reappear. 4. If needed, re-run a full sync: Start-ADSyncSyncCycle -PolicyType Initial.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
