# Hardening: Microsoft Defender for Cloud â€“ Secure Score

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud â€“ Secure Score
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that the Azure Secure Score in Microsoft Defender for Cloud is lower than expected. Several recommendations related to enabling encryption at rest for Azure SQL Database are marked as 'Unhealthy'. How can the administrator identify and remediate these recommendations to improve the secure score?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender for Cloud is enabled; Azure SQL Database instances exist in the subscription.

## Symptoms
- Secure Score is below target threshold
- Recommendation 'Transparent Data Encryption on SQL databases should be enabled' shows status 'Unhealthy'
- Azure SQL Database audit logs show no recent TDE configuration changes

## Error Codes
N/A

## Root Causes
1. Transparent Data Encryption (TDE) is not enabled on one or more Azure SQL databases
2. The SQL server's Azure Active Directory admin is not configured, preventing automated remediation

## Remediation Steps
1. Navigate to Microsoft Defender for Cloud > Recommendations > 'Transparent Data Encryption on SQL databases should be enabled'
2. Select the unhealthy resources and click 'Fix' to enable TDE via the portal, or use the Azure CLI command: az sql db tde set --resource-group <rg> --server <server> --database <db> --status Enabled
3. Ensure the SQL server has an Azure AD admin assigned to allow Defender for Cloud to apply the setting automatically

## Validation
After remediation, the recommendation status should change to 'Healthy' and the Secure Score should increase. Verify by running: az sql db tde show --resource-group <rg> --server <server> --database <db> --query 'status'

## Rollback
To disable TDE, set the status to 'Disabled' using the same CLI command or portal blade. Note that disabling TDE may affect compliance requirements.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/secure-score-security-controls>
- <https://learn.microsoft.com/en-us/azure/azure-sql/database/transparent-data-encryption-tde-overview>
