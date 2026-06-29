# Troubleshooting: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'Access to this page requires authorization' error when accessing PIM troubleshooting page?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Access to this page requires authorization
- You can try signing in or changing directories

## Error Codes
N/A

## Root Causes
1. User lacks authorization to access the page

## Remediation Steps
1. Try signing in
2. Try changing directories

## Validation
1. Sign in to the Azure portal (https://portal.azure.com) with the affected user account. 2. Navigate to Microsoft Entra ID > Identity Governance > Privileged Identity Management > Troubleshoot. 3. Confirm that the 'Access to this page requires authorization' error no longer appears and the troubleshooting page loads successfully. 4. If the error persists, repeat steps 1-3 after switching to a different directory (tenant) via the Directory + subscription filter in the Azure portal.

## Rollback
1. If the remediation (signing in or changing directories) does not resolve the issue, revert to the original directory by selecting the original tenant from the Directory + subscription filter. 2. Sign out of the Azure portal and sign back in with the original user account. 3. Re-navigate to the PIM troubleshooting page to confirm the original error state is restored. 4. If the error persists after rollback, escalate to a Global Administrator to verify the user's PIM Administrator role assignment.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-troubleshoot>
