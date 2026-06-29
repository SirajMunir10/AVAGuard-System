# Troubleshooting: Security Alerts

**Domain:** Defender for Endpoint
**Subdomain:** Security Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot access issues when viewing security alerts in Microsoft Defender for Cloud?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Access to this page requires authorization
- You can try signing in or changing directories

## Error Codes
N/A

## Root Causes
1. Insufficient authorization to access the security alerts page

## Remediation Steps
1. Try signing in
2. Try changing directories

## Validation
1. Open a new InPrivate/Incognito browser session and navigate to https://portal.azure.com. 2. Sign in with the affected user account. 3. Go to Microsoft Defender for Cloud > Security alerts. 4. Confirm the alerts page loads without the 'Access to this page requires authorization' or 'You can try signing in or changing directories' errors. 5. Verify that the user can view the list of security alerts and click into any alert to see details.

## Rollback
1. If the user still sees the authorization error, instruct them to sign out of all sessions and clear browser cache/cookies. 2. Have the user sign in again using the correct tenant directory (e.g., select the appropriate directory from the directory picker). 3. If the issue persists, verify the user has the required RBAC role (e.g., Security Reader, Security Admin) assigned at the subscription or resource group scope. 4. If roles are missing, assign the appropriate role via Azure Active Directory > Roles and administrators or via Subscription > Access control (IAM). 5. After role assignment, ask the user to sign out and sign back in, then retry accessing the Security alerts page.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-overview>
