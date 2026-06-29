# Governance: Governance

**Domain:** Sentinel
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
A security operations team notices that Microsoft Sentinel is not ingesting audit logs from Azure Active Directory (now Microsoft Entra ID). The workspace was created with default permissions. How can the team verify and correct the missing data connector configuration to ensure governance and compliance requirements are met?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with default RBAC; Azure AD (Entra ID) diagnostics settings not configured

## Symptoms
- No AuditLogs or SignInLogs tables appearing in Sentinel Log Analytics workspace
- Data connector for Azure Active Directory shows 'disconnected' status in Sentinel
- Compliance reports missing sign-in and audit events

## Error Codes
N/A

## Root Causes
1. Diagnostic settings for Azure AD (Entra ID) not configured to stream logs to the Sentinel Log Analytics workspace
2. Insufficient permissions (e.g., missing Security Administrator or Global Reader role) to enable the data connector

## Remediation Steps
1. Ensure the user configuring the connector has at least the Security Administrator role in Azure AD (Entra ID) and Contributor permissions on the Log Analytics workspace.
2. In Microsoft Sentinel, navigate to Content hub, install the Azure Active Directory solution, then open the Azure Active Directory data connector.
3. Select the connector configuration blade, choose the appropriate log types (AuditLogs, SignInLogs, NonInteractiveUserSignInLogs, etc.), and click 'Apply Changes'.
4. Alternatively, configure diagnostic settings in Azure AD (Entra ID) > Monitoring > Diagnostic settings to stream logs to the Sentinel workspace.
5. Wait up to 15 minutes for ingestion to begin; verify data in the Log Analytics workspace by running a query: `AuditLogs | take 10`.

## Validation
Run `AuditLogs | take 10` and `SignInLogs | take 10` in the Sentinel Log Analytics workspace. Confirm that the Azure AD data connector shows 'Connected' status.

## Rollback
Disable the Azure AD data connector in Sentinel, and remove the diagnostic settings in Azure AD (Entra ID) that stream logs to the workspace.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-active-directory>
