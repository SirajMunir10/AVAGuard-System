# Troubleshooting: Virtual Network

**Domain:** Azure
**Subdomain:** Virtual Network
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot VM connectivity issues in Azure Virtual Network when access to the troubleshooting page requires authorization?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Access to the troubleshooting page requires authorization
- Prompt to sign in or change directories

## Error Codes
N/A

## Root Causes
1. Authorization required to access the troubleshooting page

## Remediation Steps
1. Try signing in
2. Try changing directories

## Validation
1. Open a new incognito or private browser window. 2. Navigate to https://portal.azure.com. 3. Sign in with the Azure account that has the required permissions (e.g., Network Contributor or Owner) for the subscription containing the virtual network and VM. 4. In the Azure portal, go to 'Virtual machines', select the affected VM, and under 'Help' select 'Connection troubleshoot'. 5. Verify that the troubleshooting page loads without prompting for sign-in or directory change. 6. Run a connectivity test (e.g., from the VM to another resource) and confirm the test completes successfully.

## Rollback
1. If the troubleshooting page still prompts for authorization, sign out of the current session. 2. Clear browser cache and cookies. 3. Close all browser windows. 4. Open a new browser session and navigate to https://portal.azure.com. 5. Sign in with a different Azure account that has the required permissions (e.g., Global Administrator or User Access Administrator) for the directory. 6. If the issue persists, verify that the user account has the necessary role assignments (e.g., Network Contributor) at the subscription or resource group scope. 7. If needed, assign the required role using Azure RBAC: az role assignment create --assignee <user-principal-name> --role "Network Contributor" --scope /subscriptions/<subscription-id>/resourceGroups/<resource-group-name>.

## References
- <https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-vm-connectivity>
