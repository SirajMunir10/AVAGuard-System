# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to create an endpoint security policy in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint security policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Intune admin center.
2. Go to Endpoint security > select the desired policy type > Create Policy.
3. Configure policy basics: Platform: Choose the target device platform (options vary by policy type). Profile: Select from available profiles for your chosen platform. Select Create to continue.
4. Complete policy configuration: Basics: Provide a descriptive name and optional description for the profile. Configuration settings: Expand each group of settings and configure the settings you want to manage with this profile. When done configuring settings, select Next. Scope tags: Choose Select scope tags to open the Select tags pane to assign scope tags to the profile (optional). Assignments: Select the groups to receive this profile. See Assign user and device profiles. Review + create: Review your configuration and select Create when ready. The new profile then appears in the policy list.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > select the policy type you created (e.g., Antivirus, Firewall, etc.).
3. Confirm the new profile appears in the policy list with the expected name and platform.
4. Select the profile and review the Configuration settings, Scope tags, and Assignments to ensure they match your intended configuration.
5. On a target device that is a member of the assigned group, verify the policy is applied by checking the device's policy status in Intune (Devices > All devices > select device > Device configuration).

## Rollback
1. Sign in to the Microsoft Intune admin center.
2. Navigate to Endpoint security > select the policy type containing the problematic profile.
3. Locate the profile you created and select it.
4. Choose Delete from the action bar and confirm deletion.
5. If the profile was already assigned, the policy will be removed from devices on their next check-in. To expedite, you can force a sync on affected devices via Intune (Devices > select device > Sync).
6. If you need to restore a previous configuration, recreate the profile with the original settings and assignments.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
