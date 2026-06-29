# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How do I modify an existing endpoint security policy in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Endpoint Security Policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the policy to modify.
2. Select Edit for each section requiring changes (Basics, Assignments, Scope tags, Configuration settings).
3. Save changes after editing a section before proceeding to the next.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Manage > Policies. 2. Select the policy that was modified. 3. Verify that the Basics, Assignments, Scope tags, and Configuration settings sections reflect the intended changes. 4. Check the policy status to ensure it is saved and applied. 5. Optionally, use the 'Review + save' option to confirm all changes are correct.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Manage > Policies. 2. Select the policy that was modified. 3. For each section that was changed (Basics, Assignments, Scope tags, Configuration settings), select Edit and revert the settings to their previous values. 4. Save changes after editing each section. 5. Verify the policy status to ensure the rollback is applied.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
