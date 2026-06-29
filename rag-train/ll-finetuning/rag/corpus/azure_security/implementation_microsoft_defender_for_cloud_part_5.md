# Implementation: Microsoft Defender for Cloud (AuthorizationFailed)

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Implementation

## Scenario / Query
How do I enable the 'Email notifications for high severity alerts' setting in Microsoft Defender for Cloud when the tenant has Azure Policy denying creation of security contacts?

## Environment Context
- **Tenant Type:** Enterprise (multi-subscription)
- **Configuration:** Azure Policy assignment 'Configure Microsoft Defender for Cloud to use a specific security contact email' is set to Deny; no SecurityContact resource exists

## Symptoms
- No email notifications are received for high-severity Defender for Cloud alerts
- Azure portal shows 'Email notifications' setting as grayed out with message 'Contact details are not configured'
- Attempts to create a SecurityContact via portal or API fail with a policy violation

## Error Codes
- `AuthorizationFailed`
- `PolicyViolation`

## Root Causes
1. An Azure Policy denies creation or modification of the SecurityContact resource type
2. The security contact email address has never been set at the subscription or management group scope

## Remediation Steps
1. Identify the specific policy assignment that denies SecurityContact creation using Azure Policy > Assignments and review the policy definition details
2. Request an exception or modify the policy assignment to allow the required SecurityContact resource (e.g., change effect from Deny to Audit or add an exclusion scope)
3. Once the policy allows, configure the security contact email using the Azure portal: Microsoft Defender for Cloud > Environment settings > subscription > Email notifications. Enter a valid email address for 'All users with the following roles' or 'Additional email addresses'
4. Alternatively, use the Azure CLI command: az security contact create --email 'admin@contoso.com' --phone '' --alert-notifications 'on' --notifications-to-admins 'on' (as documented by Microsoft)

## Validation
Verify by triggering a test alert (e.g., simulate a security alert) and confirming that the notification email is received at the configured address. Also check the SecurityContact resource exists via Get-AzSecurityContact.

## Rollback
Remove the SecurityContact resource: az security contact delete --name 'default'. If the policy was modified, revert the policy assignment to its original Deny effect.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/configure-email-notifications>
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/security-contact>
