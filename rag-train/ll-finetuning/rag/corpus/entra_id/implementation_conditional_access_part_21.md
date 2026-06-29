# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure Named Locations for Conditional Access policies to block sign-ins from specific IP ranges or countries?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create logical groupings of IP address ranges or countries and regions using Named Locations.
2. Create a policy for all apps that blocks sign-in from that named location.
3. Exempt administrators from this policy.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Named locations. 3. Verify the named location (IP ranges or countries) is listed with the correct configuration. 4. Navigate to Protection > Conditional Access > Policies. 5. Confirm the blocking policy exists, is set to 'On', and targets the named location. 6. Confirm the policy includes an exclusion for the administrator group. 7. Use the 'What If' tool in Conditional Access to simulate a sign-in from a blocked IP or country for a non-admin user and verify the policy applies (block). 8. Use the 'What If' tool to simulate a sign-in from a blocked IP or country for an admin user and verify the policy does not apply.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the blocking policy and set its state to 'Off' or delete the policy. 4. Navigate to Protection > Conditional Access > Named locations. 5. Delete or edit the named location to remove the IP ranges or countries. 6. Verify that sign-ins from previously blocked IPs or countries are now allowed for non-admin users.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
