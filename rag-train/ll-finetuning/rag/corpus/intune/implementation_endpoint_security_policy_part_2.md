# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How do I determine whether a specific Attack surface reduction profile requires granular Attack surface reduction permission or Security baselines permission?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Attack surface reduction policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Check the specific profile requirements for Attack surface reduction policies.
2. Some profiles use the granular Attack surface reduction permission while others require Security baselines permission.
3. For detailed profile-specific requirements, see Custom role considerations.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Attack surface reduction.
3. Select the specific Attack surface reduction profile in question.
4. Review the profile details and note the policy type (e.g., 'App and browser isolation', 'Exploit protection', etc.).
5. Go to Tenant administration > Roles > All roles and select the custom role assigned to the user.
6. Under 'Permissions', expand 'Endpoint security' and check if 'Attack surface reduction' is listed as a granular permission. If not, check if 'Security baselines' permission is present.
7. Alternatively, use the Microsoft Graph API: GET https://graph.microsoft.com/beta/deviceManagement/configurationPolicies?$filter=name eq 'ProfileName' and review the '@odata.type' property to determine if the profile is based on a security baseline or a custom policy.

## Rollback
1. If the remediation involved assigning a custom role with granular Attack surface reduction permission, revert to the previous role assignment by removing that permission from the custom role.
2. If the remediation involved assigning a role with Security baselines permission, remove that permission from the custom role.
3. To revert using Microsoft Graph API: Update the role assignment by removing the relevant permission using PATCH https://graph.microsoft.com/beta/deviceManagement/roleAssignments/{roleAssignmentId} with a JSON body that omits the added permission.
4. Verify that the user's effective permissions return to the original state by repeating the validation steps and confirming the profile is no longer accessible if intended.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
