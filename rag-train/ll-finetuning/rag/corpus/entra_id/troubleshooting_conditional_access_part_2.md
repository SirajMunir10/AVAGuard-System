# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How can I determine why a Conditional Access policy applies or doesn't apply to a sign-in event when a user accesses multiple resources like Microsoft Teams?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Conditional Access policies enabled or in report-only mode

## Symptoms
- User signs in to an app like Microsoft Teams but Conditional Access policy applies unexpectedly across multiple resources
- Admin cannot determine which resource triggered a Conditional Access policy

## Error Codes
N/A

## Root Causes
1. Conditional Access policies apply to all resources requested during a sign-in event, not just the primary app the user thinks they are signing into

## Remediation Steps
1. Navigate to the sign-in logs in the Entra ID portal
2. Select the relevant sign-in event
3. Go to the Conditional Access tab
4. Select a policy to view the Audience report under the Resource section
5. Use the audience report to identify which resources (audiences) in the list are in scope of the policy

## Validation
Check the Audience report in the sign-in logs for all enabled or report-only policies to confirm which resources are in scope

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
