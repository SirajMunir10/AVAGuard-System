# Implementation: App Protection Policies

**Domain:** Intune
**Subdomain:** App Protection Policies
**Incident Type:** Implementation

## Scenario / Query
How to create and assign an app protection policy to set device risk level using Microsoft Defender for Endpoint integration?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Platforms: iOS/iPadOS and Android only

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure admin access to the Microsoft Intune admin center with Endpoint Security Manager role or equivalent permissions for security-related Mobile apps policies. Custom roles require Assign, Create, Delete, Read, Update, and Wipe rights for the Managed apps permission.
2. Follow the application protection policy creation guide.
3. Configure Defender for Endpoint-specific settings: Under 'Apps', select apps to protect by threat-based policies.
4. Under 'Conditional launch', configure threat level and response actions: Set 'Max allowed device threat level' to one of: Secured (no threats allowed), Low (only low-level threats permitted), Medium (low and medium threats permitted), or High (all threat levels permitted, reporting only).
5. Set 'Actions when threshold exceeded' to either 'Block access' (prevent app access) or 'Wipe data' (remove corporate data from the app).
6. Under 'Assignments', assign to groups of users. The policy evaluates their devices for app-level protection.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com) with an account that has the Endpoint Security Manager role or equivalent permissions. 2. Navigate to 'Apps' > 'App protection policies'. 3. Locate the newly created policy and select it. 4. Under 'Monitor', select 'User status' and verify that the policy is assigned to the intended user groups. 5. On a test iOS/iPadOS or Android device that is a member of the assigned group, sign in with a user account from that group. 6. Open a managed app (e.g., Microsoft Outlook) and confirm that the device risk level enforcement is applied (e.g., access blocked or data wiped if device threat level exceeds the configured threshold). 7. In the Intune admin center, under 'Conditional launch' for the policy, confirm that the 'Max allowed device threat level' and 'Actions when threshold exceeded' settings match the intended configuration.

## Rollback
1. Sign in to the Microsoft Intune admin center with an account that has the Endpoint Security Manager role or equivalent permissions. 2. Navigate to 'Apps' > 'App protection policies'. 3. Select the policy that was created or modified. 4. Under 'Conditional launch', change the 'Max allowed device threat level' to 'Secured' (or the previous value) and set 'Actions when threshold exceeded' to 'Block access' (or the previous action). 5. Alternatively, to remove the policy entirely, select the policy and click 'Delete'. 6. If the policy was assigned to groups, under 'Assignments', remove the groups or change the assignment to 'Not configured'. 7. Verify that the changes take effect by checking user status and testing on a device.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
