# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I connect Microsoft Defender XDR to Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Microsoft Entra tenant
- **Configuration:** Microsoft Sentinel workspace, Microsoft Defender XDR licensing

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure you have a valid license for Microsoft Defender XDR, as described in Microsoft Defender XDR prerequisites.
2. Your user must have the Security Administrator role on the tenant you want to stream the logs from, or the equivalent permissions.
3. You must have read and write permissions on your Microsoft Sentinel workspace.
4. To make any changes to the connector settings, your account must be a member of the same Microsoft Entra tenant with which your Microsoft Sentinel workspace is associated.
5. Install the Microsoft Defender XDR solution from the Content Hub in Microsoft Sentinel. For more information, see Discover and manage Microsoft Sentinel out-of-the-box content.
6. If you're working in the Defender portal, this solution is automatically installed.
7. Grant access to Microsoft Sentinel as appropriate for your organization. For more information, see Roles and permissions in Microsoft Sentinel.
8. For on-premises Active Directory sync via Microsoft Defender for Identity: Your tenant must be onboarded to Microsoft Defender for Identity.
9. You must have the Microsoft Defender for Identity sensor installed. For more information, see Deploy Microsoft Defender for Identity.

## Validation
1. Confirm Microsoft Defender XDR licensing: Navigate to Microsoft 365 admin center > Billing > Licenses and verify that Microsoft Defender XDR licenses are assigned to relevant users. 2. Verify user permissions: In Microsoft Entra admin center, go to Roles and administrators, confirm the user has Security Administrator role. 3. Check Microsoft Sentinel workspace permissions: In Azure portal, open your Sentinel workspace, select Access control (IAM), verify the user has Contributor or equivalent role. 4. Confirm tenant association: Ensure the user account is in the same Microsoft Entra tenant as the Sentinel workspace. 5. Validate solution installation: In Microsoft Sentinel, go to Content hub, search for 'Microsoft Defender XDR', confirm it shows as 'Installed'. 6. For Defender for Identity: In Microsoft 365 Defender portal, navigate to Settings > Identities, confirm the tenant is onboarded and sensor is installed.

## Rollback
1. Remove the Microsoft Defender XDR solution: In Microsoft Sentinel, go to Content hub, find the solution, select 'Uninstall'. 2. Revoke user permissions: In Microsoft Entra admin center, remove the Security Administrator role from the user. 3. Remove workspace permissions: In Azure portal, under the Sentinel workspace's Access control (IAM), remove the user's Contributor role. 4. If Defender for Identity sensor was installed, uninstall it from the on-premises server via Add/Remove Programs. 5. Disconnect the data connector: In Microsoft Sentinel, go to Data connectors, select 'Microsoft Defender XDR', click 'Disconnect'.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
