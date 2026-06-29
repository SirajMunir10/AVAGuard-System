# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate changes to network access policy in SharePoint or OneDrive?

## Environment Context
- **Tenant Type:** SharePoint/OneDrive
- **Configuration:** Network access policy (trusted network boundary)

## Symptoms
- Users unable to access SharePoint or OneDrive resources from certain IP ranges
- Unexpected changes to location-based access controls

## Error Codes
N/A

## Root Causes
1. A SharePoint or global administrator changed the location-based access policy in the SharePoint admin center or by using SharePoint PowerShell

## Remediation Steps
1. Review audit log for NetworkAccessPolicyChanged activity
2. Identify the administrator who made the change
3. Verify the authorized IP address ranges in the policy
4. Reconfigure the network access policy to the correct IP ranges if unauthorized change occurred

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user with the Audit Log or View-Only Audit Log role. 2. Navigate to Solutions > Audit. 3. Under the Search tab, set the Date range to cover the period of the suspected change. 4. In the Activities list, select 'NetworkAccessPolicyChanged' under the SharePoint or OneDrive activity categories. 5. Click Search and confirm that the audit log returns entries showing the change, including the user who performed it, the date/time, and the modified IP ranges. 6. Verify that the current network access policy in the SharePoint admin center (Access Policy > Network location) matches the authorized IP ranges expected by the organization.

## Rollback
1. If the audit log reveals an unauthorized change, sign in to the SharePoint admin center (https://admin.microsoft.com/SharePoint) as a SharePoint administrator. 2. Go to Policies > Access Policy > Network location. 3. Select the location-based access policy that was changed. 4. Edit the policy to restore the previously authorized IP address ranges (documented from the audit log or organizational records). 5. Save the policy. 6. Alternatively, use SharePoint PowerShell: Connect-SPOService -Url https://<tenant>-admin.sharepoint.com; Set-SPOTenant -IPAddressAllowList '<comma-separated IP ranges>'. 7. Test access from a blocked IP range to confirm the policy is enforced correctly.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
